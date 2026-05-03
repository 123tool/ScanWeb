import requests
from core.logger import log_success

def discover_subdomains(domain, sub_list):
    found_subs = []
    # Bersihkan protokol jika ada
    clean_domain = domain.replace("https://", "").replace("http://", "").split('/')[0]

    for sub in sub_list:
        sub = sub.strip()
        if not sub: continue
        
        target_sub = f"http://{sub}.{clean_domain}"
        try:
            # Timeout pendek agar scanning tetap cepat
            response = requests.get(target_sub, timeout=3)
            if response.status_code == 200:
                msg = f"[ACTIVE] {target_sub}"
                log_success(msg)
                found_subs.append(msg)
        except:
            pass
    return found_subs
