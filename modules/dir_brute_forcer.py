import requests
from utils.report_writer import write_report

def run(target_url, wordlist_path, report_name):
    result = {
        "module": "Directory Brute Forcer",
        "target": target_url,
        "wordlist": wordlist_path,
        "found_paths": [],
        "status": None
    }

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            paths = f.read().splitlines()

        print(f"[+] Starting directory brute force on {target_url}")
        for path in paths:
            url = f"{target_url.rstrip('/')}/{path}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code in [200, 301, 302]:
                    print(f"[✓] Found: {url} (Status: {response.status_code})")
                    result["found_paths"].append({"url": url, "status": response.status_code})
                else:
                    print(f"[-] Not Found: {url} (Status: {response.status_code})")
            except Exception as e:
                print(f"[!] Error accessing {url}: {e}")

        result["status"] = "success" if result["found_paths"] else "no directories found"

    except Exception as e:
        result["status"] = "failed"
        result["error"] = str(e)
        print(f"[!] Error reading wordlist: {e}")

    write_report(result, report_name)
