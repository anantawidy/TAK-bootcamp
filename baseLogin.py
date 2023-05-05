from selenium.webdriver.common.by import By
from locator import elem
from data import acc

def testLogin(driver):
    driver.get(acc.url)
    driver.find_element(By.CSS_SELECTOR, elem.click_login).click()
    driver.find_element(By.CSS_SELECTOR, elem.email).send_keys(acc.email)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(acc.password)
    driver.find_element(By.CSS_SELECTOR, elem.btn_login).click()