from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
from selenium.common.exceptions import TimeoutException
from tkinter import *
from tkinter import filedialog
from selenium.webdriver.chrome.options import Options
import os
import threading
from tkinter import *
from tkinter import filedialog, messagebox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver_path = ChromeDriverManager().install()

def make_browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    service = Service(driver_path)
    return webdriver.Chrome(service=service, options=options)


def amazon(link,keyword):
    browser=make_browser()
    try: 
        browser.get(link)
        wait = WebDriverWait(browser, 15)
        search_bar=wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))
        search_bar.send_keys(keyword)
    
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
        search_button.click()
        items = browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        time.sleep(2)

        for item in items:
            try:
                item_name=item.find_element(By.XPATH,".//h2//span").text
            except Exception:
                item_name="you have a error in prodect name"

            try:
                price=item.find_element(By.XPATH,".//span[@class='a-price-whole']").text
            except Exception:
                price="N/A"

            try:
                rate=item.find_element(By.XPATH,".//div[@class='a-row a-size-small']").text
            except Exception:
                rate="N/A"
            
            try:
                item_link=item.find_element(By.XPATH,".//a").get_attribute("href")
            except Exception:
                item_link="N/A"


            item_detalils.append({
                'item name':item_name,
                'price':price,
                'link':item_link,
                'rate':rate
            })
    except TimeoutException:
        print("we have a time error or you blocked")

    browser.quit()
    


def noon(keyword):
    browser=make_browser()
    try:
        url2=f"https://www.noon.com/egypt-en/search/?q={keyword}"
        browser.get(url2)
        wait=WebDriverWait(browser,15)
        wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'linkWrapper')]")
            ))
        items = browser.find_elements(By.XPATH, "//div[contains(@class,'linkWrapper')]")
        
        for item in items:
            try:
                item_name=item.find_element(By.XPATH,".//h2[@class='_title_i1yaq_19']").text
            except Exception:
                item_name="N/A"

            try:
                item_price=item.find_element(By.XPATH,".//strong[@class='_amount_1o2w0_59']").text
            except Exception:
                item_price="the item is finished rite now"
            
            try :
                item_rate=item.find_element(By.XPATH,".//div[@class='_textCtr_1r83y_16']").text
            except Exception:
                item_rate="prodect has no rated"
            
            try:
                item_link=item.find_element(By.XPATH,".//a").get_attribute("href")
            except Exception:
                item_link="item is finished"
            
            item_detalils2.append({
                'item name':item_name,
                'price':item_price,
                'link':item_link,
                'rate':item_rate
            })
    except Exception:
        print("we have a time error or you blocked")

    browser.quit()


def making_file(item_details):
    if not item_details:
        messagebox.showwarning("Warning", "we can't find informiation about this item")
        return
    folder = filedialog.askdirectory()

    file_path = os.path.join(folder,"products.csv")
    key=item_detalils[0].keys()
    with open (file_path,'+w',newline='',encoding='UTF-8')as output_file:
        dict_writer=csv.DictWriter(output_file,key)
        dict_writer.writeheader()
        dict_writer.writerows(item_detalils)
        stars_row = {k: "*****************" for k in key}
        dict_writer.writerow(stars_row) 
        dict_writer.writerows(item_detalils2)

    messagebox.showinfo("Done","Was Created😁")

def GOOO():
    keyword=label.get().strip()
    if not keyword:
        messagebox.showwarning("please enter a valid item to search about")
        return
    
    GO_button.config(state=DISABLED,text="loading....")
    amazon("https://www.amazon.eg",keyword)
    noon(keyword)
    making_file(item_detalils)
    GO_button.config(state=NORMAL,text="GO")

def thread():
    threading.Thread(target=GOOO,daemon=True).start()


item_detalils=[]
item_detalils2=[]


window=Tk()
window.title('buy overview')
window.geometry('600x400')
window.config(background= "gray81")

label=Entry(window,width=60)
label.place(x=120,y=60)


GO_button=Button(window,text="GO",activeforeground='SteelBlue3',command=thread)
GO_button.place(x=260,y=130)


window.resizable(False, False)
window.mainloop()


