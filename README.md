# VulnHawk - Python-Based Vulnerability Scanner

Welcome to **VulnHawk** — a powerful and educational open-source vulnerability scanner built in Python.

This repository includes **two versions** of the scanner:

1. **Basic Scanner** – Great for learning port scanning fundamentals.
2. **Advanced Scanner** – A comprehensive vulnerability assessment tool that integrates Nmap, CVE lookups, PDF reporting, and risk scoring.

---

## 🔍 Table of Contents

* [Project Overview](#project-overview)
* [Basic Scanner](#basic-scanner)

  * [Description](#description)
  * [Usage](#usage)
  * [Requirements](#requirements)
* [Advanced Scanner](#advanced-scanner)

  * [Description](#advanced-description)
  * [Features](#features)
  * [Setup & Requirements](#setup--requirements)
  * [Usage](#advanced-usage)
* [Folder Structure](#folder-structure)
* [Contributing](#contributing)
* [Feedback](#feedback)
* [License](#license)
* [Author](#author)
* [Happy Scanning](#happy-scanning)

---

## Project Overview

**VulnHawk** is built for learners, ethical hackers, and cybersecurity enthusiasts. It starts with the fundamentals and scales to a semi-professional tool that demonstrates:

* Port scanning
* Service fingerprinting
* Vulnerability detection (CVE lookup)
* Report generation

---

## Basic Scanner

### Description

A simple port scanner using Python’s built-in `socket` module. It scans a given range of ports and prints all open ports on the target.

Ideal for beginners who want to:

* Understand TCP handshakes
* Learn how port scanners work from scratch

### Usage

```bash
cd basic/
python basic_scanner.py
```

* Enter the target IP/domain.
* Provide the port range (start & end).
* See the list of open ports.

### Requirements

* Python 3.x (tested with Python 3.6+)
* No external libraries needed

---

## Advanced Scanner

### Advanced Description

The advanced version elevates the scanner by using:

* `nmap` for detailed port & service scanning
* Public CVE databases for vulnerability detection
* `fpdf` for professional report generation

This tool suits intermediate to advanced users and demonstrates real-world vulnerability scanning practices.

### Features

* 🛠 Service & version detection via Nmap
* 🧠 Automatic CVE lookup (via Vulners API)
* 📝 Generates PDF reports with:

  * Scan summary
  * Detected services & vulnerabilities
  * OS info, uptime, and traceroute
  * CVSS-based risk scoring with color-coded severity
* 📊 Output in both terminal and PDF format

### Setup & Requirements

Install the dependencies:

```bash
pip install nmap requests fpdf
```

Install Nmap:

* **Linux (Ubuntu/Debian):**

  ```bash
  sudo apt-get install nmap
  ```
* **Windows:**
  Download from [https://nmap.org/download.html](https://nmap.org/download.html)

Ensure the `fonts/` folder exists in `advanced/` directory:

* Contains required fonts for PDF: `DejaVuSans.ttf`, `DejaVuSans-Bold.ttf`, `DejaVuSans-Oblique.ttf`

### Advanced Usage

```bash
cd advanced/
python scanner.py
```

* Enter target IP/domain
* Optional: Generate a PDF report

Scan results and CVEs are displayed in the terminal and saved to a PDF report.

---

## Folder Structure

```
vuln-hawk/
├── basic/
│   ├── info/
│   │   ├── .gitignore_info.txt
│   │   ├── basic_scanner_info.txt
│   ├── .gitignore
│   └── basic_scanner.py
├── advanced/
│   ├── scanner.py
│   ├── cve_lookup.py
│   ├── generate_report.py
│   ├── .gitignore
│   ├── README.md
│   ├── requirements.txt
│   ├── fonts/
│   │   ├── DejaVuSans.ttf
│   │   ├── DejaVuSans-Bold.ttf
│   │   └── DejaVuSans-Oblique.ttf
│   ├── info/
│   │   ├── .gitignore_info.txt
│   │   ├── cve_lookup_info.md
│   │   ├── generate_report_info.md
│   │   ├── requirements_info.md
│   │   ├── scanner_info.md
├── LICENSE
└── README.md
```

---

## Contributing

All contributions are welcome! You can:

* Report bugs or open issues
* Suggest new features
* Submit pull requests

Make sure your code is tested and well-documented before submitting.

---

## Feedback
Got a bug, feature request, or improvement idea?
👉 Open an issue or start a discussion on [GitHub Issues](https://github.com/tanujkumar2405/VulnHawk/issues)

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](https://github.com/tanujkumar2405/VulnHawk/blob/main/LICENSE) file for details.

---

## Author

Built and maintained by [Tanuj Kumar](https://www.linkedin.com/in/tanuj-kumar-cybersecurity). — Creator and Maintainer  
[GitHub](https://github.com/tanujkumar2405) | [LinkedIn](https://www.linkedin.com/in/tanuj-kumar-cybersecurity)  

  

If you find this project useful, please ⭐ the repository and share it with others.

---

## Happy Scanning

**Just a developer who loves breaking and fixing stuff**.  
— *Tanuj Kumar* 💻🔐


