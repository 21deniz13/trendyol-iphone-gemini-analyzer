import sqlite3

baglanti=sqlite3.connect("trendyol_iphone.db")
vt=baglanti.cursor()
try:
    vt.execute("Select id,model,urun_adi,fiyat,tarih From fiyatlar")
    kayitlar=vt.fetchall()

    if not kayitlar:
        print("Veritabanında kayıtlı ürün bulunamadı. Lütfen önce veri kazıma işlemini çalıştırın.")
    else:
        for kayit in kayitlar:
          kayit_id=kayit[0]
          model=kayit[1]
          urun_adi=kayit[2]
          fiyat=kayit[3]
          tarih=kayit[4]

          print(f"[{kayit_id}] {tarih} | {model} -> {urun_adi} : {fiyat}")

except sqlite3.OperationalError:
    print(
        "Veritabanında kayıtlı ürün bulunamadı. "
        "Lütfen önce veri kazıma işlemini çalıştırın."
    )

finally:
    baglanti.close()