import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check

#from selenium_basics.google_homepage_test import pagetitle


#from selenium_basics.google_homepage_test import pagetitle


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google','Google Home Page Not loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images','Images Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait = WebDriverWait(driver,10)
    wait.until(EC.title_contains('Business'))

    check.equal(driver.title,'Business','Business Page Is not Loaded-title')
    check.is_in('business',driver.current_url,'Business Page Is not Loaded-URL')
    #assert 'Business' in driver.title,'Business Page Is not Loaded-title'
    #assert 'business' in driver.current_url,'Business Page Is not Loaded-URL'




