import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class pimTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # LOGIN TEST CASE
    def employeeName(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(2)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(2)
        # Employee Name
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Ab')
        time.sleep(4)

    def employeeId(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(2)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(2)
        # Employee ID
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('0299')
        time.sleep(2)

    def employmentStatus(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(2)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(2)
        # Employee Status
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]')
        time.sleep(2)

    def includeTest(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'username').send_keys('Admin')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        time.sleep(2)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(2)
        # Include
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i').click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()



    #buatcomit
