from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.initProps()


    def initProps(self):
        self.urls = {
            'vapeluxe': 'https://vapeluxe.ru/catalog/devices',
            'zenmod': 'https://zenmod.shop/ec/pod/',
        }

    
    def getAllParsedData(self):
        result = []
        for shop, url in self.urls.items():
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'lxml')

            if shop == 'vapeluxe':
                devices_list = soup.find_all('div', class_="product__shop")

                for i, device in enumerate(devices_list):
                    name = device.find('div', class_="product__name").text
                    price = device.find('div', class_="product__cart").find('span').text
                    obj = {
                        'id': i,
                        'shop': 'vapeluxe',
                        'type': 'device',
                        'inventor': name.lower().split()[0],
                        'model': ' '.join(name.split()[1:]),
                        'price': price #[0].strip('₽')
                    }
                    result.append(obj)

            elif shop == 'zenmod':
                devices_list = soup.find_all('div', class_='prdl__item')

                for i, device in enumerate(devices_list):
                    name = device.find('a', class_="prdc__title").text
                    price = device.find('div', class_="prdc__price-wrapper")
                    obj = {
                        'id': i,
                        'shop': 'zenmod',
                        'type': 'device',
                        'inventor': name.lower().split()[0],
                        'model': ' '.join(name.split()[1:]),
                        'price': price.text.split('₽')[len(price.text.split('₽')) - 2].strip(' ') + ' рублей'
                    }
                    result.append(obj)

        return result