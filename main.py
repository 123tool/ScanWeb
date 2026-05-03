import os
import datetime
from core.logger import banner, log_info, log_warn
from core.scanner import check_security_headers
from core.discovery import scan_paths
from core.subdomain import discover_subdomains

def save_report(target, data):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"reports/SPYE_Report_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"--- SPY-E SECURITY AUDIT REPORT ---\n")
        f.write(f"Target    : {target}\n")
        f.write(f"Timestamp : {datetime.datetime.now()}\n")
        f.write("="*40 + "\n\n")
        f.write(data)
    print("\n" + "="*40)
    log_info(f"LAPORAN PRO SELESAI: {filename}")

def main():
    banner()
    target = input("Masukkan URL Target (contoh: https://target.com): ")
    if not target.startswith("http"):
        log_warn("Gunakan format URL yang benar (http/https)!")
        return

    full_report_data = ""

    # TAHAP 1: Security Headers
    log_info("Memulai Tahap 1: Header Analysis...")
    h_results = check_security_headers(target)
    full_report_data += "1. SECURITY HEADERS ANALYSIS\n" + "\n".join(h_results) + "\n\n"

    # TAHAP 2: Subdomain Discovery
    log_info("Memulai Tahap 2: Subdomain Discovery...")
    sub_file = "data/subdomains.txt"
    if os.path.exists(sub_file):
        with open(sub_file, "r") as f:
            subs = f.readlines()
        s_results = discover_subdomains(target, subs)
        full_report_data += "2. SUBDOMAIN DISCOVERY\n" + ("\n".join(s_results) if s_results else "No subdomains found.") + "\n\n"

    # TAHAP 3: Path Discovery
    log_info("Memulai Tahap 3: Path & File Discovery...")
    path_file = "data/paths.txt"
    if os.path.exists(path_file):
        with open(path_file, "r") as f:
            paths = f.readlines()
        p_results = scan_paths(target, paths)
        full_report_data += "3. PATH DISCOVERY\n" + ("\n".join(p_results) if p_results else "No sensitive paths found.") + "\n\n"

    # Simpan Semua Hasil
    save_report(target, full_report_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Program dihentikan paksa.")
