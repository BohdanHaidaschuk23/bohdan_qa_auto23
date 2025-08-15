import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.mark.ui
def test_check_incorrect_name():
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    login_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field")))
    pass_elem = driver.find_element(By.ID, "password")
    login_elem.send_keys("bohdanhaidashchyk@gmail.com")
    pass_elem.send_keys("wrongpassword")
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()
    WebDriverWait(driver, 10).until(
        EC.title_contains("Sign in to GitHub"))
    assert driver.title == "Sign in to GitHub · GitHub"
    driver.close()