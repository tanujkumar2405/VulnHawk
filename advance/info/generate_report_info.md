# 📄 generate_report.py — PDF Report Generator Info

This module is responsible for generating a professional PDF report from the results of the vulnerability scanner. It formats and structures the data including open ports, detected services, OS info, traceroute hops, and identified vulnerabilities (CVEs) into a clean and readable document.

---

## 🔧 Features

- 📑 Generates a well-structured PDF report with:
  - Target info and timestamp
  - Open ports and detected services
  - OS detection and traceroute hops
  - CVEs with CVSS risk scores
  - Visual risk indicator (LOW, MEDIUM, HIGH, CRITICAL)
- ✍️ Styled formatting using custom fonts (DejaVu)
- 📌 Categorizes and limits text for clean layout
- 📊 CVSS risk level legend for clarity

---

## 🛠 Functions

### `generate_pdf_report(target, services, vulnerabilities)`
Generates a timestamped PDF report for the target system.

**Parameters:**
- `target (str)`: IP or domain of the scanned target.
- `services (list[str])`: Lines describing open services, ports, OS info, etc.
- `vulnerabilities (list[dict])`: List of CVEs found with keys `id`, `title`, `cvss`.

**Output:**
- Creates a timestamped `.pdf` file in the current directory.
- Uses structured sections to display the information cleanly.

---

## 🎨 PDF Layout Sections

- **Header/Footer**: Title, scanner name, author, pagination
- **Scanner Info**: Tool name, author, version
- **Risk Score**: Based on average CVSS score from detected CVEs
- **Target Info**: Domain/IP, resolved IP, date/time
- **Open Ports**: Port summary and list
- **System Info**: OS, uptime, traceroute hops
- **Detected Services**: Numbered list of open services
- **Vulnerabilities**: List of top CVEs with score
- **CVSS Legend**: Clarifies what the score means

---

## 📘 Fonts & Styling

- Uses **DejaVuSans** fonts from a local `fonts/` directory
- Font styles:
  - Normal: DejaVuSans.ttf
  - Bold: DejaVuSans-Bold.ttf
  - Italic: DejaVuSans-Oblique.ttf
- Automatically wraps long lines to fit page width

---

## 📌 Dependencies

- `fpdf`: PDF generation library
- `socket`: For resolving target IPs
- `datetime`: For timestamping reports
- `os`: For font path resolution

Ensure the `fonts/` folder is present with required fonts or modify font usage accordingly.

---

## 📥 Output Example

```plaintext
report_2025-07-24_14-52-10.pdf
```
This PDF can be shared or archived as a security audit document.


---


## 📎 Notes

- Designed to complement scanner.py and cve_lookup.py.

- Handles empty or partial data gracefully.

- Automatically calculates average CVSS score for determining risk level.


---


## 👨‍💻 Author

**Tanuj Kumar**
Python Vulnerability Scanner Project
"Automating the discovery, documenting the threats."


---
