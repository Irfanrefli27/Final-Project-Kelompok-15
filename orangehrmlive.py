from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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
    driver.get_screenshot_as_file("LoginPage.png")
    btnLogin.click()
    time.sleep(10)

def actionSearchAdmin(driver):
    #setUp
    menuAdmin = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']")
    menuAdmin.click()
    drbdnUserRole = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]")
    drbdnUserRole.click()
    time.sleep(20)