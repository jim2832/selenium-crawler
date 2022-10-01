from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #可以針對鍵盤進行輸入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/usr/local/bin/chromedriver2"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("http://www.course.acad.nsysu.edu.tw/tasystem/login.php") #前往指定的網頁

#等到出現公告之後才開始之後的動作
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME , "textBox"))
#     )

#關閉警示視窗
time.sleep(1)
actions =  ActionChains(driver) #創建物件
actions.move_by_offset(0.5, 0.5)
actions.click()
actions.click()
actions.perform()

time.sleep(1)

#登入
id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "id"))
    )

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

login = driver.find_element_by_xpath('/html/body/article/section/div/form/div[2]/input')

id.clear()
password.clear()

id.send_keys("B123257723") #輸入帳號
password.send_keys("257723") #輸入密碼
login.click() #按下登入按鈕

#選取課程
course = driver.find_element_by_xpath('/html/body/main/aside/nav/ul/li[3]/a')
course.click()
time.sleep(2)
Keys.RETURN

#處理彈出式視窗
prompt = driver.switch_to.alert
prompt.accept()

#開始上課
start_class = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH , '//*[@id="ta002"]'))
    )
start_class.click()