"""
homepage error
"""
from time import sleep


from selenium import webdriver
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('What broswer do you want ? ')

match(browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))

    case 'edge':
        driver = webdriver.Edge(service= Service('../resources/msedgedriver.exe'))

    case _:
        print('unknown broswer - not avaiable ')
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))










driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print('Pass')
else:
    print('Fail')



sleep(10)
driver.quit()

