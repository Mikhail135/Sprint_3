from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
from data import Data
class TestLogin:
    def test_log_in_button_through_your_personal_account(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')))
        assert "Соберите бургер" in driver.page_source


    def test_log_in_button_through_log_in_to_your_account(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.LOG_IN).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')))
        assert "Соберите бургер" in driver.page_source

    def test_log_in_reg_form(self, driver):
        driver.get(Data.SITE_REG)
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//a[@href="/login"]')))
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')))
        assert "Соберите бургер" in driver.page_source

    def test_log_in_through_forgot_password(self, driver):
        driver.get(Data.SITE_FORGOT_PASSWORD)
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//a[@href="/login"]')))
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')))
        assert "Соберите бургер" in driver.page_source


