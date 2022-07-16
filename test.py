from selenium import webdriver
from selenium.webdriver.common.keys import Keys #可以針對鍵盤進行輸入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #操作下拉式選單
import time

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://www.thsrc.com.tw/") #前往指定的網頁

#同意個資隱私政策
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME , "GDtitle"))
    )
confirm = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]')
confirm.click()

#選取起始和終點站
start_station = Select(driver.find_element_by_id("select_location01")) #起始站
start_station.select_by_index(1) #選取台北站

end_station = Select(driver.find_element_by_id("select_location02")) #終點站
end_station.select_by_index(6) #選取台中站

"""
#選取去程日期和時間
date1 = driver.find_element_by_id("Departdate01")
date1.click()
"""

search = driver.find_element_by_xpath('//*[@id="start-search"]')
search.click()