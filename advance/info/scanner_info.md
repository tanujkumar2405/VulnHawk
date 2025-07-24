# 🔍 Advance Vulnerability Scanner – scanner.py Overview

## 📌 Description

`scanner.py` is the core scanning script of the Vulnerability Scanner Tool. It performs a comprehensive scan of the target IP/domain, detecting:

- Open ports and service versions

- Operating system fingerprinting

- Uptime and last boot time

- Traceroute hops

- Real-time CVE lookups for each service

It uses `nmap` for scanning, parses the XML output for deep inspection, and integrates with a `generate_report.py` module to optionally export a detailed PDF report.


---


## ⚙️ Functional Features

| Feature              | Description                                                            |
| -------------------- | ---------------------------------------------------------------------- |
| 🔎 Service Detection | Uses `-sV` to detect version information for open services             |
| ⚙️ Default Scripts   | Enables default NSE scripts using `-sC`                                |
| 🖥 OS Detection      | Detects the OS and accuracy using `-O`                                 |
| 🕓 Uptime Detection  | Extracts system uptime and last boot timestamp                         |
| 🌐 Traceroute        | Uses `--traceroute` and parses raw XML to show hops                    |
| 🛡 CVE Lookup        | Uses `search_cve(product, version)` to fetch real-time vulnerabilities |
| 📄 PDF Reporting     | Option to generate a PDF report for scanned data                       |



---


## 📁 Modules Used

- `nmap`: Python wrapper for the Nmap scanner

- `os`: For system-level operations

- `xml.etree.ElementTree`: For XML parsing of traceroute data

- `generate_report`: Handles PDF generation

- `cve_lookup`: Custom module to search CVEs for detected services


---


## 📥 Input

- Target: Any valid domain or IP address (e.g., example.com, 192.168.1.1)

- Prompted at runtime.


---


## 📤 Output

- Prints:

    - Open ports, service names, and versions

    - Associated CVEs with CVSS scores

    - OS match and accuracy

    - Uptime and boot info

    - Traceroute hops

-Optionally saves a PDF report via `generate_report.py`


---


## 🧠 Notes

Ensure Nmap is installed on your system.

The `search_cve` function should handle timeouts and rate limits when querying CVE sources.

Useful for penetration testers, network administrators, and security researchers.


---


## 🖥 Example Usage

```bash
$ python3 scanner.py

Enter target IP/domain: scanme.nmap.org

[+] Scanning scanme.nmap.org for service version...
Host: scanme.nmap.org (scanme.nmap.org)
State: up
...
Do you want to generate a PDF report? (yes/no): yes
```


---
