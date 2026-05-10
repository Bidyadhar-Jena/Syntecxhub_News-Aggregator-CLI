import requests
from bs4 import BeautifulSoup

#Requesting the websie
URL='https://timesofindia.indiatimes.com/'

#Fake browser identity
headers = {
    "User-Agent":"Mozilla/5.0"
}

response=requests.get(URL,headers=headers)

#Parese the HTML Document
soup=BeautifulSoup(response.content, 'html.parser')

#Extract the news headline from HTML
headlines=soup.find_all('span')
seen = set()

#Display the Headlines
print("\nAll TOI Headlines:\n")

for headline in headlines:
    text = headline.get_text(strip=True)

    if len(text) > 25 and text not in seen:
        seen.add(text)
        print(text)
        print()