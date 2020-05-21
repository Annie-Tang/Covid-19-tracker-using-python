# Python Final Project
# news.py
# Author: Zihan Tang
# scraping CDC latest news of Covid-19

import requests
from bs4 import BeautifulSoup

#-------------------------------------------------
# function to scraping covid-19 latest news from CDC
def scraping_News():
    url = 'https://www.cdc.gov/media/index.html'
    # get web page using requests library
    web_content = requests.get(url).text
    # parser data using BeautifulSoup
    soup = BeautifulSoup(web_content, "html.parser")
    # get CDC latest news after analyzing html
    news = soup.find_all('a',{'class':'item-title'})
    # list to store news headlines and links
    newsdata = []
    temp = []
    for link in news:
        temp.append(link.string)
        if str(link.get('href'))[0] == "h":
            linktemp = str(link.get('href'))
            temp.append(linktemp)
        else:
            linktemp = "https://www.cdc.gov" + str(link.get('href'))
            temp.append(linktemp)
        newsdata.append(temp)
        temp = []
    # return list of all news headlines and links
    return newsdata

scraping_News()
