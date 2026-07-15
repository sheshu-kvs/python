# An WebScraping are used to the collect data from the browser stro it on the local system in the database

import requests
from bs4 import BeautifulSoup

url="http://www.bu.edu/president/boston-university-facts-stats/";
url="http://terrawebs.com";

resp=requests.get(url);
content= resp.content   # we will get the content from  the browser
soup = BeautifulSoup(content,'html.parser')
print(soup.title)
print(soup.body.h3)


