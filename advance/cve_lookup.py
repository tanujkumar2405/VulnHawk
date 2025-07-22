# CVE stands for Common Vulnerabilities and Exposures.

import requests

API_KEY = "IBVH1ZP24TOFIZQ4RTEV8KWT06RPXHUPHMARHKQR34GEBD6ELKWEI76TRIQQTAB5"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Python VulnScanner",
    "X-Api-Key": API_KEY
}

def search_cve(service_name, version):
    query = f"{service_name} {version}".strip()
    url = "https://vulners.com/api/v3/search/lucene/"
    data = {
        "query": query,
        "apiKey": API_KEY
    }

    try:
        response = requests.post(url, json=data, headers=HEADERS)
        response.raise_for_status()
        results = response.json()

        cve_list = []
        if results.get("result") == "OK":
            for doc in results.get("data", {}).get("documents", []):
                if doc.get("type") == "cve":
                    cve_id = doc.get("id")
                    title = doc.get("title")
                    cvss = float(doc.get("cvss", 0))
                    cve_list.append({
                        "id": cve_id,
                        "title": title,
                        "cvss": cvss
                    })
        return cve_list[:5]  # limit to top 5 CVEs
    except Exception as e:
        return [{"id": "Error", "title": str(e), "cvss": 0}]
