import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from peacekeep import PeacekeepPage

@pytest.fixture
def setup_object():
    serv = Service('./chromedriver')
    driver = webdriver.Chrome(service=serv)

    peacekeep = PeacekeepPage(driver)
    peacekeep.load()

    return peacekeep


def test_countries(setup_object):
    peacekeep = setup_object
    countries = peacekeep.getCountries()

    #check whether the countries correspond to the ones mandated by the country's foreign policy, the last one will fail

    assert countries[0].text == 'Աֆղանստան'
    assert countries[1].text == 'Կոսովո'
    assert countries[2].text == 'Լիբանան'
