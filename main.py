from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path= r".\driver\msedgedriver.exe", options="")



def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

        goods_str = ''

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_price = good.find_element(By.CSS_SELECTOR, '.goods-card__price-now').text
            good_link = good.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            goods_str = goods_str + good_title + ' ' + good_price + '\n' + good_link + '\n'

        


        file = open(r'C:\Users\79181\OneDrive\Рабочий стол\selenium intro\textgoodswb.txt', 'w', encoding= 'utf-16')
        file.write(goods_str)
        file.close
    except Exception as ex:
        print("An error occured: \n" + str(ex))


main()
