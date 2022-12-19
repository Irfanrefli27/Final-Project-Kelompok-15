from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.action_chains import ActionChains
import time

def actionLogin(driver):
    #setUp
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    btnLogin = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
    #Call
    username.send_keys("Admin")
    password.send_keys("admin123")
    driver.get_screenshot_as_file("LoginSukses.png")
    btnLogin.click()
    time.sleep(5)

def actionDashboardMenu(driver):
    #Open Assign Leave
    #btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    #btnDashboard.click()
    #time.sleep(3)
    driver.get_screenshot_as_file("Dashboard Menu.png")
    btnAssigLeave = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[1]/button")
    btnAssigLeave.click()
    time.sleep(5)
    driver.get_screenshot_as_file("open assign leave menu.png")
    #Open Leave List
    btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    btnDashboard.click()
    time.sleep(3)
    btnLeaveList = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/button")
    btnLeaveList.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open leave list menu.png")
    #open Timesheets
    btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    btnDashboard.click()
    time.sleep(3)
    btnTimesheets = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]/button")
    btnTimesheets.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open timesheets menu.png")
    #open Apply Leave
    btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    btnDashboard.click()
    time.sleep(3)
    btnApplyLeave = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[4]/button")
    btnApplyLeave.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open apply leave menu.png")
    #open My Leave
    btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    btnDashboard.click()
    time.sleep(3)
    btnMyLeave = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[5]/button")
    btnMyLeave.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open my leave menu.png")
    #open My Timesheets
    btnDashboard = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']")
    btnDashboard.click()
    time.sleep(3)
    btnMyTimesheets = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[6]/button")
    btnMyTimesheets.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open my timesheets menu.png")

def actionDirectoryMenu(driver):
    #Open Directory Menu
    btnDirectory = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/directory/viewDirectory']")
    btnDirectory.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open directory menu.png")
    #Filter By Job Title Filter
    btndrpdnJobFilter = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div")
    btndrpdnJobFilter.click()
    driver.get_screenshot_as_file("open select job title.png")
    time.sleep(1)
    btnvalue = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]")
    btnvalue.click()
    time.sleep(1)
    btnSearch = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    btnSearch.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open search result by job filter.png")
    time.sleep(1)
    #Filter By Job Title Filter
    btnreset = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]")
    btnreset.click
    btnlocation = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div")
    btnlocation.click()
    time.sleep(1)
    btnvaluelocation = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]")
    btnvaluelocation.click()
    btnSearch = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    btnSearch.click()
    time.sleep(3)
    driver.get_screenshot_as_file("open search result by location filter.png")

def actionLogout(driver):
    btnProfile = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//header[@class='oxd-topbar']//div[@class='oxd-topbar-header-userarea']/ul/li[@class='oxd-userdropdown']//p[@class='oxd-userdropdown-name']")
    btnProfile.click()
    btnLogOut = driver.find_element(By.LINK_TEXT, "Logout")
    btnLogOut.click()
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
