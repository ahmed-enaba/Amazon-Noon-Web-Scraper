from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

item_detalils=[]
item_detalils2=[]

about=input("Enter what do you want to search about: ")

url="https://www.amazon.eg"
url2=f"https://www.noon.com/egypt-en/search/?q={about}"

def amazon(link):
    service=Service(ChromeDriverManager().install())
    browser=webdriver.Chrome(service=service)
    browser.get(link)
    time.sleep(5)

    search_bar=browser.find_element('id','twotabsearchtextbox')
    search_bar.send_keys(about)
    search=browser.find_element('id','nav-search-submit-button').click()
    items = browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    time.sleep(10)

    for item in items:
        html_code=item.get_attribute("outerHTML")
        soup=BeautifulSoup(html_code,'html.parser')
        try:
            item_name=item.find_element(By.XPATH,".//h2//span").text
        except:
            item_name="you have a error in prodect name"

        try:
            price=item.find_element(By.XPATH,".//span[@class='a-price-whole']").text
        except:
            price="N/A"

        try:
            rate=item.find_element(By.XPATH,".//div[@class='a-row a-size-small']").text
        except:
            rate="N/A"
        
        try:
            item_link=item.find_element(By.XPATH,".//a").get_attribute("href")
        except:
            link="N/A"


        item_detalils.append({
            'item name':item_name,
            'price':price,
            'link':item_link,
            'rate':rate
        })

    browser.quit()
    

amazon(url)


def noon(link):
    service=Service(ChromeDriverManager().install())
    browser=webdriver.Chrome(service=service)
    browser.get(link)
    time.sleep(5)
    items=browser.find_elements(By.XPATH,"//div[@class='PBoxLinkHandler-module-scss-module__WvRpgq__linkWrapper']")
    
    for item in items:
        try:
            item_name=item.find_element(By.XPATH,".//h2[@class='ProductDetailsSection-module-scss-module__Y6u1Qq__title']").text
        except:
            item_name=" "

        try:
            item_price=item.find_element(By.XPATH,".//strong[@class='Price-module-scss-module__q-4KEG__amount']").text
        except:
            item_price="the item is finished rite now"
        
        try:
            item_rate=item.find_element(By.XPATH,".//div[@class='RatingPreviewStar-module-scss-module__zCpaOG__textCtr']").text
        except:
            item_rate="prodect has no rated"
        
        try:
            item_link=item.find_element(By.XPATH,".//a").get_attribute("href")
        except:
            item_link="item is finished"

        item_detalils2.append({
            'item name':item_name,
            'price':item_price,
            'link':item_link,
            'rate':item_rate
        })


noon(url2)



def making_file():
    path='G:/Selenium app with python/csv.csv'
    key=item_detalils[0].keys()
    with open (path,'+w',newline='',encoding='UTF-8')as output_file:
        dict_writer=csv.DictWriter(output_file,key)
        dict_writer.writeheader()
        dict_writer.writerows(item_detalils)
        stars_row = {k: "*****************" for k in key}
        dict_writer.writerow(stars_row) 
        dict_writer.writerows(item_detalils2)
        print("csv file created successfuly")
making_file()
