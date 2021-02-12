from selenium import webdriver
from typing import List


class HandlerFrexco:
    def __init__(self):
        chromedriver = "D:\\webdriverchrome\\chromedriver.exe"
        self.browser = webdriver.Chrome(chromedriver)

    def load_site(self, site='https://deliverydireto.com.br/frexco/frexco2'):
        self.browser.get(site)

    def close_page(self):
        self.browser.quit()

    def get_elements_list(self) -> List:
        elements = self.browser.find_elements_by_xpath("//div[@class='products-section__body']")
        list_products = list()
        list_items = list()

        for x in range(len(elements)):
            list_products.append(elements[x].text)
            last_item = list_products[-1]
            itens = last_item.split('add')
            for item in itens:
                vegetable = item.split('\n')
                for space in vegetable:
                    if space == '':
                        vegetable.remove(space)
                for i in vegetable:
                    if i == []:
                        vegetable.remove([i])
                list_items.append(vegetable)
        print(list_items)
        return list_items
