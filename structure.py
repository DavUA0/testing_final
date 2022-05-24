from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from home import HomePage
import constants


class StructurePage:
    URL = constants.BASE_URL_STRUCT
    DEPS = (By.XPATH, constants.STRUCT_DEP_SELECTOR)

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getDeps(self):
        deps = self.browser.find_elements(*self.DEPS)

        return deps
