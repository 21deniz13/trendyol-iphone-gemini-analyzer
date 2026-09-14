import sqlite3
from ai_analiz import fiyat_farki_analizi

baglanti=sqlite3.connect("trendyol_iphone.db")
vt=baglanti.cursor()

try:
    vt.execute("SELECT model,urun_adi,fiyat,tarih FROM fiyatlar")
    kayitlar=vt.fetchall()
finally:
    baglanti.close()

if not kayitlar:
    print(
        "Veritabanında analiz edilecek ürün bulunamadı. Lütfen önce veri kazıma betiğini çalıştırın."
    )
    exit()

def fiyata_cevir(kayit):
   try:
       fiyat_str=kayit[2]
       fiyat_str=fiyat_str.replace("TL","").replace(" ","").strip()

       if "," in fiyat_str:
           fiyat_str=fiyat_str.split(",")[0]

       temiz_sayi=fiyat_str.replace(".","")
       return float(temiz_sayi)
   except Exception:
       return 0.0

en_ucuz=min(kayitlar,key=fiyata_cevir)
en_pahali=max(kayitlar,key=fiyata_cevir)

print(f"EN UCUZ: {en_ucuz[1]} -> {en_ucuz[2]}")
print(f"EN PAHALI: {en_pahali[1]} -> {en_pahali[2]}")

ucuz_urun_bilgisi = f"{en_ucuz[0]} - {en_ucuz[1]} ({en_ucuz[2]})"
pahali_urun_bilgisi = f"{en_pahali[0]} - {en_pahali[1]} ({en_pahali[2]})"

ai_raporu = fiyat_farki_analizi(
    en_ucuz_urun=ucuz_urun_bilgisi,
    en_pahali_urun=pahali_urun_bilgisi,
    ucuz_yorumlar="Kullanıcılar fiyatının uygun olmasını övüyor ancak teslimat süresinden şikayetçi.",
    pahali_yorumlar="Kullanıcılar ürün kalitesinden ve performansından çok memnun fakat fiyatı yüksek buluyor."
)

print("\n--- YAPAY ZEKA DEĞERLENDİRME RAPORU ---")
print(ai_raporu)