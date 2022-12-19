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


class test_performance(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_go_to_performance_page(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get(url) # open website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys(username) # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys(password) # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(5)


    def test_b_Change_the_Original_URL_to_the_wrong_URL(self): 
        # steps
        browser = self.browser #buka web browser (chrome)
        browser.get(url) # open website
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@name='username']").send_keys(username) # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@name='password']").send_keys(password) # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(1)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/") 
        time.sleep(2)
        browser.refresh
        time.sleep(2)
        browser.back
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[6]/a/span").click() # click on My Info menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click again to performance menu
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/") 
        time.sleep(2)
        browser.refresh
        time.sleep(2)
        browser.back
        time.sleep(2)
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview") 
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[6]/a/span").click() # click on My Info menu
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click again to performance menu
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").text

        self.assertIn('Performance', response_message)


    def test_c_Search_for_existing_KPIs(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(5)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/div[2]/i").click() # click on Dropdown Job Title List
        time.sleep(3)
        # Get Dropdown AJAX Data
        num_times = 13

        for i in range(num_times):
                # Use the send_keys method to send the "dpad down" key
                browser.find_element(By.XPATH, "//span[text()='IT Manager']").click()
                time.sleep(7)

                browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]").click() # click on search button
                time.sleep(10)


        # validasi
        response_message = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text

        self.assertIn('Records Found', response_message)


    def test_d_Search__KPIs_that_do_not_exist(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(5)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div[2]/div/div/div[2]/i").click() # click on Dropdown Job Title List
        time.sleep(3)

        # Get Dropdown AJAX Data
        browser.find_element(By.XPATH, "//span[text()='Account Assistant']").click() 
        time.sleep(5)
        
        browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]").click() # click on search button
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div/div/div/label").text

        self.assertIn('Job Title', response_message)


    def test_e_add_new_KPI(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]").click() # click on Add New KPIs button
        time.sleep(3)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("New Tests Growth Percentage") # Insert Key Performance Indicator
        time.sleep(3)
        
        
        # Get Dropdown AJAX Data for Job List
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click() # click on KPIs Dropdown Job Title List
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[text()='Automation Tester']").click() # choose on KPIs Dropdown Job Title List
        time.sleep(5)
        
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]").click() # click on Minimum Rating Field
        time.sleep(3)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(Keys.CONTROL + "a") # update Minimum Rating Data (select All Data)
        time.sleep(3)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("0") # Insert Minimum Rating
        time.sleep(3)

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").click() # click on Maximum Rating Field
        time.sleep(3)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys(Keys.CONTROL + "a") # update Maximum Rating Data (select All Data)
        time.sleep(3)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("100") # Insert Maximum Rating
        time.sleep(3)

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]").click() # click save button
        time.sleep(10)

        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)



        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/i[1]").click() # click on sort button
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/span[1]").click() # click on Ascending sort button
        time.sleep(5)



        # validasi
        assert "https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchKpi" in browser.current_url

    def test_f_Create_New_but_with_no_input_value_in_required_field_textbox(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]").click() # click on Add New KPIs button
        time.sleep(3)
        
        
        # Get Dropdown AJAX Data for Job List
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]").click() # click on KPIs Dropdown Job Title List
        time.sleep(3)
        browser.find_element(By.XPATH, "//span[text()='Automation Tester']").click() # choose on KPIs Dropdown Job Title List
        time.sleep(5)
        

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]").click() # click save button
        time.sleep(15)


        # validasi
        response_message = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/span[1]").text

        self.assertIn('Required', response_message)


    def test_g_Delete_Configure_KPI(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(10)

        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)



        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/i[1]").click() # click on sort button
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/span[1]").click() # click on Ascending sort button
        time.sleep(5)

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]").click() # click on Checkbox
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/button[2]/i[1]").click() # click delete button
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]").click() # click on " Yes, Delete " button
        time.sleep(10)


        # validasi
        response_message = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text

        self.assertIn('Records Found', response_message)


    def test_h_Delete_Configure_KPI_with_selecting_multiple(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(10)

        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)



        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/i[1]").click() # click on sort button
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/span[1]").click() # click on Ascending sort button
        time.sleep(5)

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]").click() # click on Checkbox 1
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]").click() # click on Checkbox 2
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click() # click delete for multiple checkbox
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]").click() # click on " Yes, Delete " button
        time.sleep(10)


        # validasi
        response_message = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text

        self.assertIn('Records Found', response_message)


    def test_i_Delete_Configure_KPI_Without_Checked_Data(self): 
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
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[7]/a/span").click() # click on performance menu
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/span").click() # click on configure button
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li/ul/li").click() # click on KPIs
        time.sleep(10)

        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.ARROW_DOWN) # Page Down to find data
        time.sleep(1)



        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/i[1]").click() # click on sort button
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/span[1]").click() # click on Ascending sort button
        time.sleep(5)

        browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/button[2]/i[1]").click() # click delete button without do check on the data on the checkbox
        time.sleep(5)
        browser.find_element(By.XPATH,"//body/div[@id='app']/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]").click() # click on " Yes, Delete " button
        time.sleep(10)


        # validasi
        response_message = browser.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text

        self.assertIn('Records Found', response_message)



    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()