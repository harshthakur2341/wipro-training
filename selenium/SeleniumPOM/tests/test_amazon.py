import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url,'URL is not Correct'
    print("\n Opened Amazon homepage")


@pytest.mark.parametrize("search_product",[
    ("wireless mouse"),("shoes")

])
def test_search_product(driver,search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Searching product -{search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search Result page did not load'
    print(f" Search Result is loaded successfully-{search_product}")


@pytest.mark.parametrize("search_product",[
    ("wireless mouse"),("shoes")

])
def test_find_elements_amazon(driver,search_product):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Searching product -{search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search Result page did not load'
    print(f" Search Result is loaded successfully-{search_product}")


    productlistingpage = ProductListingPage(driver)

    productlistingpage.first_product_title()
    val = productlistingpage.all_products()

    assert val , "No products found in Amazon search results"

@pytest.mark.parametrize(("search_product","brand_filter"),[
    ("wireless mouse",'Logitech'),("shoes","Nike")

])

def test_brand_filter(driver,search_product,brand_filter):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Searching product -{search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search Result page did not load'
    print(f" Search Result is loaded successfully-{search_product}")


    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brand_filter)

    assert productlistingpage.check_product_titles_for_brand_filter(brand_filter),'Brand filter did not apply properly'
