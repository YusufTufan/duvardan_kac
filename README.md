# DUVARDAN KAÇ

## Oyun Tanıtımı

"DUVARDAN KAÇ", Python ve pygame kütüphanesi kullanılarak geliştirilen minimalist bir arcade oyunudur. Oyuncular, ekrandaki karakteri kontrol ederek rastgele oluşturulan duvar engelleri arasından geçmeye çalışırlar. Oyunun amacı, duvarlara çarpmadan mümkün olduğunca uzun süre hayatta kalmak ve yüksek skor elde etmektir.

## Oynanış
Oyun mekanikleri oldukça basittir:
- Oyun başladığında karakter otomatik olarak ilerler
- Ekrana dokunduğunuzda/tıkladığınızda karakter zıplar
- Duvarlar sağdan sola doğru hareket eder ve rastgele boşluklarla oluşturulur
- Her başarılı duvar geçişinde skor artar
- Duvara çarpıldığında oyun sona erer
- Zorluk seviyesi, oynadıkça ve skorunuz arttıkça yükselir


# Oyundan Görseller

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="https://raw.githubusercontent.com/YusufTufan/duvardan_kac/refs/heads/main/Assets/first.jpg" width="250"/>
  <img src="https://raw.githubusercontent.com/YusufTufan/duvardan_kac/refs/heads/main/Assets/oyun_ici.jpg" width="250"/>
  <img src="https://raw.githubusercontent.com/YusufTufan/duvardan_kac/refs/heads/main/Assets/oyun_sonu.jpg" width="250"/>
</div>

## Teknik Detaylar
### Kullanılan Teknolojiler
- Python 3.x
- Pygame kütüphanesi
- Nesne tabanlı programlama yaklaşımı

### Dosya Yapısı
- `main.py`: Oyunun ana döngüsü ve kontrollerin yönetildiği dosya
- `objects.py`: Oyun nesnelerinin (karakter, duvarlar, vb.) tanımlandığı ve çizim fonksiyonlarının bulunduğu dosya
- `Assets/`: Oyun görselleri, arkaplan ve sprite'lar
- `Fonts/`: Oyun içi metinlerde kullanılan yazı tipleri
- `Sounds/`: Oyun müzikleri ve ses efektleri

### Oyun Bileşenleri
1. **Karakter**: Oyuncunun kontrol ettiği küçük beyaz kare
2. **Duvarlar**: Rastgele yüksekliklerde oluşturulan engeller
3. **Skor Sistemi**: Geçilen her duvar için puan kazanma
4. **Arayüz**: Ana menü, oyun ekranı ve oyun sonu ekranı

## Kurulum ve Çalıştırma

```bash
# Repoyu klonlayın
git clone https://github.com/YusufTufan/DUVARDAN_KAC.git

# Proje dizinine gidin
cd DUVARDAN_KAC

# Gereksinimleri yükleyin
pip install pygame

# Oyunu başlatın
python main.py
```

## Gereksinimler
- Python 3.x
- Pygame

## İletişim ve Katkı
Bu projeye katkıda bulunmak isteyenler için pull request'ler açıktır. Oyun hakkında geri bildirim veya önerileriniz için GitHub üzerinden iletişime geçebilirsiniz.

**DUVARDAN KAÇ** - Minimal, bağımlılık yapıcı ve zorlu bir arcade deneyimi.
