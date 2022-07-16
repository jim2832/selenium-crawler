from selenium import webdriver
from selenium.webdriver.common.keys import Keys #可以針對鍵盤進行輸入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://www.dcard.tw/f") #前往指定的網頁

# print(driver.title) <- 印出標題

search = driver.find_element_by_name("query") #尋找input標籤
search.clear() #先清空搜尋內容(以防有預設文字)
search.send_keys("教授") #搜尋文字
search.send_keys(Keys.RETURN) #enter動作

#等到出現「看板」文字之後才開始之後的動作
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME , "sc-f860e6e9-1"))
    )

#標題
titles = driver.find_elements_by_class_name("sc-417133b6-3")
for title in titles: 
    print(title.text)

link = driver.find_element_by_link_text("#請益 教授推薦信") #找到某篇文章
link.click() #執行點擊動作
time.sleep(3)
driver.back() #回到上一頁
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward() #下一頁
time.sleep(3)

time.sleep(5)
driver.quit() #關閉網頁