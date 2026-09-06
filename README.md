# tkinter_not_degerlendirme
Python Tkinter ile geliştirilmiş, girilen sınav puanına göre başarı durumunu (Kaldı/Geçti/Başarılı) gösteren basit masaüstü GUI uygulaması.

## 📌 Özellikler
- **Not Analizi:** Girilen puana göre dinamik renklerle (Kırmızı / Mavi / Yeşil) durum mesajı gösterir.
- **Girdi Kontrolü & Hata Yönetimi:** Harf/boş girişlerde `messagebox` ile uyarı verir; 0-100 dışındaki mantıksız değerleri engeller.

## 🛠️ Kullanılan Konular ve Teknolojiler
Bu projede pekiştirilen temel Python ve Arayüz (GUI) kavramları:

- **Python Temelleri:**
  - `if - elif - else` koşullu durum yapıları ve aralık kontrolleri
  - `try - except` (ValueError) ile istisna yönetimi
  - Tip dönüşümleri (`str` -> `int`)

- **Tkinter GUI Geliştirme:**
  - `Tk` ile ana pencere düzenleme (`geometry`, `resizable`)
  - Arayüz elemanlarının kullanımı (`Label`, `Entry`, `Button`)
  - `place()` geometrik düzenleyicisi ile eleman konumlandırma
  - `configure()` ile dinamik etiket ve renk güncellemeleri
  - `messagebox` ile uyarı penceresi kullanımı
