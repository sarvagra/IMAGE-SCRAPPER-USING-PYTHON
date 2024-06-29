import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging 
logging.basicConfig(filename="00_logging.log", level=logging.DEBUG,format='%(asctime)s%(message)s')
flipkart_url= "https://www.flipkart.com/search?q="+"macbooks"

urlclient=uReq(flipkart_url)

print(urlclient)
#to get data dump, use urlclient.read().
flipkart_page=urlclient.read()

flipkart_html=bs(flipkart_page,'html.parser')

#how to create a click.

product_link="https://www.flipkart.com"+"/apple-2022-macbook-air-m2-8-gb-ssd-256-gb-ssd-mac-os-monterey-mlxw3hn-a/p/itmc2732c112aeb1?pid=COMGFB2GSG8EQXCQ&amp;lid=LSTCOMGFB2GSG8EQXCQJWHH2F&amp;marketplace=FLIPKART&amp;q=macbooks&amp;store=6bo%2Fb5g&amp;srno=s_1_3&amp;otracker=search&amp;otracker1=search&amp;fm=organic&amp;iid=19a8002f-354b-4ea8-9960-9f94bfb4b421.COMGFB2GSG8EQXCQ.SEARCH&amp;ppt=hp&amp;ppn=homepage&amp;ssid=ukuigx4dts0000001719556654265&amp;qH=76885621d5a99940"
bigbox=flipkart_html.findAll("div",{"class":"cPHDOP col-12-12"})
print(len(bigbox))
product_req=print(bigbox[3].div.div.div.a['href']) 
print(product_link) #prints product link.

# to get all url's use for loop in bigbox length range.

product_req=requests.get(product_link)
product_html=bs(product_req.text,'html.parser')
comment_box=product_html.findAll("div",{"class":"RcXBOT"})

print(len(comment_box)) #finding number of comment boxes

print(comment_box[0].div.div.div.div.text) #extracting rating
print(comment_box[0].div.div.div.p.text) # extracting header
print(comment_box[0].div.div.find_all("div",{"class":""})[0].div.text) 

for i in comment_box:
    print("name:"+i.div.div.find_all('p',{"class":"_2NsDsF AwS1CA"})[0].text) #printing names of all customers
    print("rating:"+ i.div.div.div.div.text) #printing rating given by all customers
    print(i.div.div.div.p.text)
#to get the name of the customer who reviewed.


