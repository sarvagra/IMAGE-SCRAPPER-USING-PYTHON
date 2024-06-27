import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging 

flipkart_url= "https://www.flipkart.com/search?q="+"macbooks"
urlclient=uReq(flipkart_url)
print(urlclient)
#to get data dump, use urlclient.read()
flipkart_page=urlclient.read()

flipkart_html=bs(flipkart_page,'html.parser')

#how to create a click