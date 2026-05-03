import os
import datetime
from core.logger import banner, log_info
from core.scanner import check_security_headers
from core.discovery import scan_paths
from core.subdomain import discover_subdomains

def save_report(target, data):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    filename = f"reports/scan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"SPY-E SCAN REPORT\nTarget: {target}\n" + "="*30 + "\n\n")
        f.write(data)
    log_info(f"Laporan tersimpan di: {filename}")

def main():
    banner()
    target = input("Masukkan URL Target (https://example.com): ")
    if not target.startswith("http"):
        print("URL Salah!")
        return

    report_content = ""
    
    log_info("Memulai Audit...")
    
    # 1. Check Headers
    header_res = check_security_headers(target)
    report_content += "--- Security Headers ---\n" + "\n".join(header_res) + "\n\n"

    # 2. Path Discovery (Logika di modul discovery.py)
    # ... proses scanning ...
    
    save_report(target, report_content)

if __name__ == "__main__":
    main()
