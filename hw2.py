from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codecs
from selenium.webdriver.chrome.service import Service
import json


s = Service("./driver/chromedriver")
driver = webdriver.Chrome(service=s)


def main():
    try:
        driver.get("https://www.wildberries.ru/")

        for i in range(1, 100, 15):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight * {} / 100);".format(i))
            time.sleep(1)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")
        goods_json = []

        for good in goods_arr:
            description = good.find_elements(By.CSS_SELECTOR, '.goods-card__description span')[1].text
            price = good.find_elements(By.CSS_SELECTOR, '.goods-card__price-now')[0].text
            href = good.find_elements(By.CSS_SELECTOR, '.goods-card__container')[0].get_attribute('href')

            good_json = {
                'description': description,
                'price': price,
                'href': href
            }
            goods_json.append(good_json)

        with codecs.open("vvv.json", "wb", "utf=16") as stream:
            json.dump(goods_json, stream, ensure_ascii=False)

    except Exception as ex:
        print("An error occured: \n" + str(ex))


main()
