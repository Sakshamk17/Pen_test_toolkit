# 🛡️ Penetration Testing Toolkit

COMPANY: CODTECH IT SOLUTION

NAME: SAKSHAM VIJAY KHOBRAGADE

INTERN ID: CT04DG2805

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

A powerful modular Python-based toolkit designed for penetration testers and cybersecurity learners. This toolkit automates various reconnaissance and exploitation tasks including banner grabbing, port scanning, SSH brute forcing, directory brute forcing, and custom login brute forcing.

---

## 📁 Features

- 🔎 **Banner Grabber** – Grab service banners from open ports
- 🚪 **Port Scanner** – Scan open ports in a given range on a target
- 🔐 **SSH Brute Forcer** – Attempt SSH login using a username and password wordlist
- 📂 **Directory Brute Forcer** – Discover hidden directories on a web server
- 🔐 **Custom Brute Forcer** – Automate brute force attacks on login forms using POST requests
- 📄 **PDF & JSON Reports** – Automatically generated reports for every module

---

## 🛠️ Modules Breakdown

### 1. **Banner Grabber**
Grabs and prints the service banner of a specified port.

**Usage:**
Enter target IP or domain: 93.184.216.34
Enter port number: 80

---

### 2. **Port Scanner**
Scans a range of ports to find which ones are open on the target host.

**Usage:**
Enter target IP or domain: scanme.nmap.org
Enter start port: 20
Enter end port: 100

---

### 3. **SSH Brute Forcer**
Performs brute-force attacks on SSH servers using a username and password wordlist.

**Usage:**
Enter SSH server IP: 192.168.1.10
Enter SSH username: root
Enter password wordlist path: wordlists/passwords.txt

---

### 4. **Directory Brute Forcer**
Discovers hidden directories on a website using a wordlist.

**Usage:**
Enter target URL (e.g., http://example.com/): http://testphp.vulnweb.com/
Enter directory wordlist path [default: wordlists/common_dirs.txt]:

---

### 5. **Custom Brute Forcer**
Attempts brute-force login on websites with custom form fields.

**Usage:**
Enter target login URL: http://example.com/login.php
Enter username field name (e.g., 'uname'): username
Enter password field name (e.g., 'pass'): password
Enter username: admin
Enter password wordlist path: wordlists/passwords.txt


---

## 📁 Project Structure

pen_test_toolkit/
├── main.py
├── modules/
│ ├── banner_grabber.py
│ ├── port_scanner.py
│ ├── ssh_brute_forcer.py
│ ├── dir_brute_forcer.py
│ └── brute_forcer.py
├── utils/
│ ├── report_writer.py
│ └── report_generator.py
├── wordlists/
│ ├── common_dirs.txt
│ └── passwords.txt
├── reports/
│ ├── *.pdf
│ └── *.json


---

## 📝 Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `paramiko`
  - `fpdf`
  - `beautifulsoup4` (optional)

**Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚠️ Disclaimer

This toolkit is intended strictly for educational and authorized testing purposes. Unauthorized use against systems you do not own or have permission to test is illegal and unethical.

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or add.

## Outputs

![Image](https://github.com/user-attachments/assets/6659103b-74c1-4ad8-a976-8aada06e7d81)

![Image](https://github.com/user-attachments/assets/2af8053b-820e-4d80-b44c-6d2079d92390)

![Image](https://github.com/user-attachments/assets/f03b6f70-c46c-4a47-953b-b091ee5c2d52)

![Image](https://github.com/user-attachments/assets/3fffc22a-7b71-4fb9-af15-338ac981f2d9)

![Image](https://github.com/user-attachments/assets/40902c91-bc87-471c-8393-8f67410f7179)
