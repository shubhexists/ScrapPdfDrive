# https://www.pdfdrive.com/download.pdf?id=162071379&h=9820954ddfcfe6ea6887bbcb9808050e&u=cache&ext=pdf
# https://www.pdfdrive.com/download.pdf?id=136494023&h=1aa480a89378f61c111d68cdd8632b97&u=cache&ext=pdf
# https://www.pdfdrive.com/zero-to-one-notes-on-startups-or-how-to-build-the-future-d162071379.html
# https://www.pdfdrive.com/download.pdf?id=178130338&h=c730f19386e30e06531c7b02ed17b300&u=cache&ext=pdf

import requests
import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def searchBook(bookName):
    bookName_lower = bookName.lower()
    final_bookName = ""
    for i in bookName_lower:
        if i != " ":
            final_bookName+=i
        else:
            final_bookName+='-'
    
    url = "https://www.pdfdrive.com/" + final_bookName +"-books.html"
    res = requests.get(url)
    bookList = []
    soup = bs4.BeautifulSoup(res.text, "lxml")
    link = soup.find_all("a",href=True)
    for i in link[17:37]:
        j = i["href"]
        k = j[:-15:1]+"d"+j[-14::]
        bookList.append(k)
    return bookList


def getDownLoadLink (url_endPoint):
    downloadLink = ''
    url = "https://www.pdfdrive.com"+url_endPoint
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(url)
    time.sleep(15)
    squadPage=driver.page_source
    soup = bs4.BeautifulSoup(squadPage, "lxml")
    book = soup.find_all("a",href=True)
    for i in book:
        j = i['href']
        if j[-3:] == 'pdf':
            downloadLink = j
            break    
    return downloadLink

def downloadBook(url):
    res = requests.get('https://www.pdfdrive.com'+url)
    with open("book.pdf", "wb") as f:
        f.write(res.content)