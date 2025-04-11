import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

file_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
url = "https://parabank.parasoft.com/parabank/index.htm"


def test01():
    service = Service(file_path)
    driver = webdriver.Chrome(service=service)
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
    about_us_link.click()
    time.sleep(1)
    print(driver.title)
    time.sleep(1)
    driver.quit()