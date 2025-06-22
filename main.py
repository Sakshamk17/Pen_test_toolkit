import os
from modules import banner_grabber, port_scanner, ssh_brute_forcer, dir_brute_forcer, brute_forcer

def print_banner():
    banner = r"""
  ____            _       _             _______          _ _    _ _
 |  _ \ ___  _ __| |_ ___| |__   ___   |__   __|        | | |  (_) |
 | |_) / _ \| '__| __/ __| '_ \ / _ \     | | ___   ___ | | | ___| |_
 |  __/ (_) | |  | || (__| | | |  __/     | |/ _ \ / _ \| | |/ / | __|
 |_|   \___/|_|   \__\___|_| |_|\___|     | | (_) | (_) | |   <| | |_
                                        |_|\___/ \___/|_|_|\_\_|\__|
        Python-Based Penetration Testing Toolkit
    """
    print(banner)

def main():
    print_banner()
    report_name = input("Enter report name (without extension): ")

    while True:
        print("\nSelect a module to run:")
        print("1. Banner Grabber")
        print("2. Port Scanner")
        print("3. SSH Brute Forcer")
        print("4. Directory Brute Forcer")
        print("5. Custom Brute Forcer")
        print("0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            target = input("Enter target IP or domain: ")
            port = int(input("Enter port number: "))
            banner_grabber.run(target, port, report_name)

        elif choice == "2":
            target = input("Enter target IP or domain: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            port_scanner.run(target, start_port, end_port, report_name)

        elif choice == "3":
            host = input("Enter SSH server IP: ")
            username = input("Enter SSH username: ")
            wordlist = input("Enter password wordlist path: ")
            ssh_brute_forcer.run(host, username, wordlist, report_name)

        elif choice == "4":
            target_url = input("Enter target URL (e.g., http://example.com/): ")
            wordlist = input("Enter directory wordlist path [default: wordlists/common_dirs.txt]: ") or "wordlists/common_dirs.txt"
            dir_brute_forcer.run(target_url, wordlist, report_name)

        elif choice == "5":
            target_url = input("Enter target login URL: ")
            user_field = input("Enter username field name (e.g., 'uname'): ")
            pass_field = input("Enter password field name (e.g., 'pass'): ")
            username = input("Enter username: ")
            wordlist_path = input("Enter password wordlist path: ")
            brute_forcer.run(target_url, user_field, pass_field, username, wordlist_path, report_name)

        elif choice == "0":
            print("Exiting toolkit.")
            break
        else:
            print("[!] Invalid choice. Please select from 0 to 5.")

if __name__ == "__main__":
    main()
