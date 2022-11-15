from selenium import webdriver
from selenium.webdriver.common.by import By
import codecs
import time
import json

driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe", options="")


def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(3)

        y = 1000
        for timer in range(0,10):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 1000
            time.sleep(1)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")
        goods_str = ''
        mas = []

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_price = good.find_element(By.CLASS_NAME, "goods-card__price-now").text
            good_url = good.find_element(By.CSS_SELECTOR, ".goods-card__container").get_attribute('href')
            print(good_title, good_price, good_url)
            goods_str = goods_str + good_title + "\t" + good_price + "\t" + str(good_url) + "\n"
            mas.append([str(good_title), str(good_price), str(good_url)])

        arr = {i + 1: {
            'title': mas[i][0],
            'price': mas[i][1],
            'url': mas[i][2]
        } for i in range(len(mas))}
        
        with codecs.open("parseRes.txt", "w", "utf-16") as stream:   # or utf-8
            stream.write(goods_str)

        print(arr)
        
        with open('parsingData.json', 'w', encoding='utf-8') as f:
            json.dump(arr, f, indent=4, sort_keys=False, ensure_ascii=False)

    except Exception as ex:
        print("An error occured: \n" + str(ex))

    finally:
        driver.close()
        driver.quit()


main()