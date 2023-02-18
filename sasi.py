import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import keyboard

while True:
    # Kullanıcıdan şasi numarasını al
    shasi_numarasi = input("Lütfen şasi numarasını girin: ")

    # Options ayarları yapma
    options = Options()
    options.headless = True

    # Driver yolu giris
    driver = webdriver.Edge('msedgedriver.exe', options=options)

    # Site giris
    driver.get("https://www.sasisorgulama.com/")

    # Şasi numarası girme
    kod = driver.find_element(By.NAME, "kod")
    kod.click()
    kod0 = driver.find_element(By.NAME, "kod") 
    kod0.send_keys(shasi_numarasi)
    time.sleep(2)
    check = driver.find_element(By.NAME, "sorgula")
    check.click()

    # Sonuç bilgisini yazdırma
    try:
        yazdır = driver.find_element(By.CLASS_NAME, "dbar").text
        print(yazdır)
        with open('sonuç.txt', 'w') as f:
            f.write(yazdır)
    except:
        print("Hatalı şase numarası girdiniz.")

    # Tarayıcıyı kapat
    driver.quit()

    # Klavyeden q tuşuna basıldığında programı sonlandırma
    if keyboard.is_pressed('q'):
        break

