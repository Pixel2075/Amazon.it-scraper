from bs4 import BeautifulSoup 
import requests
from requests_html import HTMLSession 
from scraper import get_url_desc_price,get_item,get_image2
def get_specs(url,soup):
    names = []
    specs_list = []
    specs_dict = {}
    i = 0
    try:
        specs1 = soup.find('table',{'class':'a-normal a-spacing-micro'})
        specs = specs1.find_all('tr')
        for name in specs:
            names.append(name.find('td',{'class':'a-span3'}).text)
        for spec in specs:
            specs_list.append(spec.find('td',{'class':'a-span9'}).text)
        for nam in names:
            specs_dict[nam] = specs_list[i]
            i += 1
    except Exception as e:
        #print(e) 
        try:
            s = HTMLSession()
            r = s.get(url)
            r.html.render(sleep=1)
            soup1 = BeautifulSoup(r.content,'html.parser')
            specs1 = soup1.find('table',{'class':'a-normal a-spacing-micro'})
            specs = specs1.find_all('tr')
            for name in specs:
                names.append(name.find('td',{'class':'a-span3'}).text)
            for spec in specs:
                specs_list.append(spec.find('td',{'class':'a-span9'}).text)
            for nam in names:
                specs_dict[nam] = specs_list[i]
                i += 1
        except Exception as e:
            specs = 'N/A'
            #print(e)
    return specs_dict 
def get_details(url,soup):
    f =0 
    names2 = [] 
    details_list = []
    details_dict = {} 
    try:
        details1 = soup.find('table',{'id':'productDetails_techSpec_section_1'})
        details = details1.find_all('tr')
        for name in details:
                names2.append(name.find('th').text)
        u = []
        for detail in details:
                u.append(detail.find('td').text.strip())  
        for namesi in range(len(u)):
                details_dict[names2[namesi]] = u[namesi]
    except Exception as e:
        #print(e) 
        try:
            s = HTMLSession()
            r = s.get(url)
            r.html.render(sleep=1)
            soup1 = BeautifulSoup(r.content,'html.parser')
            details1 = soup1.find('table',{'id':'productDetails_techSpec_section_1'})
            details = details1.find_all('tr')
            for name in details:
                    names2.append(name.find('th').text)
            u = []
            for detail in details:
                u.append(detail.find('td').text.strip())  
            for namesi in range(len(u)):
                    details_dict[names2[namesi]] = u[namesi]            
        except Exception as e:
            #print(e) 
            details_dict['details'] = 'N/A'
    return details_dict 
def get_image(url,soup,item):
    try:
        images = {}
        image1 = soup.find_all('div',{'id':'imgTagWrapperId'})
        for image in image1:
            founded = image.find_all('img')
            for img in founded:
                var = img['src']
                images['img_url'] = var
        splited = images['img_url'].split('/')[5]
        images['splited'] = splited
        images['non_splited'] = splited[0:-4]
    except Exception as e:
            #print(e) 
            try:
                images = get_image2(item)
            except Exception as e:
                images = {}
                image = soup.find_all('img')
                for imag in image:
                    pic = imag.split('/')
                    if pic[4] == 'I':
                        images['img_url'] = imag 
                        images['splited'] = pic[5]
                        images['non_splited'] = pic[5][0:-4] 
                        #print(e) 
                try:
                    images = {}
                    images['splited'] = 'N/A'
                    images['non_splited'] = 'N/A'
                    images['image_url'] = 'N/A'
                    #print(e)
                except:
                    print('Error While Retriving Image') 
    return images
    
def get_asin(url):
    try: 
        asin = url.split('/')[5]
    except:
        asin =  'Error'
    return asin


