from bdb import effective
import orangehrmlive
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def search_valid_admin():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(5)
    orangehrmlive.searchValidAdmin(driver)

def search_username_only():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(5)
    orangehrmlive.searchUsernameOnly(driver)

def search_employee_name_only():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(5)
    orangehrmlive.searchEmployeeNameOnly(driver)

def reset_button():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(5)
    orangehrmlive.resetButton(driver)

def not_registered_username():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver.maximize_window()
    
    driver.get("https://opensource-demo.orangehrmlive.com/ ")
    time.sleep(5)
    orangehrmlive.searchNotRegisteredUsername(driver)

if __name__ == '__main__':
    #search_valid_admin()
    search_username_only()
    search_employee_name_only()
    reset_button()
    not_registered_username()