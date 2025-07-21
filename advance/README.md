# Advanced Vulnerability Scanner

This is the advanced version of the Python Vulnerability Scanner project.

---

## Features

- Detailed port scanning using **nmap**
- Service version detection
- CVE (Common Vulnerabilities and Exposures) lookup via Vulners API
- PDF report generation with scan results and risk levels
- OS and uptime detection
- Network traceroute analysis
- Color-coded risk assessment based on CVSS scores

---

## Setup & Requirements

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. 2. Install nmap tool

- On Ubuntu/Debian:

```bash
    sudo apt-get install nmap
```
- On Windows, download from https://nmap.org/download.html and install.

### 3. Fonts
Make sure the *fonts/* folder with DejaVu font files exists in this directory, required for PDF reports.


---


## Usage

Run the main scanner script:

```bash
    python scanner.py
```
You will be prompted to enter the target IP/domain.

After scanning, you will be asked whether to generate a PDF report.


---


## Files Description

- *scanner.py*: Main scanner that uses nmap and performs CVE lookups.

- *cve_lookup.py*: Queries Vulners API to search for CVEs by service name and version.

- *generate_report.py*: Generates a detailed PDF report with scan results.

- *fonts/*: Contains DejaVu font files required for PDF report formatting.


---


## Notes

- An active internet connection is required for CVE lookups.

- You can customize or extend the scripts as needed.

- Make sure your firewall or antivirus allows nmap scans.


---


## Contact

For issues or questions, please open an issue in the main repository.

Happy scanning! 🔍


---


## 2. `requirements.txt` file for **advanced/** folder

### How to use:

1. Place the `requirements.txt` inside your `advanced/` folder.

2. Run:

```bash
    pip install -r advanced/requirements.txt
```