# Vulnerability Scanner Project

Welcome to the **Vulnerability Scanner Project**!  
This repository contains two versions of a Python-based vulnerability scanner:

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Basic Version](#basic-version)  
  - [Description](#basic-description)  
  - [Usage](#basic-usage)  
  - [Requirements](#basic-requirements)  
- [Advanced Version](#advanced-version)  
  - [Description](#advanced-description)  
  - [Features](#advanced-features)  
  - [Setup & Requirements](#advanced-setup--requirements)  
  - [Usage](#advanced-usage)  
- [Folder Structure](#folder-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

This project is designed to help beginners and enthusiasts learn about network scanning and vulnerability detection using Python.

- The **Basic Version** is a simple port scanner that scans a range of ports on a target host to identify which ports are open.
- The **Advanced Version** is a more sophisticated tool that uses nmap for detailed scanning, queries public CVE databases to find vulnerabilities, and generates PDF reports with findings.

---

## Basic Version


### Basic Description

The basic scanner uses Python’s built-in `socket` module to attempt TCP connections on a specified range of ports on a target IP or domain. It prints all open ports found during the scan.

This is perfect for beginners who want to understand how port scanning works in Python.


### Basic Usage

1. Navigate to the `basic/` folder:

```bash
   cd basic/
```
2. Run the scanner script:

```bash
    python basic_scanner.py
```

3. Enter the target IP or domain when prompted.

4. Enter the starting and ending port numbers for the scan.

The scanner will print all open ports it finds.


### Basic Requirements

- Python 3.x (tested on Python 3.6+)

- No additional external libraries needed.


---


## Advanced Version


### Advanced Description

The advanced scanner combines several tools and techniques to provide a detailed security assessment:

- Uses *nmap* for comprehensive port scanning and service detection.

- Queries the Vulners API for known CVEs (Common Vulnerabilities and Exposures) related to detected services.

- Generates a professional PDF report summarizing scan results and detected vulnerabilities.

- Includes OS detection, uptime, traceroute information, and CVSS-based risk scoring.

This version is aimed at intermediate to advanced users familiar with Python and security concepts.


### Advanced Features

- Service detection and version scanning using nmap.

- Automatic CVE lookup via Vulners API for detected software.

- PDF report generation with detailed scan data and vulnerability risk assessment.

- System information extraction including OS details and uptime.

- Network traceroute hops displayed for the scanned host.

- Color-coded risk levels in the report based on CVSS scores.


### Advanced Setup & Requirements

Before running the advanced scanner, install the following dependencies:

1. **Python libraries:**

```bash
    pip install nmap requests fpdf
```

2. **Nmap tool:**

Make sure *nmap* is installed on your system and available in your PATH.

- **Ubuntu/Debian:**

```bash
    sudo apt-get install nmap
```

- **Windows:**

Download and install from https://nmap.org/download.html

3. **Fonts folder:**
The *fonts/* directory contains DejaVu fonts required for PDF report generation. Make sure it exists inside *advanced/* folder.


### Advanced Usage

1. Navigate to the *advanced/* folder:

```bash
    cd advanced/
```
2. Run the scanner:

```bash
    python scanner.py
```

3. Enter the target IP or domain when prompted.

4. After scanning, choose whether to generate a PDF report.

The scan results and detected CVEs will be displayed in the console and optionally saved as a PDF in the current folder.


---


## Folder Structure

```bash
    vulnerability-scanner/
    ├── basic/
    │   └── basic_scanner.py               # Basic port scanner script
    ├── advanced/
    │   ├── cve_lookup.py                  # CVE lookup via Vulners API
    │   ├── generate_report.py             # PDF report generator
    │   ├── scanner.py                    # Main advanced scanner with nmap
    │   ├── fonts/                        # Required fonts for PDF reports
    │   │    ├── DejaVuSans.ttf
    │   │    ├── DejaVuSans-Bold.ttf
    │   │    └── DejaVuSans-Oblique.ttf
    ├── README.md                         # This file
```


---


## Contributing

Contributions are welcome! You can:

- Report bugs or issues

- Suggest new features

- Submit pull requests with improvements

Please make sure to test your changes and update documentation accordingly.


---


## License

This project is open source and available under the *[MIT License](https://github.com/tanujkumar2405/VulnHawk/blob/main/LICENSE)*.


**If you have any questions or need help running the scanners, feel free to open an issue or contact me.**

***Happy scanning! 🔍🔐***

