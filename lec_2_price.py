from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import codecs

driver = webdriver.Chrome("./chromedriver.exe")

driver.get('https://www.wildberries.ru/')

def main():
    try:
        driver.get('https://www.wildberries.ru/')
        time.sleep(2)

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

        goods_arr = driver.find_elements(By.CLASS_NAME, value='goods__item')

        goods_str = ''
        
        for good in goods_arr:
            good_price = good.find_element(By.CSS_SELECTOR, "ins").text
            print(good_price)
            goods_str = goods_str + good_price + '\n'

        # f = open("goods.txt", "a")
        # f.write("goods_str")
        # f.close()

        with codecs.open("hjlkl.txt", "w", "utf-16") as stream:   # or utf-8
            stream.write(goods_str)
    
    except Exception as ex:
        print('Error tut: \n' + str(ex))

main()