import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://github.com/MaGicInU?tab=repositories'

data = requests.get(url)
html=BeautifulSoup(data.text,'html.parser')
repos=html.findAll('li', attrs = {'class':'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})


details=[]


for repo in repos:
    detail={}
    name=repo.findAll('a',attrs = {'itemprop':'name codeRepository'})
    detail['name']=(name[0].text.strip())
    try:
        desc=repo.findAll('p',attrs = {'itemprop':'description'})
        detail['description']=(desc[0].text.strip())
    except:
        detail['description']="none"
        

    details.append(detail)
pprint(details)

