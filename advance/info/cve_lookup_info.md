# 🔍 CVE Lookup Module Documentation (`cve_lookup.py`)

## 📄 Overview

The `cve_lookup.py` module provides functionality to search for recent Common Vulnerabilities and Exposures (CVEs) related to a specific service and version using the Vulners API. This enables security tools to fetch vulnerability data in real-time and integrate risk scoring into their analysis.


---


## 🧠 What is a CVE?

CVE stands for Common Vulnerabilities and Exposures. It is a publicly available list of known security vulnerabilities maintained by MITRE. Each CVE entry contains an identifier (e.g., `CVE-2023-12345`), a short description, and a severity score (CVSS).


---


## ⚙️ How It Works

The script:

1. Sends a POST request to Vulners' Lucene search API.

2. Searches for documents tagged as CVEs.

3. Filters and extracts the most relevant results.

4. Returns a list of CVEs (up to 5) including:

    - `CVE ID`

    - `Title`

    - `CVSS Score`


---


## 📦 Dependencies

- `[requests](https://pypi.org/project/requests/)` – For sending HTTP requests.

```bash
pip install requests
```


---


## 🛠️ Usage Example

```python
from cve_lookup import search_cve

service = "apache"
version = "2.4.54"

cves = search_cve(service, version)
for cve in cves:
    print(f"{cve['id']} - {cve['title']} (CVSS: {cve['cvss']})")
```


---


## 🧪 Sample Output

```less
CVE-2023-12345 - Apache vulnerability XYZ (CVSS: 7.8)
CVE-2023-67890 - DoS via malformed header (CVSS: 6.5)
...
```


---


## 🔐 API Key
This script requires a Vulners API Key. You can obtain one by signing up at:

👉 https://vulners.com/

Set it in the script like:
```python
API_KEY = "YOUR_API_KEY_HERE"
```


---


## 🚨 Error Handling

In case of an API error or exception, a dummy CVE with `"Error"` as ID will be returned:

```python
[{"id": "Error", "title": "Network or API error details", "cvss": 0}]
```


---


## 🧠 Ideal For

- Vulnerability scanners

- Penetration testing tools

- Cybersecurity automation projects

- CVSS scoring integrations     


---


### 📘 Maintained by **Tanuj Kumar** – for educational and cybersecurity exploration purposes.


---
