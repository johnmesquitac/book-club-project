from asyncore import read
import psycopg2 as ps
import pandas as pd

try:
    connection = ps.connect(
        user='postgres',
        password='@Akira',
        host='localhost',
        port='5432',
        database='postgres'
    )
    cursor = connection.cursor()

    read_data = pd.read_csv(r'C:\Users\mesqu\Documents\Scrapping-Books-Project\retrieving_data_from_page\books_data.csv')
    for _,row in read_data.iterrows():
        cursor.execute("INSERT INTO books (title, price, stars, stock) VALUES (%s,%s,%s,%s)" , (row['title'], float(row['price']), row['star'], row['stock']))
    connection.commit()
    connection.close()

except (Exception, ps.Error) as error:
    print(error)

