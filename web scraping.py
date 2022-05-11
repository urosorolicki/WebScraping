from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pandas
import csv as pd

driver = webdriver.Chrome("/Users/ladminp/Downloads/chromedriver")
products=[] 
prices=[] 
ratings=[] 
driver.get("<a href="">https://ananas.rs/proizvod/hyundai-kuvalo-za-vodu-hy-2015a/142570")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
