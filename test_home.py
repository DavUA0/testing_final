import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from home import HomePage

@pytest.fixture
def setup_object():
    serv = Service('./chromedriver')
    driver = webdriver.Chrome(service=serv)

    home = HomePage(driver)
    home.load()

    return home


def test_default_armenian(setup_object):
    home = setup_object
    lang = home.getLang()

    # check if the default home page is in Armenian
    assert lang == 'ԼՈՒՐԵՐ'

def test_lang_change(setup_object):
    home = setup_object

    # check whether language changes work as expected

    home.changeLang('en')
    lang = home.getLang()
    assert lang == 'NEWS'

    home.changeLang('ru')
    lang = home.getLang()
    assert lang == 'НОВОСТИ'
