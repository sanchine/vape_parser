from sys import argv, exit
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication
from widgets.application import Application
from utils.presenter import Presenter
from utils.database import Database


if __name__ == "__main__":
    app = QApplication(argv)

    main_window = Application()
    presenter = Presenter(Database(), main_window)

    exit(app.exec_())

exit()














with open("pages/vapeluxe_devices.html") as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, 'lxml')

devices_list = soup.find_all('div', class_="product__shop")

file = open('./catalog/vapeluxe.txt', 'w')

for device in devices_list:
    name = device.find('div', class_="product__name")
    price = device.find('div', class_="product__cart").find('span')
    file.write(name.text + '\t|\t' + price.text + '\n')

file.close()
    