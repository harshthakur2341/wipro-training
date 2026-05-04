import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import find_connectable_ip
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.relative_locator import locate_with

driver= webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

#driver.get("https://www.google.com")
#driver.get("https://the-internet.herokuapp.com/tables")

#And or Or
'''and_example = driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
print(f"AND example : {and_example.text}")

or_example = driver.find_element(By.XPATH,)'''



#ID
'''search_input = driver.find_element(By.ID,"APjFqb" )
search_input.send_keys("selenium")
time.sleep(3)
search_input.clear()'''


#name
'''search_input = driver.find_element(By.NAME,'q')
search_input.send_keys("loctors")
time.sleep(10)
'''
#name
'''googlesearch_button = driver.find_element(By.NAME,'btnK')
googlesearch_button.click()
time.sleep(30)'''

#classname
'''infl_button = driver.find_element(By.CLASS_NAME,"RNmpXc")
infl_button.click()
time.sleep(3)'''

#tagname
'''href_elements = driver.find_elements(By.TAG_NAME,"a")
for elnt in href_elements:
    print(f'{elnt.text} - {elnt.get_attribute("href")}')'''

#linktext
'''images_link = driver.find_element(By.LINK_TEXT,"Images")
images_link.click()
time.sleep(10)'''

#Partial
'''images_link = driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
images_link.click()
time.sleep(10)'''

#CSSSel
'''search_input = driver.find_element(By.CSS_SELECTOR,'div > textarea')
search_input.send_keys('Selenium')
time.sleep(5)'''

#Xpath
'''setting_text = driver.find_element(By.XPATH,'/html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div')
print(setting_text.text)
time.sleep(5)'''

'''#child
rows = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
print(f"Child example -> Found {len(rows)} colums in the first table.")

#Parents-Get the parent row of a particular
email_cell = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']")
parent_row = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
print(f"parents exam- email '{email_cell.text}' belongs to row with first name: "
      f"{parent_row.find_element(By.XPATH,'./td[2]').text}")


#ancestor-get the table element that is an ancestor of a cell
ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
print(f" Ancestor Example -- Table Id: {ancestor_table.get_attribute('id')}")

#descendants
descendants= driver.find_elements(By.XPATH,"//table[@id='table1']/descendant::td")
print(f" descendants Example -- Found {len(descendants)} descendants cells.")'''




driver.get("https://www.saucedemo.com/")
time.sleep(5)

#elements for reference
username_field=driver.find_element(By.ID,"user-name")
password_field=driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")

#above
elmt_above_password = driver.find_element(locate_with(By.TAG_NAME,"input").above(password_field))

print(f"Above Eample -- txt above password: {elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(5)


#below
field_below_username = driver.find_element(locate_with(By.TAG_NAME,"input").below(username_field))

print(f"Below Example -- Placeholder below username: {field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys('secret_sauce')
time.sleep(5)
login_button.click()
time.sleep(5)

#right of
twitter_icon = driver.find_element(By.LINK_TEXT,"Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_right_of(twitter_icon))
print(f"toRightOf example--twitter href:{facebook_icon.get_attribute('href')} ")

#left of
left_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_left_of(facebook_icon))
print(f"toLeftof example -- facebook href:{left_icon.get_attribute('href')}")

#near
near_twitter = driver.find_elements(locate_with(By.TAG_NAME,"a").near(facebook_icon))
for element in near_twitter:
    print(f" Near example {element.get_attribute('href')}")

time.sleep(3)




driver.quit