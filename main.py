from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codecs

driver =webdriver.Chrome(executable_path="./webdriver/chromedriver.exe", options="")


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)


def main():
    try:
        
        driver.get("https://www.wildberries.ru/")
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

        # print (goods_arr[0].get_attribute('innerHTML'))

        goods_str=''

        for good in goods_arr:
            # good_title=good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            Good_Inf='Good: ' + good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text + '\nLink: ' + good.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') + '\nPrice: ' + good.find_element(By.CSS_SELECTOR,".goods-card__price-now").text
            print(Good_Inf)  
            goods_str = goods_str + Good_Inf + '\n'


        with codecs.open("Good_Inf.txt", "w", "utf-16") as stream:   # or utf-8
            stream.write(goods_str)

    except Exception as ex:
        print ("An error occured: \n" + str(ex))


main()


