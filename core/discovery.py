import requests
from core.logger import log_success, log_warn

def scan_paths(target_url, path_list):
    found_paths = []
    if not target_url.endswith("/"):
        target_url += "/"

    for path in path_list:
        path = path.strip()
        if not path: continue
        
        full_url = f"{target_url}{path}"
        try:
            # Menggunakan allow_redirects=False agar tidak terkecoh redirect login
            response = requests.get(full_url, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                msg = f"[200 OK] {full_url}"
                log_success(msg)
                found_paths.append(msg)
            elif response.status_code == 403:
                msg = f"[403 Forbidden] {full_url}"
                log_warn(msg)
                found_paths.append(msg)
        except:
            pass
    return found_paths
