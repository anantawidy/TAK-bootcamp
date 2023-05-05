import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from locator import elem
from data import acc

class Register(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_register(self):
        driver = self.driver
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("Ananta")
        driver.find_element(By.CSS_SELECTOR, elem.lastname).send_keys("Widy")
        driver.find_element(By.CSS_SELECTOR, elem.email_regist).send_keys("997979@gmail.com")
        driver.find_element(By.CSS_SELECTOR, elem.password_regist).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirm_password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_success_register_without_choose_gender(self):
        driver = self.driver
        
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'FirstName').send_keys("Ananta")
        driver.find_element(By.CSS_SELECTOR, elem.lastname).send_keys("Widy")
        driver.find_element(By.CSS_SELECTOR, elem.email_regist).send_keys("778979@gmail.com")
        driver.find_element(By.CSS_SELECTOR, elem.password_regist).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirm_password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_failed_register_empty_firstname(self):
        driver = self.driver
        url = driver.current_url
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.CSS_SELECTOR, elem.lastname).send_keys("Widy")
        driver.find_element(By.CSS_SELECTOR, elem.email_regist).send_keys("15475@gmail.com")
        driver.find_element(By.CSS_SELECTOR, elem.password_regist).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirm_password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        data = driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn(data, "First name is required.")

    def test_failed_register_empty_lastname(self):
        driver = self.driver
        
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("Ananta")
        driver.find_element(By.CSS_SELECTOR, elem.email_regist).send_keys("15475@gmail.com")
        driver.find_element(By.CSS_SELECTOR, elem.password_regist).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirm_password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        data = driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn(data, "Last name is required.")

    def test_failed_register_empty_email(self):
        driver = self.driver
        
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("Ananta")
        driver.find_element(By.CSS_SELECTOR, elem.lastname).send_keys("Widy")
        driver.find_element(By.CSS_SELECTOR, elem.password_regist).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirm_password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        data = driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn(data, "Email is required.")   

    def test_failed_register_empty_password(self):
        driver = self.driver
        
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_register).click()
        driver.find_element(By.ID, 'gender-male').click()
        driver.find_element(By.ID, 'FirstName').send_keys("Ananta")
        driver.find_element(By.CSS_SELECTOR, elem.lastname).send_keys("Widy")
        driver.find_element(By.CSS_SELECTOR, elem.email_regist).send_keys("15475@gmail.com")
        driver.find_element(By.CSS_SELECTOR, elem.btn_register).click()
        data = driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn(data, "Password is required.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()