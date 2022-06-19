from bs4 import BeautifulSoup 
import requests
import re 
from selenium import webdriver
from requests_html import HTMLSession
#template_2 = 'https://www.amazon.it/s?k={}&ref=nb_sb_noss_1'
def get_item2(search_term):
    driver = webdriver.Chrome()
    template = 'https://www.amazon.it/s?k={}'
    search_term = search_term.replace(" ","+")
    url = template.format(search_term)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all('div',{'data-component-type':'s-search-result'})
    i = 1
    for x in range(0,1000): 
        driver.get('{url}&page={page}'.format(url=url,page=i))
        soup1 = BeautifulSoup(driver.page_source, "html.parser")
        x = soup1.find_all('div',{'data-component-type':'s-search-result'})
        results += x 
        if len(x) == 0:
            break 
        i += 1
    return results 
def get_url_desc_price(item):
    products = []
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.it' + atag.get('href')
    try:
        price1 = item.find_all('div','a-section a-spacing-small s-padding-left-small s-padding-right-small')
        for money in price1:
            price2 = money.find('span','a-price')
            price = price2.find('span','a-offscreen').text
    except:
        try:
            price1 = item.find_all('div','a-section a-spacing-small s-padding-left-small s-padding-right-small')[0]
            price = price1.find('span',{'aria-hidden':'true'}).text
        except Exception as e:
            #print(e) 
            price = 'N/A'
    product = {'price':price,'description':description,'url':url}
    products.append(product)
    return products
def get_item1(search_term):
    s= HTMLSession()
    template = 'https://www.amazon.it/s?k={}'
    search_term = search_term.replace(" ","+")
    url = template.format(search_term)
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find_all('div',{'data-component-type':'s-search-result'})
    i = 1
    for x in range(0,1000): 
        new_page = s.get('{url}&page={page}'.format(url=url,page=i))
        new_page.html.render(sleep=1)
        soup1 = BeautifulSoup(new_page.content, "html.parser")
        x = soup1.find_all('div',{'data-component-type':'s-search-result'})
        results += x
        
        if len(x) == 0:
            break 
        i += 1
    return results 

def get_item(search_term):
    try:
        results = get_item1(search_term)
    except Exception as e:
        results = get_item2(search_term)
        #print(e)
    return results
def get_image2(item): 
    x = item.find_all('img') 
    for y in x:
        images = [] 
        if y['src'].split('/')[4] == 'I':
            images.append(y['src'])
            images.append(y['src'].split('/')[5])
            images.append(y['src'].split('/')[5][0:-4])
    return images 

