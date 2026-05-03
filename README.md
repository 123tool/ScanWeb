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
```
### 2. Clone
```
git clone https://github.com/123tool/ScanWeb.git
cd ScanWeb
```
### 3. Dependency
```
pip install -r requirements.txt
```
### 4. Jalankan
```
python main.py
```
**Contoh Input :**
​Target URL : 
```
https://website-kamu.com
```
​Setelah proses selesai, silakan cek folder reports/ untuk melihat detail laporan audit keamanan dalam format .txt.

## Disclaimer

**​Tool ini dibuat murni untuk tujuan edukasi dan keamanan legal (White Hat). Segala bentuk penyalahgunaan tool ini untuk merusak atau mengakses sistem tanpa izin adalah tanggung jawab penuh pengguna. Selalu pastikan kamu memiliki izin sebelum melakukan audit keamanan pada sistem pihak ketiga**
