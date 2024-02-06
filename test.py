from bs4 import BeautifulSoup
from selenium import webdriver
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
import datetime
import getpass
import platform
from browsermobproxy import Server


# server = Server("path/to/browsermob-proxy/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()
# proxy_address = proxy.proxy
app=Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template("index.html")
#     s=Service(ChromeDriverManager().install())
#     driver=webdriver.Chrome(service=s)
#     chrome_options = Options()
#     driver = webdriver.Chrome(options=chrome_options)

    
#     mobile_emulation = {
#     "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# }

#     #chrome_options.add_argument(f'--proxy-server={proxyserver.proxy}')
#     #chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#     chrome_options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
#     driver = webdriver.Chrome(options=chrome_options)
#     brand=[]
#     name=[]
#     size=[]
#     price=[]
#     image=[]
#     category=[]
#     rank=[]
#     category_url=[]
#     category_name=[]
#     loc=[]

#     def set_location_cookie(driver, latitude, longitude):
#         cookie = {
#             'name': 'geolocation',
#             'value': f'{{"latitude": {latitude}, "longitude": {longitude}}}',
#             'domain': '.swiggy.com',  # Make sure the domain matches the current page's domain
#         }
#         driver.add_cookie(cookie)



# # List of cities
#     cities = {
#         #'Delhi': {'latitude': 28.6139, 'longitude': 77.2090},
#         'Kolkata': {'latitude': 22.5726, 'longitude': 88.3639},
#     #     'Mumbai': {'latitude': 19.0760, 'longitude': 72.8777},
#     #     'Chennai': {'latitude': 13.0827, 'longitude': 80.2707},
#     }
    
#     links=[ 'https://www.swiggy.com/instamart/category-listing?categoryName=Fresh+Vegetables&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Fresh+Fruits&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Dairy%2C+Bread+and+Eggs&custom_back=true&taxonomyType=All+Listing',
# 'https://www.swiggy.com/instamart/category-listing?categoryName=Atta,+Rice+and+Dals&custom_back=true&taxonomyType=All+Listing',
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

#         # Open Swiggy for the current city
#     #         driver.get("https://www.swiggy.com/")
#     # url=pd.read_excel(r'instamart_url.xlsx')
#     # url=list(url['links'])
#     # url=url[2:]
#     for i in links:
#         driver.get(i)
#         time.sleep(2)
#         driver.implicitly_wait(10)

#         # You can perform any other actions on the website as needed
#         pageSource = driver.page_source
#         soup = BeautifulSoup(pageSource, 'html.parser')
#         # Optional: Wait for a few seconds before moving to the next city
#         t=driver.find_element(By.CLASS_NAME,"item-wrapper").text
#         if t=='Bestsellers':
#             print(t)
#             print(driver.current_url)
#             pageSource = driver.page_source
#             soup = BeautifulSoup(pageSource, 'html.parser')
#             driver.implicitly_wait(10)
#             count=1
#             for j in soup.find_all("div",attrs={"data-testid":"ItemWidgetContainer"}):
                
#                 a=j
#                 driver.implicitly_wait(10)
#                 image.append(a.find('img')['src'])
#                 brand.append(a.find('div',attrs={"data-testid":"brand-name"}).text)
#                 if a.find('div',attrs={"class":"sc-aXZVg feliul SF1nE"}):
#                     name.append(a.find('div',attrs={"class":"sc-aXZVg feliul SF1nE"}).text)
#                 else:
#                     name.append("na")
#                 size.append(a.find('div',attrs={"class":"novMV"}).text)
#                 price.append(a.find('div',attrs={"class":"sc-aXZVg fVjROI Wf3-P"}).text)
#                 category_url.append(driver.current_url)
#                 category_name.append(soup.find('h1',attrs={"class":"sc-aXZVg bUjCLt"}).text)
#                 rank.append(count)
#                 loc.append("mumbai")
#                 count+=1
#             else:
#                 pass
#             driver.implicitly_wait(10)    
#     d={"brand":brand,
#     'name':name,
#     'size':size,
#     'price':price,
#     'image':image, 
#     'rank':rank,
#     'category_url':category_url,
#     'category_name':category_name,
#     "location":loc}      
#     df=pd.DataFrame(d,columns=d.keys())  
#     x = datetime.datetime.now()
#     dt=x.strftime("%x")
#     df.to_excel("dt.xlsx")
            
            

            
#     driver.quit()
#     return name    
#proxyserver.stop()
    
    # finally:
    #     # Close the browser window

    


if __name__=="__main__":
    app.run(debug=True)