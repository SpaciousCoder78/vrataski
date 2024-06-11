#importing packages
from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

#target url
url = input('Enter URL: ')

#getting the contents of page by requesting

try:
    response = requests.get(url)
    doc=BeautifulSoup(response.text,"html5lib")
    print(doc.prettify())
    data = []
    for row in doc.find_all('tr'):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    # Arrange data into a pandas DataFrame
    df = pd.DataFrame(data, columns=['ID', 'County', 'District', 'School', 'Type', 'Public/Private', 'Charter', 'Status'])

    # Save DataFrame to CSV
    df.to_csv('output.csv', index=False)
except:
    print("Exception occurred")