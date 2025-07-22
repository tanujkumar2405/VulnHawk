import os
import nmap
from generate_report import generate_pdf_report
from cve_lookup import search_cve
import xml.etree.ElementTree as ET

def scan_with_service_detection(target):
    scanner = nmap.PortScanner()
    print(f"\n[+] Scanning {target} for service version...\n")

    try:
        scanner.scan(hosts=target, arguments='-sV -sC -O --traceroute')
    except nmap.PortScannerError as e:
        print(f"[!] Scan failed: {e}")
        return [], []

    services_found = []
    all_cves = []

    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")

        for proto in scanner[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                serv = scanner[host][proto][port]
                state = serv['state']
                name = serv['name']
                product = serv.get('product', '')
                version = serv.get('version', '')
                info = f"   [OPEN] Port {port} | Service: {name} | {product} {version}"
                print(info)
                services_found.append(info)
        
        # 🛡 CVE Lookup per service
                if product and version:
                    cves = search_cve(product, version)
                    if cves:
                        for cve in cves:
                            line = f"[CVE] {cve['id']} | {cve['title']} | CVSS: {cve['cvss']}"
                            print("   " + line)
                            services_found.append(line)
                            all_cves.append(cve)
                    else:
                        print("   No CVEs found for this service.")


        # --- OS Detection ---
        if 'osmatch' in scanner[host]:
            os_info = scanner[host]['osmatch'][0]
            os_line = f"[OS] {os_info['name']} (Accuracy: {os_info['accuracy']}%)"
            print(f"\n{os_line}")
            services_found.append(os_line)

        # --- Uptime Detection ---
        if 'uptime' in scanner[host]:
            uptime_sec = scanner[host]['uptime']['seconds']
            lastboot = scanner[host]['uptime']['lastboot']
            uptime_line = f"[Uptime] {uptime_sec} seconds - Last boot: {lastboot}"
            print(uptime_line)
            services_found.append(uptime_line)

    # --- Traceroute via raw XML ---
    try:
        raw_xml = scanner.get_nmap_last_output()
        root = ET.fromstring(raw_xml)

        for host in root.findall("host"):
            trace = host.find("trace")
            if trace is not None:
                print("\n[+] Traceroute:")
                for hop in trace.findall("hop"):
                    ttl = hop.attrib.get("ttl", "?")
                    ip = hop.attrib.get("ipaddr", "N/A")
                    host_name = hop.attrib.get("host", "Unknown")
                    rtt = hop.attrib.get("rtt", "N/A")
                    hop_line = f"[Hop {ttl}] {ip} ({host_name}) - RTT: {rtt} ms"
                    print(hop_line)
                    services_found.append(hop_line)
    except Exception as e:
        print(f"[!] Could not parse traceroute hops from XML: {e}")

    if not services_found:
        print("    [!] No open services found.")

    return services_found, all_cves


if __name__ == "__main__":
    target = input("\nEnter target IP/domain: ")
    services, vulnerabilities = scan_with_service_detection(target)

    choice = input("\nDo you want to generate a PDF report? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        generate_pdf_report(target, services, vulnerabilities)
    else:
        print("[i] Skipped PDF generation.")
