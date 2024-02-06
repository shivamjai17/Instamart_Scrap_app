from asyncio import wait
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, render_template,request
from selenium.webdriver.chrome.service import Service
import pandas as pd 
import json
import time
from datetime import datetime
import getpass
import platform

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def index():
    chrome_options = ChromeOptions()
# Initialize the WebDriver (assuming you are using Chrome)

    cities = ['Bangalore','Chennai', 'Delhi','Mumbai', 'Kolkata', 'Hyderabad']
    selected_city = None

    if request.method == 'POST':
        selected_city = request.form.get('city')
    
    return render_template('front.html', cities=cities, selected_city=selected_city)   
@app.route('/scrape', methods=['POST'])
def scrape(): 
    selected_city = request.form['city']
    # mobile_emulation = {
    # "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    # }

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #chrome_options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    
    driver = webdriver.Chrome(options=chrome_options)

 

    
    # driver.get("https://www.swiggy.com/")
    # driver.find_element(By.CLASS_NAME,"_1NdRR").click()
    # driver.implicitly_wait(10)
    # time.sleep(2)
    # l=driver.find_element(By.CLASS_NAME,"_3B7Eo")
   
    # l.send_keys(selected_city)
    # time.sleep(5)
    # driver.find_element(By.CLASS_NAME,"_3qV1m").click()
    start = time.process_time()
    driver.get("https://www.swiggy.com/")
    driver.find_element(By.CLASS_NAME,"_2z2N5").click()
    driver.implicitly_wait(5)
    l=driver.find_element(By.TAG_NAME,"input")
    
    l.send_keys(selected_city)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"_2peD4").click()



    time.sleep(1)
    driver.implicitly_wait(5)

    #driver.get("https://www.swiggy.com/instamart/category-listing?categoryName=Fresh+Vegetables&custom_back=true&taxonomyType=All+Listing")
    brand=[]
    name=[]
    size=[]
    price=[]
    image=[]
    category=[]
    rank=[]
    category_url=[]
    category_name=[]
    loc=[]
#     links=[ 'https://www.swiggy.com/instamart/category-listing?categoryName=Fresh+Vegetables&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Fresh+Fruits&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Dairy%2C+Bread+and+Eggs&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Rice%2C+Atta+and+Dals&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Masalas+and+Dry+Fruits&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Edible+Oils+and+Ghee&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Munchies&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Sweet+Tooth&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Cold+Drinks+and+Juices&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Biscuits+and+Cakes&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Instant+and+Frozen+Food&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Meat+and+Seafood&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Cereals+and+Breakfast&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Sauces+and+Spreads&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Tea,+Coffee+and+More&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Cleaning+Essentials&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Hygiene+and+Wellness&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Bath,+Body+and+Hair&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Paan+Corner&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Home+and+Kitchen&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Office+and+Electricals&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Baby+Care&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Pet+Supplies&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Beauty+and+Grooming&custom_back=true&taxonomyType=All+Listing']

        # Open Swiggy for the current city
    #         driver.get("https://www.swiggy.com/")
    # url=pd.read_excel(r'instamart_url.xlsx')
    # url=list(url['links'])
    # url=url[2:]
    bang_links=[
"https://www.swiggy.com/instamart/category-listing?categoryName=Dairy%2C+Bread+and+Eggs&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Masalas+and+Dry+Fruits&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Edible+Oils+and+Ghee&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Munchies&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Sweet+Tooth&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Cold+Drinks+and+Juices&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Biscuits+and+Cakes&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Instant+and+Frozen+Food&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Meat+and+Seafood&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Cereals+and+Breakfast&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Sauces+and+Spreads&custom_back=true&taxonomyType=All+Listing",
"https://www.swiggy.com/instamart/category-listing?categoryName=Tea%2C+Coffee+and+More&custom_back=true&taxonomyType=All+Listing"


]
    for i in bang_links:
        driver.get(i)
        time.sleep(2)
        driver.implicitly_wait(5)

        # You can perform any other actions on the website as needed
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        # Optional: Wait for a few seconds before moving to the next city
        wait = WebDriverWait(driver, 3)
        #t=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"item-wrapper")))
        t=driver.find_element(By.CLASS_NAME,"item-wrapper").text
        
        if t=='Bestsellers':
            print(t)
            print(driver.current_url)
            pageSource = driver.page_source
            soup = BeautifulSoup(pageSource, 'html.parser')
            driver.implicitly_wait(5)
            count=1
            for j in soup.find_all("div",attrs={"data-testid":"ItemWidgetContainer"}):
                
                a=j
                driver.implicitly_wait(4)
                time.sleep(2)
                image.append(a.find('img')['src'])
                brand.append(a.find('div',attrs={"data-testid":"brand-name"}).text)
                if a.find('div',attrs={"class":"sc-aXZVg feliul SF1nE"}):
                    name.append(a.find('div',attrs={"class":"sc-aXZVg feliul SF1nE"}).text)
                else:
                    name.append("na")
                size.append(a.find('div',attrs={"class":"novMV"}).text)
                price.append(a.find('div',attrs={"class":"sc-aXZVg fVjROI Wf3-P"}).text)
                category_url.append(driver.current_url)
                category_name.append(soup.find('h1',attrs={"class":"sc-aXZVg bUjCLt"}).text)
                rank.append(count)
                loc.append(selected_city)
                count+=1
            else:
                pass
            driver.implicitly_wait(2)    
    d={"brand":brand,
    'name':name,
    'size':size,
    'price':price,
    'image':image, 
    'rank':rank,
    'category_url':category_url,
    'category_name':category_name,
    "location":loc}      
    df=pd.DataFrame(d,columns=d.keys()) 
    current_datetime = datetime.now().strftime("%d-%m-%y")
    file_f=current_datetime+"_"+selected_city
    file=f'{file_f}.xlsx'
    df.to_excel(file,index=False)
         
    driver.quit()
    end = time.process_time() 
    print("Elapsed time using process_time()", (end - start) * 10**3, "ms.")
    return name
    
    


    

if __name__ == '__main__':
    app.run(debug=True)
