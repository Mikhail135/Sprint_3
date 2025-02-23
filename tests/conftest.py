import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver
@pytest.fixture
def name():
    name = 'Mikhail'
    return name

@pytest.fixture
def email():
    email = 'Mikhail_18@gmail.com'
    return email

@pytest.fixture
def password():
    password = '123456'
    return password


