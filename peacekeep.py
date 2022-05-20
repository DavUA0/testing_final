from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url_peacekeep = 'https://mil.am/hy/pages/37'

class PeacekeepPage:
    URL = base_url_peacekeep
    TBODY = (By.TAG_NAME, 'tbody')
    TR = (By.TAG_NAME, 'tr')
    TD = (By.TAG_NAME, 'td')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getCountries(self):
        table = self.browser.find_element(*self.TBODY)
        first_row = table.find_element(*self.TR)
        countries = first_row.find_elements(*self.TD)
        
        return countries[1:]
