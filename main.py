from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_text_by_xpath(xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text.strip()
    except:
        return "Bilinmiyor"

def scrape_car_data(url):
    driver.get(url)
    time.sleep(3)  # Sayfanın yüklenmesini bekle

    data = {}
    data['Fiyat'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div')
    data['İlan No'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]')
    data['İlan Tarihi'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]')
    data['Seri'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]')
    data['Model'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[5]')
    data['Yıl'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[6]')
    data['Km'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[7]')
    data['Vites Tipi'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[8]')
    data['Yakıt Tipi'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[9]')
    data['Motor Gücü'] = get_text_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[13]')

    return data

# Kullanıcıdan ilan sayısı ve linkleri al
urls = []
n = int(input("Kaç ilan karşılaştırmak istiyorsunuz? "))
for i in range(n):
    url = input(f"{i+1}. ilan linkini girin: ")
    urls.append(url)

# Her ilan için verileri çek
car_list = []
for url in urls:
    print(f"Veriler çekiliyor: {url}")
    car_data = scrape_car_data(url)
    car_list.append(car_data)

driver.quit()

# Verileri pandas DataFrame olarak göster
df = pd.DataFrame(car_list)
print("\nAraç Karşılaştırma Tablosu:\n")
print(df)
