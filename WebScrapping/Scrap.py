from bs4 import BeautifulSoup
import requests
URL = "https://www.hamropatro.com/"
r = requests.get(URL)
print(r.content)

soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())