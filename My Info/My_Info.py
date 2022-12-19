import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

username="Admin"
password="admin123"
url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class test_MyInfo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_Edit_employee_ID_information(self):
        # steps
        browser = self.browser #open web browser (chrome)
        browser.get(url) # open website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys(username) # fill username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys(password) # fill password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # click log in button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[6]/a").click() # go to My Info Menu
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/input").click() # click on the Employee ID Field
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/input").send_keys(Keys.CONTROL + "a") # update Employee ID Data (select All Data)
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/input").send_keys("0023") # update Employee ID Data
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/input").send_keys(Keys.PAGE_DOWN) # Page Down to Find Save Button
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # click save button
        time.sleep(7)




        # validasi
        response_message = browser.find_element(By.XPATH,"//label[contains(text(),'Employee Id')]").text

        self.assertIn('Employee Id', response_message)

    def test_b_Edit_my_name_with_existed_Employee_Name(self):
        # steps
        browser = self.browser #open web browser (chrome)
        browser.get(url) # open website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys(username) # fill username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys(password) # fill password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # click log in button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[6]/a").click() # go to My Info Menu
        time.sleep(3)

        browser.find_element(By.XPATH,"/html//input[@name='firstName']").click() # click on the Employee First Name Field
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='firstName']").send_keys(Keys.CONTROL + "a") # update Employee First Name Data (select All Data)
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='firstName']").send_keys("Dominic") # update Employee First Name Data



        browser.find_element(By.XPATH,"/html//input[@name='lastName']").click() # click on the Employee Last Name Field
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='lastName']").send_keys(Keys.CONTROL + "a") # update Employee Last Name Data (select All Data)
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='lastName']").send_keys("Chase") # update Employee Last Name Data

        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div/div/div/div[2]/input").send_keys(Keys.PAGE_DOWN) # Page Down to Find Save Button
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # click save button
        time.sleep(7)




        # validasi
        response_message = browser.find_element(By.XPATH,"//label[contains(text(),'Employee Full Name')]").text

        self.assertIn('Employee Full Name', response_message)


    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()