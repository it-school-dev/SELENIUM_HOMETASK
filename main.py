from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service('.\webdriver\chromedriver.exe'))
driver.maximize_window()

#Сделать адекватную самостоятельную промотку
#Перенести в файл(json). Возможно, объектами

def main():
    try:
        driver.get('https://www.wildberries.ru/')
        time.sleep(2)

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight/2);')
        time.sleep(2)

        goods_arr=driver.find_elements(By.CLASS_NAME, 'goods__item')
        for good in goods_arr:
            good_title=good.find_elements(By.CSS_SELECTOR,'.goods-card__description span')[1].text
            good_price=good.find_element(By.CLASS_NAME,'goods-card__price-now').text
            good_url=good.find_element(By.CLASS_NAME, 'goods-card__container').get_attribute('href')
            print(good_title,good_price,good_url)
        print(len(goods_arr))
    except Exception as ex:
        print('Error with '+str(ex))

main()