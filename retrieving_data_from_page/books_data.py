from multiprocessing.dummy import current_process
from bs4 import BeautifulSoup
import requests
import pandas as pd

book_data = []
current_page = 'page-1.html'

while current_page is not None:
    url = "http://books.toscrape.com/catalogue/"+current_page
    r = requests.get(url)
    # Initiate beautiful and list element to extract all the rows in the table
    soup = BeautifulSoup(r.content, "html.parser")
    books = soup.find_all(lambda tag: tag.name == 'article')

    #scrapping throughout the pages, finding title, price and stars
    for book in books:
        insert_book = {}
        title = book.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.get('title') and tag.text)[0]['title']
        price = book.find("p", {"class": "price_color"}).text[1:]
        star = book.find("p", {"class": "star-rating"}).attrs['class'][1]
        stock = book.find("p", {"class":"instock availability"}).text
        insert_book['title'] = title
        insert_book['price'] = price
        insert_book['star'] = star
        insert_book['stock'] = stock.strip()
        book_data.append(insert_book)

    bottom_page = soup.find('ul', {"class":"pager"})
    pages = bottom_page.find_all('a')
    try:
        current_page = pages[1]['href']
    except:
        if current_page == 'page-1.html': #if i'm in the first page
            current_page = pages[0]['href']
        else: 
            current_page = None #if i reach the last page
        pass

df = pd.DataFrame(book_data)
df.to_csv(r'C:\Users\mesqu\Documents\Scrapping-Books-Project\retrieving_data_from_page\books_data.csv')
