from asyncore import read
import psycopg2 as ps
import pandas as pd

try:
    connection = ps.connect(
        user='postgres',
        password='password',
        host='localhost',
        port='5432',
        database='postgres'
    )
    cursor = connection.cursor()

    read_data = pd.read_csv(r'PATH')
    for _,row in read_data.iterrows():
        cursor.execute("INSERT INTO books (title, price, stars) VALUES (%s,%s,%s)" , (row['title'], float(row['price']), row['star']))
    connection.commit()
    connection.close()

except (Exception, ps.Error) as error:
    print(error)

