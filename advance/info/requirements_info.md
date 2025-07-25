## 📄 requirements_info.txt
Explanation of libraries listed in `requirements.txt`

---

**1. nmap**
- **Purpose**: Interface with the Nmap tool for network scanning.

- **Used In**: `scanner.py`

- **Why It's Needed**: Enables service/version detection, OS fingerprinting, and traceroute. It wraps around the Nmap command-line tool via Python.

---

**2. requests**
- **Purpose**: Simplified HTTP requests handling in Python.

- **Used In**: `cve_lookup.py`

- **Why It's Needed**: Used to send and handle API requests to Vulners or other CVE databases to fetch vulnerability data based on scanned services.

---

**3. fpdf**

- **Purpose**: Generate PDF files using Python.

- **Used In**: `generate_report.py`

- **Why It's Needed**: Enables creation of clean, formatted vulnerability scan reports in PDF format, including CVEs, risks, traceroute data, and more.


---


✅ These packages form the backbone of the scanner's functionality—network discovery, vulnerability fetching, and reporting.