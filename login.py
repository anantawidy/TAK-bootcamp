import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locator import elem
from data import acc

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login_with_checklist_remember(self):
        driver = self.driver
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_login).click()
        driver.find_element(By.CSS_SELECTOR, elem.email).send_keys(acc.email)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.check_remember).click()
        driver.find_element(By.CSS_SELECTOR, elem.btn_login).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/login")

    def test_success_login_without_checklist_remember(self):
        driver = self.driver
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_login).click()
        driver.find_element(By.CSS_SELECTOR, elem.email).send_keys(acc.email)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_login).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/login")

    def test_failed_login_empty_email(self):
        driver = self.driver
        url = driver.current_url
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_login).click()
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(acc.password)
        driver.find_element(By.CSS_SELECTOR, elem.btn_login).click()
        data = driver.find_element(By.CLASS_NAME, 'message-error').text
        self.assertIn(data, "Login was unsuccessful. Please correct the errors and try again.")

    def test_failed_login_empty_password(self):
        driver = self.driver
        url = driver.current_url
        driver.get(acc.url)
        driver.find_element(By.CSS_SELECTOR, elem.click_login).click()
        driver.find_element(By.CSS_SELECTOR, elem.email).send_keys(acc.email)
        driver.find_element(By.CSS_SELECTOR, elem.btn_login).click()
        data = driver.find_element(By.CLASS_NAME, 'message-error').text
        self.assertIn(data, "Login was unsuccessful. Please correct the errors and try again.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()