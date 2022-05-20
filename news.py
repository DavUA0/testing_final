from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url_news = 'https://mil.am/en/news'

class MilNewsPage:
    URL = base_url_news

    NAVIGATORS = (By.CLASS_NAME, 'breadcrumb')
    TAGS = (By.CLASS_NAME, 'main-tag')
    BADGES = (By.XPATH, "//div[@class='badge-top green']")
    H5 = (By.TAG_NAME, 'h5')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def getNavigatorNames(self):
        navigators = self.browser.find_element(*self.NAVIGATORS)
        return navigators

    def getFirstHashtagName(self):
        hashtags = self.browser.find_elements(*self.TAGS)
        return hashtags[0].text

    def getBadges(self):
        hashtags = self.browser.find_elements(*self.TAGS)
        hashtags[0].click()
        badges = self.browser.find_elements(*self.BADGES)
        return badges

    def getHeader(self):
        hashtags = self.browser.find_elements(*self.TAGS)
        hashtags[0].click()
        header = self.browser.find_element(*self.H5)
        return header
