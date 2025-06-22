import json
from fpdf import FPDF
import os
from datetime import datetime

def write_report(data, report_name):
    os.makedirs("reports", exist_ok=True)

    json_path = f"reports/{report_name}.json"
    pdf_path = f"reports/{report_name}.pdf"

    # JSON
    with open(json_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4) + ",\n")

    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Penetration Testing Report", ln=True, align="C")
    pdf.cell(200, 10, txt="Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ln=True, align="C")
    pdf.ln(10)

    for key, val in data.items():
        line = f"{key}: {val}"
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)
