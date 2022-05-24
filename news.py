from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from home import HomePage
import constants


class MilNewsPage:
    URL = constants.BASE_URL_NEWS

    NAVIGATORS = (By.CLASS_NAME, constants.NEWS_NAV)
    TAGS = (By.CLASS_NAME, constants.NEWS_TAGS)
    BADGES = (By.XPATH, constants.NEWS_BADGES)
    H5 = (By.TAG_NAME, constants.H5)
    HOME_NAV_BAR = (By.ID, constants.HOME_NAV_BAR)
    ANCHS = (By.TAG_NAME, constants.ANCH)

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        home = HomePage(self.browser)
        home.load()
        news_url = home.browser.find_element(*self.HOME_NAV_BAR).find_elements(*self.ANCHS)[4].get_attribute('href')
        home.load(news_url)
        

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
