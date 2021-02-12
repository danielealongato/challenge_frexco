from selenium import webdriver
from view.utilities_frexco import HandlerFrexco


class GetInformation:

    def __init__(self):
        self.driver_utils = HandlerFrexco()


    def get_information(self):
        self.driver_utils.load_site(site='https://br.frubana.com/spo')