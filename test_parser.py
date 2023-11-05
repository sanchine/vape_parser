from bs4 import BeautifulSoup
import requests


page = requests.get('https://zenmod.shop/ec/pod/')
soup = BeautifulSoup(page.text, 'lxml')

devices_list = soup.find_all('div', class_='prdl__item')

result = []
for i, device in enumerate(devices_list):
    name = device.find('a', class_="prdc__title").text
    price = device.find('div', class_="prdc__price-wrapper")
    obj = {
        'id': i,
        'shop': 'zenmod',
        'type': 'device',
        'inventor': name.split()[0],
        'model': ' '.join(name.split()[1:]),
        'price': price.text.split('₽')[len(price.text.split('₽')) - 2].strip(' ') + '₽'
    }
    result.append(obj)

print(result)