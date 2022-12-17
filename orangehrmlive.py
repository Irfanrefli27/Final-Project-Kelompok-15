from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import time

def actionLogin(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("Admin")
    password.send_keys("admin123")
    btnLogin.click()
    time.sleep(5)
    driver.get_screenshot_as_file("InvalidPassword.png")
    time.sleep(10)

def actionLogout(driver):
    #setUp
    btnProfile = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//header[@class='oxd-topbar']//div[@class='oxd-topbar-header-userarea']/ul/li//p[@class='oxd-userdropdown-name']")
    btnProfile.click()
    btnLogin = driver.find_element(By.LINK_TEXT, "Logout")
    #Call
    btnLogin.click()
    time.sleep(5)
    driver.get_screenshot_as_file("InvalidPassword.png")
    time.sleep(10)

def emptyUsername(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("")
    password.send_keys("admin123")
    btnLogin.click()
    time.sleep(5)
    driver.get_screenshot_as_file("EmptyUsername.png")
    time.sleep(10)


