from selenium import webdriver


class DriverUtilsFrubana:

    def load_site(self, site='https://br.frubana.com/spo'):
        browser = webdriver.Firefox()
        browser.get(site)