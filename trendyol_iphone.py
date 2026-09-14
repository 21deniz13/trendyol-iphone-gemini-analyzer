from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
from datetime import datetime
import time

tarih_bilgisi=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

baglanti=sqlite3.connect("trendyol_iphone.db")

vt=baglanti.cursor()

vt.execute("""CREATE TABLE IF NOT EXISTS fiyatlar(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 model TEXT,
                 urun_adi TEXT,
                 fiyat TEXT,
                 tarih TEXT)""")

options=Options()
options.add_argument('--headless')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


driver=webdriver.Edge(options=options)

url="https://www.trendyol.com/sr?lc=164462&qt=iphone%2013&st=iphone%2013&os=1&q=iphone%2013%20pro"
driver.get(url)

try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"product-card")))

    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)

    kartlar = driver.find_elements(By.CLASS_NAME, "product-card")

    for kart in kartlar:
       try:
          isim=kart.find_element(By.CLASS_NAME,"title").text

          fiyat=kart.find_element(By.CLASS_NAME,"price-section").text
          fiyat_temiz = fiyat.replace("\n", " ").strip()
          isim_lower = isim.lower()

          if (
                  "kılıf" in isim_lower
                  or "cam" in isim_lower
                  or "koruyucu" in isim_lower
                  or "kordon" in isim_lower
                  or "sarj" in isim_lower
                  or "şarj" in isim_lower
          ):
              continue

          tespit_edilen_model = "iPhone"
          for m in ["16", "15", "14", "13", "12", "11"]:
              if f"iphone {m}" in isim_lower:
                  tespit_edilen_model = f"iPhone {m}"
                  break

          vt.execute(
              """INSERT INTO fiyatlar(model, urun_adi, fiyat, tarih)
                           VALUES(?,?,?,?)""",
              (tespit_edilen_model, isim, fiyat, tarih_bilgisi),
          )
          print(f"Veri tabanina kaydedildi: {isim } - {fiyat_temiz}")

       except Exception as e:
         continue

    baglanti.commit()
finally:
    baglanti.close()
    driver.quit()

