# action chain -> 自動完成網頁上的動作

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/usr/local/bin/chromedriver2"

driver = webdriver.Chrome(PATH) #使用chrome作為瀏覽器
driver.get("https://tsj.tw/") #取得網址

blow = driver.find_element_by_id("click") #按鈕標籤
blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]') #因為裡面有雙引號，所以外層的要改成單引號

buttons = [] #建立空列表
buttons.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
buttons.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
buttons.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))

prices = []
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

#執行動作
actions =  ActionChains(driver) #創建物件

while(1):
    actions.click(blow)
    actions.perform() #要加perform才能確實完成動作
    count = int(blow_count.text.replace("您目前擁有", "").replace("技術點", "")) #把多餘的字串去掉，並轉為int，才能跟花費點數做比較
    for j in range(3):
        price = int(prices[j].text.replace("技術點", "")) #價錢的點數
        if count >= price:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(buttons[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break