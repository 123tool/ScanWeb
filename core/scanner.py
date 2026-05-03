import requests
from core.logger import log_success, log_warn

def check_security_headers(url):
    results = []
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        checks = ['X-Frame-Options', 'Content-Security-Policy', 'X-Content-Type-Options']
        for header in checks:
            if header in headers:
                msg = f"{header} ditemukan: {headers[header]}"
                log_success(msg)
                results.append(msg)
            else:
                msg = f"MISSING: {header} tidak ditemukan!"
                log_warn(msg)
                results.append(msg)
        return results
    except:
        return ["Gagal melakukan koneksi untuk check headers."]
