import socket
from utils.report_writer import write_report

def run(target, start_port, end_port, report_name):
    result = {
        "module": "Port Scanner",
        "target": target,
        "start_port": start_port,
        "end_port": end_port,
        "open_ports": [],
        "status": None
    }

    print(f"\n[*] Scanning {target} from port {start_port} to {end_port}...")

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            try:
                s.connect((target, port))
                print(f"[+] Port {port} is open")
                result["open_ports"].append(port)
            except:
                pass
            finally:
                s.close()

        result["status"] = "success"
    except Exception as e:
        result["status"] = "failed"
        result["error"] = str(e)
        print(f"[!] Error during scanning: {e}")

    write_report(result, report_name)
