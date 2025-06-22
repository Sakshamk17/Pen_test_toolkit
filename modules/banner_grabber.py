import socket
from utils.report_writer import write_report

def run(target, port, report_name):
    result = {
        "module": "Banner Grabber",
        "target": target,
        "port": port,
        "banner": None,
        "status": None
    }

    try:
        with socket.socket() as s:
            s.settimeout(5)
            s.connect((target, port))
            banner = s.recv(1024).decode().strip()
            result["banner"] = banner
            result["status"] = "success"
            print(f"[+] Banner from {target}:{port} -> {banner}")

    except Exception as e:
        result["status"] = "failed"
        result["error"] = str(e)
        print(f"[!] Could not grab banner: {e}")

    write_report(result, report_name)
