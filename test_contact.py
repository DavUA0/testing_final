import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from contacts import ContactPage

@pytest.fixture
def setup_object():
    serv = Service('./chromedriver')
    driver = webdriver.Chrome(service=serv)

    contact = ContactPage(driver)
    contact.load()

    return contact


def test_numbers(setup_object):
    contact = setup_object
    short_n, long_n = contact.getHotlineNumbers()

    # check if the hotline numbers match
    assert short_n == '1-28'
    assert long_n == '(+37412) 21-00-00'

def test_email(setup_object):
    contact = setup_object
    email = contact.getEmail()

    # check whether the contact email is correct
    assert email == 'modpress@mil.am'
