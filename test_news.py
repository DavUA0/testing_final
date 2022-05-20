import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from news import MilNewsPage

@pytest.fixture
def setup_object():
    serv = Service('./chromedriver')
    driver = webdriver.Chrome(service=serv)

    news_page = MilNewsPage(driver)
    news_page.load()

    return news_page


def test_navigator(setup_object):
    news_page = setup_object

    # check the upper navigators to make sure we are on the news page
    assert news_page.getNavigatorNames().text == "Home News"

def test_first_tag_header(setup_object):
    news_page = setup_object

    hashtag_name = news_page.getFirstHashtagName()
    header = news_page.getHeader()
    
    # check whether the tag corresponds to the one clicked initially
    assert hashtag_name == header.text

def test_first_tag_badges(setup_object):
    news_page = setup_object

    hashtag_name = news_page.getFirstHashtagName()
    badges = news_page.getBadges()

    # check whether the hashtags match the one clicked initially
    for badge in badges:
        assert hashtag_name == badge.text
