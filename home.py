from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import constants


class HomePage:
    URL = constants.BASE_URL_HOME
    CENTER = (By.CLASS_NAME, constants.HOME_CNTR)
    H3 = (By.TAG_NAME, constants.H3)
    NAV_LANG_ID = (By.ID, constants.HOME_NAV)
    ANCH = (By.TAG_NAME, constants.ANCH)


    def __init__(self, browser):
        self.browser = browser

    def load(self, url=None):
        if url is None:
            url = self.URL
        self.browser.get(url)

    def getLang(self):
        centerh = self.browser.find_elements(*self.CENTER)
        h3 = centerh[0].find_element(*self.H3)
        
        return h3.text

    def changeLang(self, lang):
        nav_lang = self.browser.find_element(*self.NAV_LANG_ID)

        if lang == 'en':
            self.browser.get(nav_lang.find_elements(*self.ANCH)[1].get_attribute('href'))
        elif lang == 'ru':
            self.browser.get(nav_lang.find_elements(*self.ANCH)[2].get_attribute('href'))
