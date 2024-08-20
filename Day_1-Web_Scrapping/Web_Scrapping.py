import requests #To send http request to the website
from bs4 import BeautifulSoup #To parse the html and ectract data
import pandas as pd #To store data in csv file


url = "http://books.toscrape.com/" #site to test scrapping
response = requests.get(url) #fetches the content on url and stores it in a variable

soup = BeautifulSoup(response.text, 'html.parser') #This step transforms the raw HTML into a navigable structure that BeautifulSoup can work with.

#you have to find the tags 

books = []
for book in soup.find_all('article',class_='product_pod'): #find all entries
    title = book.h3.a['title'] #extracts title
    price = book.find('p', class_='price_color').text #extract prices
    availability = book.find('p', class_='instock availability').text.strip() #Extract Availability
    books.append([title, price, availability]) #appends to the books []


df = pd.DataFrame(books, columns=['Title','Price','Availability']) #generates a dataframe for easy handling
df.to_csv('books.csv',index=False)
    


