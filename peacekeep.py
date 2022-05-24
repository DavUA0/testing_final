from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import constants


class PeacekeepPage:
    URL = constants.BASE_URL_PEACEKEEP
    TBODY = (By.TAG_NAME, constants.TBD)
    TR = (By.TAG_NAME, constants.TR)
    TD = (By.TAG_NAME, constants.TD)


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getCountries(self):
        table = self.browser.find_element(*self.TBODY)
        first_row = table.find_element(*self.TR)
        countries = first_row.find_elements(*self.TD)
        
        return countries[1:]

    # TODO: add screenshot directive for the failing test
