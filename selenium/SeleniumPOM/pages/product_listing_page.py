import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR,"a h2 span")
       #nput[@type='checkbox']")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def first_product_title(self):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\n First Product:",first_product)


    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles on page one .\n")

        for i ,title in enumerate(product_titles[:5],start = 1):
            print(f"{i},{title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(self,brandname):
        BRAND_FILTER = (By.XPATH, "//span[text()='" + brandname + "']/parent::a/descendant::i")

        return BRAND_FILTER



    def select_brand_filter(self,brandname):
        brand_filter = self.driver.find_element(*self.brand_filter_locator(brandname))
        brand_filter.click()


    def check_product_titles_for_brand_filter(self,brandname):

        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))

        for title in product_titles:
            print("title:",title.text)
            if not title.text.__contains__(brandname):
                return False
        return True

    def mensize_locator(self,mensize):
        MENSIZE_FILTER = (By.XPATH,"")