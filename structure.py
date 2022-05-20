from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url_struct = 'https://mil.am/en/structures/12'

class StructurePage:
    URL = base_url_struct
    DEPS = (By.XPATH, "//div[@class='col-xs-12 col-sm-6']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getDeps(self):
        deps = self.browser.find_elements(*self.DEPS)

        return deps
