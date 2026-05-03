# 🛡️ SPY-E Security Scanner Pro
**SPY-E Security Scanner** adalah tool audit keamanan otomatis yang dirancang untuk keperluan *Digital Forensics* dan *Cybersecurity Research*[span_1](start_span)[span_1](end_span). Tool ini membantu developer dan praktisi keamanan untuk mendeteksi celah konfigurasi pada server, mencari subdomain yang aktif, serta menemukan file atau direktori sensitif yang terbuka untuk publik[span_2](start_span)[span_2](end_span).

---

## 🚀 Fitur Utama
*   **Header Security Audit**: Menganalisis proteksi HTTP Header (X-Frame, CSP, dll) untuk mencegah serangan seperti Clickjacking[span_3](start_span)[span_3](end_span).
*   **Subdomain Hunter**: Melakukan pemindaian otomatis terhadap subdomain yang mungkin tidak terproteksi[span_4](start_span)[span_4](end_span).
*   **Path & File Discovery**: Mencari file sensitif seperti `.env`, `.git`, atau folder backup secara otomatis[span_5](start_span)[span_5](end_span).
*   **Auto-Save Report**: Setiap hasil pemindaian akan otomatis tersimpan dalam folder `reports/` dengan timestamp yang rapi[span_6](start_span)[span_6](end_span).
*   **Cross-Platform**: Berjalan lancar di **Xubuntu (Linux)**, **Termux (Android)**, **Ubuntu**, maupun **CMD (Windows)**[span_7](start_span)[span_7](end_span).

---

## 🛠️ Instalasi

### 1. Persiapan Lingkungan
Pastikan kamu sudah menginstal Python 3.x di perangkatmu[span_8](start_span)[span_8](end_span).

**Untuk Linux/Ubuntu/Xubuntu:**
```bash
sudo apt update && sudo apt install python3 python3-pip -y
