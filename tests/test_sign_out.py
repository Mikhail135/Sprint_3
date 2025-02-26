from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
from data import Data
class TestExit:
    def test_button_exit_from_personal_account(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Xpath.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Xpath.LOG_OUT)))
        driver.find_element(By.XPATH, Xpath.LOG_OUT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Xpath.SHORT_LOG_IN)))
        assert "Войти" in driver.page_source
