# Python Final Project
# covid19.py
# Author: Annis
# scraping USA coronavirus cases of every state

import requests
from bs4 import BeautifulSoup

#--------------------------------------------------
# scraping USA cases on worldometers.info
url = "https://www.worldometers.info/coronavirus/country/us/"
# get web page using requests library
web_content = requests.get(url).content
# parser data using BeautifulSoup
soup = BeautifulSoup(web_content, "html.parser")
# function to scraping web data
def getinfo():
    # list to store every state's various cases
    datalist = []
    temp = []
    num = 1
    for k in soup.find_all('td'):
        i = str(k.string).replace('\n', '').replace('\r', '')
        if i == '\xa0' or i == 'None':
            i = ''
        if num < 7:
            temp.append(i)
        elif num > 11:
            num = 1
            datalist.append(temp)
            temp = []
            temp.append(i)
        if k.string == '\nVeteran Affairs ':
            break   # get data until states name ends
        num += 1
    return datalist
    # elements in datalist: [state, total cases, new cases, total deaths, new deaths, active cases]
getinfo()


