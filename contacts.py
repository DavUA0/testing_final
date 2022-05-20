from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url_contact = 'https://mil.am/en/contacts'

class ContactPage:
    URL = base_url_contact

    H4 = (By.TAG_NAME, 'h4')
    ANCH = (By.TAG_NAME, 'a')
    CONTACTS_DIV = (By.CLASS_NAME, 'card-address')
    MAIL_ANCH = (By.XPATH, "//a[contains(@href,'mailto')]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getHotlineNumbers(self):
        h4 = self.browser.find_element(*self.H4)
        anchors = h4.find_elements(*self.ANCH)

        return anchors[0].text,anchors[1].text

    def getEmail(self):
        contsDiv = self.browser.find_element(*self.CONTACTS_DIV)
        mail_anchor = self.browser.find_element(*self.MAIL_ANCH)

        return mail_anchor.text
