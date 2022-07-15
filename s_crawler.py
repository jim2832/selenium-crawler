from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://www.dcard.tw/f") #前往指定的網頁

# print(driver.title) <- 印出標題
# driver.quit <- 關閉網頁

search = driver.find_element(by = "query", value= None) #尋找input標籤
search.send_keys("教授") #搜尋文字
search.send_keys(Keys.RETURN) #enter動作

# titles = driver.find_elements_by_class_name("tgn9uw-3")
# for title in titles: 
#     print(title.text)

time.sleep(5)
driver.quit()