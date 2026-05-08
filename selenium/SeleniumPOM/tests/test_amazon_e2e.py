
import time
import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


@pytest.mark.parametrize(("search_product","brandname","mensize"),[
    ("shoes","Nike","9")

])

def test_search_product(driver,search_product,brandname,mensize):
    homepage = HomePage(driver)

    homepage.type_search_input(search_product)
    print(f"Searching product -{search_product}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search Result page did not load'
    print(f" Search Result is loaded successfully-{search_product}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter did not apply properly'