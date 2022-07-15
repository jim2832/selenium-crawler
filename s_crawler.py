from selenium import webdriver
from selenium.webdriver.common.keys import Keys #可以針對鍵盤進行輸入
from selenium.webdriver.common.ny import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://www.dcard.tw/f") #前往指定的網頁

# print(driver.title) <- 印出標題
# driver.quit <- 關閉網頁

search = driver.find_element_by_name("query") #尋找input標籤
search.send_keys("教授") #搜尋文字
search.send_keys(Keys.RETURN) #enter動作

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )

titles = driver.find_elements_by_class_name("sc-417133b6-3")
for title in titles: 
    print(title.text)

time.sleep(5)
driver.quit()