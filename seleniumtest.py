import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    browser.get("http://localhost/login.php")
    browser.find_element(By.NAME, "Username").send_keys("isotope")
    browser.find_element(By.NAME, "Password").send_keys("1s0t0p3")
    browser.find_element(By.NAME, "Submit").click()
    assert "index.php" in browser.current_url
def test_login_fail():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)
    browser.get("http://localhost/login.php")
    browser.find_element(By.NAME, "Username").send_keys("isotope")
    browser.find_element(By.NAME, "Password").send_keys("2s0t0p3")
    browser.find_element(By.NAME, "Submit").click()
    assert "login.php" in browser.current_url
