from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from home import HomePage
import constants


class ContactPage:
    H4 = (By.TAG_NAME, constants.H4)
    ANCH = (By.TAG_NAME, constants.ANCH)
    CONTACTS_DIV = (By.CLASS_NAME, constants.CONT_DIV_SELECTOR)
    MAIL_ANCH = (By.XPATH, constants.CONT_MAIL_ANCH)

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        home = HomePage(self.browser)
        home.load()
        contacts = home.browser.find_element(By.CLASS_NAME, 'footer-links-map').find_elements(*self.ANCH)[0]
        contacts.click()

    def getHotlineNumbers(self):
        h4 = self.browser.find_element(*self.H4)
        anchors = h4.find_elements(*self.ANCH)

        return anchors[0].text,anchors[1].text

    def getEmail(self):
        contsDiv = self.browser.find_element(*self.CONTACTS_DIV)
        mail_anchor = self.browser.find_element(*self.MAIL_ANCH)

        return mail_anchor.text
