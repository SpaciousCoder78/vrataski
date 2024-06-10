#importing packages
from bs4 import BeautifulSoup
import html5lib
import requests

#target url
url = input('Enter URL: ')

#getting the contents of page by requesting

try:
    response = requests.get(url)
    doc=BeautifulSoup(response.text,"html5lib")
    print(doc.prettify())
except:
    print("Exception occurred")