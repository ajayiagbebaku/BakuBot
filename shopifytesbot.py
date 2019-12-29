import requests
import json
import time
from selenium import webdriver



def availabilitycheck():
    r = requests.get('https://feature.com/products.json')
    products = json.loads((r.text))['products']

    for product in products:
        print (product['title'])
        productname = product['title']

        if productname == 'Jordan Legacy AJ11 SS 23 Tee - Gym Red':
            producturl = 'https://feature.com/products/' + product['handle']
            print('found item')
            return (producturl)
    else:
        return False

def buyProduct(url):

    driver= webdriver.Chrome(executable_path=r'C:\Users\aagbebaku.TSI\Desktop\chromedriver.exe')
    driver.get(str(url))
    driver.find_element_by_xpath('//div[@data-value="XL"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="btn btn-solid"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('ajayi1987@me.com')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Ajayi')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Agbebaku')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('10941 Cleveland Ave')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Kansas City')
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys('66109')
    time.sleep(5)
    driver.find_element_by_xpath('//input[@data-backup="phone"]').send_keys('14699809950'+ u'\ue007')



myUrl = availabilitycheck()
if myUrl!= False:
        buyProduct(myUrl)
else:
    print('no')









