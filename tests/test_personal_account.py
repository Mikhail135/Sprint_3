from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
from data import Data
class TestAccount:
    def test_personal_account_after_log_in(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, Xpath.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, Xpath.LOG_OUT)))
        assert "Выход" in driver.page_source

    def test_from_personal_account_to_constructor(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
            By.XPATH, Xpath.PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
            By.XPATH, Xpath.LOG_OUT)))
        driver.find_element(By.XPATH, Xpath.CONSTRUCRT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
            By.XPATH, Xpath.CREAT_BURGER)))
        assert "Соберите бургер" in driver.page_source





