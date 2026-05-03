## 🛡️ ScanWeb Pro

Tool audit keamanan otomatis yang dirancang untuk keperluan *Digital Forensics* dan *Cybersecurity Research*. Tool ini membantu developer dan praktisi keamanan untuk mendeteksi celah konfigurasi pada server, mencari subdomain yang aktif, serta menemukan file atau direktori sensitif yang terbuka untuk publik.

---

## 🚀 Fitur
*   **Header Security Audit**: Menganalisis proteksi HTTP Header (X-Frame, CSP, dll) untuk mencegah serangan seperti Clickjacking
*   **Subdomain Hunter**: Melakukan pemindaian otomatis terhadap subdomain yang mungkin tidak terproteksi
*   **Path & File Discovery**: Mencari file sensitif seperti `.env`, `.git`, atau folder backup secara otomatis
*   **Auto-Save Report**: Setiap hasil pemindaian akan otomatis tersimpan dalam folder `reports/` dengan timestamp yang rapi
*   **Cross-Platform**: Berjalan lancar di **Xubuntu (Linux)**, **Termux (Android)**, **Ubuntu**, maupun **CMD (Windows)**

---

## 🛠️ Instalasi

### 1. Persiapan Lingkungan
Pastikan kamu sudah menginstal Python 3.x di perangkatmu

**Linux/Ubuntu/Xubuntu :**
```bash
sudo apt update && sudo apt install python3 python3-pip -y
```
**Termux :**
```
pkg update && pkg install python -y
