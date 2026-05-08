import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    yield driver
    driver.quit()




def test_open_amazon(driver):
    assert "amazon" in driver.current_url,'URL for Amazon is not correct'
    assert "Amazon" in driver.title,'Title for amazon is not correct'
    print("\n Opened Amazon Homepage,title and url verified")


def test_search_product(driver):
    wait = WebDriverWait(driver,5)
    search_box = wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element((By.ID,"nav-search-submit-button"))
    search_button.click()

    assert driver.current_url.__contains__('wireless'),'Search result page did not load'
    assert driver.title.__contains__('wireless'),'Search result page did not load'
    print("\n Search results page loaded successfully")




def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver,15)

    first_product = wait.until(
        EC.visibility_of_element_located(())
    )