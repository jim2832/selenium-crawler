from selenium import webdriver
from selenium.webdriver.common.keys import Keys #可以針對鍵盤進行輸入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget #可以在網路下載東西

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://www.instagram.com/")

#等待跳轉
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

#等待跳轉
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')

username.clear()
password.clear()

username.send_keys("jim880705") #輸入帳號
password.send_keys("ss580223") #輸入密碼
login.click() #按下登入按鈕

#等待跳轉
search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )

"""
ig有一個很特別的地方
若你要搜尋的時候
打完字要先停頓1秒
之後按下一次Enter
再停頓1秒
再按下一次Enter
才能順利搜尋
"""

keyword = "#台北美食"
search.send_keys(keyword) #將關鍵字輸入到搜尋欄
time.sleep(1)
search.send_keys(Keys.RETURN) #按下Enter
time.sleep(1)
search.send_keys(Keys.RETURN) #按下Enter

#下載圖片
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
    )

#滑動滾輪
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

#檔案路徑
path = os.path.join(keyword)
os.mkdir(path)

count = 0
imgs = driver.find_element_by_class_name("FFVAD")
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + ".jpg")
    #print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count+=1

time.sleep(5)
driver.quit()