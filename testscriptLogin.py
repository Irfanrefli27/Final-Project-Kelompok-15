from bdb import effective
import orangehrmlive
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def login_success():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.loginSuccess(driver)

def invalid_username():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.invalidUsername(driver)

def invalid_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.invalidPassword(driver)

def empty_username():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.emptyUsername(driver)

def empty_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.emptyPassword(driver)

def empty_username_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.emptyUsernamePassword(driver)

def forget_password():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(10)
    orangehrmlive.forgotPassword(driver)

if __name__ == '__main__':
    login_success()
    invalid_username()
    invalid_password()
    empty_username()
    empty_password()
    empty_username_password()
    forget_password()
