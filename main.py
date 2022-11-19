from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codecs
import json

driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")


def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(5)

        y = 1000
        for timer in range(0,10):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 1000
            time.sleep(1)
        
        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

        goods_str = ''
    
        k=0
        res=[]

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_price = good.find_element(By.CLASS_NAME, "goods-card__price-now").text
            good_link = good.find_element(By.CLASS_NAME, "goods-card__container").get_attribute('href')
            print(good_title, good_price, good_link)

            goods_str = goods_str + good_title + ' ' + good_price + ' ' + str(good_link) + "\n"
            
            # res.append([goods_str])

            res.append({
                'k'+1 
                'name': good_title, 
                'link': good_link, 
                'price': good_price
                })

        with codecs.open("ParsingRes.txt", "w", "utf-8") as stream:
            stream.write(goods_str)

        with open('ParsingResult.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, indent = 4, ensure_ascii=False)

    except Exception as ex:
        print("An error occured: \n" + str(ex))
main() 