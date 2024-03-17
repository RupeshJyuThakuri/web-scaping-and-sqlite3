import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('Daraj_Catagories.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS categories (Category_Name text)''')

def get_content(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.find_all('span', class_="txt-holder")
    
    for category in categories:
        category_text = category.text
        c.execute('''INSERT INTO categories VALUES (?)''', (category_text,))

if __name__ == '__main__':
    URL = "https://www.daraz.com.np/#hp-official-stores"
    get_content(URL)
    conn.commit()
    print('complete')
    
c.execute('''SELECT * FROM categories''')
result = c.fetchall()
print(result)

conn.close()
