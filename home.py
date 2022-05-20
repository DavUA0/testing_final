from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url_home = 'https://mil.am/'

class HomePage:
    URL = base_url_home
    CENTER = (By.CLASS_NAME, 'center-header')
    H3 = (By.TAG_NAME, 'h3')
    NAV_LANG_ID = (By.ID, 'cd-navigation-lang')
    ANCH = (By.TAG_NAME, 'a')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

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
