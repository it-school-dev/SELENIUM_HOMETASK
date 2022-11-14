


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codecs
import json
  

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

driver = webdriver.Chrome(executable_path="./driver/chromedriver",
                               chrome_options=options)
   


def main():
    try:
        driver.get("https://www.wildberries.ru")
        time.sleep(4)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        driver.execute_script('window.scrollTo({top: 0, behavior: "smooth"});')
        time.sleep(4)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")
        
        goods_dict = {}
        # goods_str = ''
        for good in goods_arr:
             good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
             good_link = good.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
             good_price = good.find_element(By.CSS_SELECTOR, '.goods-card__price-now').text

             good_dict = {}

             good_dict['good_price'] = good_price
             good_dict['good_link'] = good_link

            #  goods_str = goods_str + good_title + ' ' + good_price + '\n' + good_link + '\n'
            #  print(goods_str)

             goods_dict[str(good_title)] = good_dict

        # with codecs.open("parseRes.txt", "w", "utf-16") as stream:   # or utf-8
        #      stream.write(goods_str)

        with open("parseRes.json", "w", encoding="utf-16") as fp:
            json.dump(goods_dict, fp, indent=4, ensure_ascii=False)

    
    except Exception as ex:
        print("an error: \n" + str(ex))


    
main()
