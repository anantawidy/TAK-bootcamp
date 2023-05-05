import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from locator import elem
from data import acc
import baseLogin
import time

class Checkout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_add_to_cart_choose_category_first(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.ID, "add-to-cart-button-45").click()
        time.sleep(2)
        data = driver.find_element(By.CLASS_NAME, 'content').text
        self.assertIn(data, "The product has been added to your shopping cart")

    def test_success_send_to_friend_with_messsage(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.CLASS_NAME, "email-a-friend").click()
        driver.find_element(By.ID, "FriendEmail").send_keys("alfath@gmail.com")
        driver.find_element(By.ID, "PersonalMessage").send_keys("Hi, thanks you for to be my best frirend")
        driver.find_element(By.XPATH, elem.send_email).click()
        data = driver.find_element(By.XPATH, elem.result_send_message).text
        self.assertIn(data, "Fiction")

    def test_success_send_to_friend_without_messsage(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.CLASS_NAME, "email-a-friend").click()
        driver.find_element(By.ID, "FriendEmail").send_keys("alfath@gmail.com")
        driver.find_element(By.XPATH, elem.send_email).click()
        data = driver.find_element(By.XPATH, elem.result_send_message).text
        self.assertIn(data, "Fiction")

    def test_failed_send_to_friend_without_fill_email(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.CLASS_NAME, "email-a-friend").click()
        driver.find_element(By.XPATH, elem.send_email).click()
        data = driver.find_element(By.XPATH, elem.error_no_email).text
        self.assertIn(data, "Enter friend's email")

    def test_failed_send_to_friend_input_invalid_email(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.CLASS_NAME, "email-a-friend").click()
        driver.find_element(By.XPATH, elem.send_email).click()
        data = driver.find_element(By.XPATH, elem.error_no_email).text
        self.assertIn(data, "Wrong email")

    def test_success_compare(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.XPATH, elem.compare_list).click()
        driver.find_element(By.XPATH, elem.btn_remove_compare).click()
        data = driver.find_element(By.XPATH, elem.remove_compare).text
        self.assertIn(data, "Compare products")

    def test_success_remove_cart(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.ID, "add-to-cart-button-45").click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btn_shopping_cart).click()
        driver.find_element(By.XPATH, elem.btn_checklist_cart).click()
        driver.find_element(By.XPATH, elem.btn_update_cart).click()
        data = driver.find_element(By.XPATH, elem.success_remove_cart).text
        self.assertIn(data, "Shopping cart\nYour Shopping Cart is empty!")

    def test_success_check_shipping(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.ID, "add-to-cart-button-45").click()
        driver.find_element(By.XPATH, elem.btn_shopping_cart).click()
        select = Select(driver.find_element(By.ID, 'CountryId'))
        select.select_by_value('42')
        driver.find_element(By.ID, "ZipPostalCode").send_keys("16435")
        driver.find_element(By.XPATH, elem.estimate_shipping).click()
        data = driver.find_element(By.XPATH, elem.success_shipping).text
        self.assertIn(data, "Ground (10.00)")

    def test_success_checkout(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.ID, "add-to-cart-button-45").click()
        driver.find_element(By.XPATH, elem.btn_shopping_cart).click()
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.XPATH, elem.btn_checkout).click()
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/login/checkoutasguest?returnUrl=%2Fcart")
        
    def test_checkout_without_tnc(self):
        driver = self.driver
        baseLogin.testLogin (driver)
        driver.find_element(By.XPATH, elem.book_category).click()
        driver.find_element(By.XPATH, elem.fiction).click()
        driver.find_element(By.ID, "add-to-cart-button-45").click()
        driver.find_element(By.XPATH, elem.btn_shopping_cart).click()
        driver.find_element(By.XPATH, elem.btn_checkout).click()
        data = driver.find_element(By.XPATH, elem.no_tnc).text
        self.assertIn(data, "Terms of service\nclose\nPlease accept the terms of service before the next step.")
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()