from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
from data import Data
class TestSignin:
    def test_registration_with_valid_password(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Xpath.REGISTER_LINK)))
        driver.find_element(By.XPATH, Xpath.REGISTER_LINK).click()
        driver.find_element(By.XPATH, Xpath.NAME_INPUT).send_keys(Data.NAME)
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((
            By.XPATH, Xpath.SUPER_SHORT_LOG_IN)))
        assert 'Вход' in driver.page_source

    def test_registration_with_short_password(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Xpath.REGISTER_LINK)))
        driver.find_element(By.XPATH, Xpath.REGISTER_LINK).click()
        driver.find_element(By.XPATH, Xpath.NAME_INPUT).send_keys(Data.NAME)
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD[:5])
        driver.find_element(By.XPATH, Xpath.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Xpath.ERROR_MESSAGE)))
        assert 'Некорректный пароль' in driver.page_source

