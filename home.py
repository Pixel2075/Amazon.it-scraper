from scraper4py import get_specs,get_details,get_image,get_asin
from scraper import get_item,get_url_desc_price,get_image2 
import requests
from bs4 import BeautifulSoup
from datetime import datetime  
def scrape(): 
    results = get_item(input('search term: '))
    print('time started: {}'.format(datetime.now()))
    print('{} items found including sponsors'.format(len(results)))
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    product_list = [] 
    for result in results:
        url = get_url_desc_price(result)[0]['url']
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        description = get_url_desc_price(result)[0]['description']
        price = get_url_desc_price(result)[0]['price'] 
        asin = get_asin(url)
        details = get_details(url,soup)
        images = get_image(url,soup,result)
        specs = get_specs(url,soup)
        product = {'url':url,'description':description,'price':price,'asin':asin,'details':details,'specs':specs,'images':images}
        product_list.append(product)
        print(product)
    print('time ended: {}'.format(datetime.now()))
    return product_list 

try:       
    user_input = input('want to store in a file: y/n? ').split(' ') 
    if user_input == 'y':
        with open(input('filename: ','wt')) as f:
            print(scrape(),file=f)
    else:
        scrape() 
except Exception as e:
    print('error occured description: {}'.format(e))
    


