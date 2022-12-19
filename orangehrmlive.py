from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import time
from selenium.webdriver.support.ui import Select

def loginSuccess(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("Admin")
    password.send_keys("admin123")
    btnLogin.click()
    time.sleep(10)
    driver.get_screenshot_as_file("SuccessLogin.png")
    time.sleep(10)

def invalidUsername(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("Admin@gmail.com")
    password.send_keys("admin123")
    btnLogin.click()
    time.sleep(10)
    driver.get_screenshot_as_file("InvalidUsername.png")
    time.sleep(10)

def invalidPassword(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("Admin")
    password.send_keys("qwertyuiop")
    btnLogin.click()
    time.sleep(10)
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

def emptyPassword(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("Admin")
    password.send_keys("")
    btnLogin.click()
    time.sleep(5)
    driver.get_screenshot_as_file("EmptyPassword.png")
    time.sleep(10)

def emptyUsernamePassword(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
   
    #Call
    username.send_keys("")
    password.send_keys("")
    btnLogin.click()
    time.sleep(5)
    driver.get_screenshot_as_file("EmptyUsernamePassword.png")
    time.sleep(10)

def forgotPassword(driver):
    #setUp
    btnForgetPass = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']/div[@class='orangehrm-login-container']//form[@action='/web/index.php/auth/validate']//p[.='Forgot your password? ']")

    #Call
    btnForgetPass.click()
    time.sleep(10)
    username = driver.find_element(By.XPATH, "//div[@id='app']//form[@action='/web/index.php/auth/requestResetPassword']/div[@class='oxd-form-row']/div//input[@name='username']")
    username.send_keys("Admin")
    btnResetPass = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-forgot-password-container']//form[@action='/web/index.php/auth/requestResetPassword']//button[@type='submit']")
    btnResetPass.click()
    time.sleep(10)
    driver.get_screenshot_as_file("ForgotPassword.png")
    time.sleep(5)

def searchValidAdmin(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/input")
    username.send_keys("Admin")
    time.sleep(5)
    # find_employee_status = \
    # drbdnUserRole = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]")
    # drbdnUserRole.click()
    # time.sleep(10)
    # select_employee_status = Select(find_employee_status)
    # select_employee_status.select_by_visible_text("Admin")
    # time.sleep(10)
    btnUserRole = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]/div/div[2]/div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']")
    btnUserRole.click()
    time.sleep(10)
    selectUserRole = driver.find_element(By.LINK_TEXT, "data-v-15ec1d6f")
    selectUserRole.click()
    time.sleep(10)
    
    # btnSearch = driver.find_element(By.XPATH , "//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']")
    # btnSearch.click()
    # time.sleep(5)

def searchUsernameOnly(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/input")
    username.send_keys("Admin")
    time.sleep(5)
    btnSearch = driver.find_element(By.XPATH , "//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']")
    btnSearch.click()
    time.sleep(5)
    driver.get_screenshot_as_file("SearchUsernameOnly.png")
    time.sleep(5)

def searchEmployeeNameOnly(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    employeeName = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']")
    employeeName.send_keys("sa")
    time.sleep(5)
    selectEmployeeName = driver.find_element(By.CLASS_NAME, "oxd-autocomplete-option")
    selectEmployeeName.click()
    time.sleep(5)
    btnSearch = driver.find_element(By.XPATH , "//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']")
    btnSearch.click()
    time.sleep(5)
    driver.get_screenshot_as_file("SearchEmployeeNameOnly.png")
    time.sleep(5)

def resetButton(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/input")
    username.send_keys("Admin")
    time.sleep(5)
    rstButton = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']//button[@type='button']")
    rstButton.click()
    time.sleep(5)
    driver.get_screenshot_as_file("resetButton.png")
    time.sleep(5)

def searchNotRegisteredUsername(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    username = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[1]/div/div[2]/input")
    username.send_keys("qwerty")
    time.sleep(5)
    btnSearch = driver.find_element(By.XPATH , "//div[@id='app']/div[@class='oxd-layout']//div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']")
    btnSearch.click()
    time.sleep(5)
    driver.get_screenshot_as_file("SearchNotRegisteredUsername.png")
    time.sleep(5)

def addNewAdminWithRegisteredEmployee(driver):
    loginSuccess(driver)
    adminMenu = driver.find_element(By.CLASS_NAME, "oxd-main-menu-item")
    adminMenu.click()
    time.sleep(5)
    btnAdd = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']")
    btnAdd.click()
    time.sleep(5)
