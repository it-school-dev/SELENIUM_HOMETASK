from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome(service=Service('.\webdriver\chromedriver.exe'))
driver.maximize_window()


def main():
    try:
        driver.get('https://www.wildberries.ru/')
        time.sleep(1)

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight/2);')
        time.sleep(1)

        goods_arr=driver.find_elements(By.CLASS_NAME, 'goods__item')
        i=0
        for good in goods_arr:

            good_title=good.find_elements(By.CSS_SELECTOR,'.goods-card__description span')[1].text
            good_price=good.find_element(By.CLASS_NAME,'goods-card__price-now').text
            good_url=good.find_element(By.CLASS_NAME, 'goods-card__container').get_attribute('href') #Поиск всей информации

            
            goods_arr[i]={                                      #Перезапись массива для хранения искомой информации
                    'name':good_title,
                    'price':good_price,
                    'url':good_url
                    }
            i+=1

            
        with open('WB pars.json', 'w', encoding='utf-8') as f:
            json.dump(goods_arr, f, indent=4, ensure_ascii=False)

    except Exception as ex:
        print('Error with '+str(ex))

main()