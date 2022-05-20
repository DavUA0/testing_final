import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from structure import StructurePage

@pytest.fixture
def setup_object():
    serv = Service('./chromedriver')
    driver = webdriver.Chrome(service=serv)

    structure = StructurePage(driver)
    structure.load()

    return structure


def test_dep_count(setup_object):
    structure = setup_object
    count = len(structure.getDeps())

    # check if the number of departments is correct
    assert count == 19
