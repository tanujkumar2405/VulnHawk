import socket
from fpdf import FPDF
import os
from datetime import datetime


class PDFReport(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("DejaVu", "", os.path.join("fonts", "DejaVuSans.ttf"), uni=True)
        self.add_font("DejaVu", "B", os.path.join("fonts", "DejaVuSans-Bold.ttf"), uni=True)
        self.add_font("DejaVu", "I", os.path.join("fonts", "DejaVuSans-Oblique.ttf"), uni=True)
        self.set_font("DejaVu", "", 12)

    def header(self):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, "Vulnerability Scan Report", ln=True, align="C")
        self.ln(5)
        self.set_font("DejaVu", "", 12)
        self.cell(0, 10, "Generated using Tanuj's Python Vulnerability Scanner", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def calculate_risk_level(cve_list):
    scores = [cve['cvss'] for cve in cve_list if cve['cvss'] > 0]
    if not scores:
        return "LOW"
    avg = sum(scores) / len(scores)
    if avg >= 9:
        return "CRITICAL"
    elif avg >= 7:
        return "HIGH"
    elif avg >= 4:
        return "MEDIUM"
    else:
        return "LOW"

def generate_pdf_report(target, services, vulnerabilities):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"report_{timestamp}.pdf"

    pdf = PDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("DejaVu", "", 12)
    pdf.set_text_color(0)

    # --- Scanner Info ---
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 10, "Scanner Info:", ln=True)
    pdf.set_font("DejaVu", "", 11)
    pdf.cell(0, 10, "Tool: Python Vulnerability Scanner", ln=True)
    pdf.cell(0, 10, "Author: Tanuj Kumar", ln=True)
    pdf.cell(0, 10, "Report Version: 1.0", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, "-" * 75, ln=True)
    pdf.ln(5)

    # --- Risk Score ---
    risk = calculate_risk_level(vulnerabilities)
    if risk == "CRITICAL":
        pdf.set_text_color(255, 0, 0)
    elif risk == "HIGH":
        pdf.set_text_color(255, 69, 0)
    elif risk == "MEDIUM":
        pdf.set_text_color(255, 140, 0)
    else:
        pdf.set_text_color(0, 128, 0)

    pdf.cell(0, 10, f"Overall Risk Level: {risk}", ln=True)
    pdf.set_text_color(0)

    # --- Target Info ---
    pdf.set_font("DejaVu", "", 12)
    pdf.cell(0, 10, f"Target: {target}", ln=True)
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Date: {formatted_date}", ln=True)

    try:
        resolved_ip = socket.gethostbyname(target)
    except:
        resolved_ip = "Could not resolve"

    pdf.cell(0, 10, f"Resolved IP: {resolved_ip}", ln=True)

    # --- Categorize Lines ---
    system_info_lines = []
    service_lines = []

    for svc in services:
        if svc.startswith("[OS]") or svc.startswith("[Uptime]") or svc.startswith("[Hop"):
            system_info_lines.append(svc)
        elif "[OPEN]" in svc:
            service_lines.append(svc)

    system_info_lines.sort(key=lambda x: (
        0 if x.startswith("[OS]") else
        1 if x.startswith("[Uptime]") else
        2
    ))

    # --- Port Summary ---
    pdf.cell(0, 10, f"Open Ports Detected: {len(service_lines)}", ln=True)
    port_list = []

    for svc in service_lines:
        parts = svc.split()
        if "Port" in parts:
            try:
                idx = parts.index("Port")
                port_list.append(parts[idx + 1])
            except:
                continue

    if port_list:
        pdf.cell(0, 10, "Ports Found: " + ", ".join(port_list), ln=True)

    # --- Divider ---
    pdf.ln(5)
    pdf.cell(0, 10, "-" * 75, ln=True)
    pdf.ln(5)

    # --- System Info Section ---
    if system_info_lines:
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 10, "System Info:", ln=True)
        pdf.set_font("DejaVu", "", 11)
        for line in system_info_lines:
            if len(line) > 180:
                line = line[:180] + "..."
            pdf.set_x(10)
            pdf.multi_cell(0, 8, line, align="L")

        pdf.ln(5)
        pdf.cell(0, 10, "-" * 75, ln=True)
        pdf.ln(5)

    # --- Detected Services Section ---
    if not service_lines:
        pdf.set_text_color(200, 0, 0)
        pdf.cell(0, 10, "No open ports or services detected.", ln=True)
    else:
        pdf.set_text_color(0)
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 10, "Detected Services:", ln=True)
        pdf.ln(5)
        pdf.set_font("DejaVu", "", 11)
        for i, svc in enumerate(service_lines, start=1):
            line = f"{i:02d}) {svc}"
            if len(line) > 500:
                line = line[:500] + "..."
            pdf.set_x(10)
            pdf.multi_cell(190, 8, line, align="L")

        pdf.ln(5)
        pdf.cell(0, 10, "-" * 75, ln=True)
        pdf.ln(5)

    # --- Vulnerabilities Section ---
    if vulnerabilities:
        pdf.ln(5)
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 10, "Vulnerabilities:", ln=True)
        pdf.set_font("DejaVu", "", 11)
        for vuln in vulnerabilities:
            line = f"{vuln['id']} - {vuln['title']} (CVSS: {vuln['cvss']})"
            if len(line) > 160:
                line = line[:160] + "..."
            pdf.multi_cell(0, 8, line)
    else:
        pdf.cell(0, 10, "No CVEs detected or risk is LOW.", ln=True)

    # --- CVSS Legend ---
    pdf.ln(5)
    pdf.set_font("DejaVu", "I", 9)
    pdf.multi_cell(0, 6,
        "CVSS Score Legend:\n"
        "  9.0 – 10.0 : CRITICAL\n"
        "  7.0 – 8.9  : HIGH\n"
        "  4.0 – 6.9  : MEDIUM\n"
        "  0.1 – 3.9  : LOW\n"
        "  0.0        : None / Informational"
    )

    pdf.output(filename)
    print(f"\n[+] Report generated: {filename}")
