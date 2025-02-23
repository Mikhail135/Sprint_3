from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
class TestSignin:
    def test_registration_with_valid_password(self, driver, name, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, Xpath.LOG_IN).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, Xpath.REGISTER_LINK)))
            driver.find_element(By.XPATH, Xpath.REGISTER_LINK).click()
            driver.find_element(By.XPATH, Xpath.NAME_INPUT).send_keys(name)
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, Xpath.REGISTER_BUTTON).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Вход")]')))
            assert 'Вход' in driver.page_source
        finally:
            driver.quit()

    def test_registration_with_short_password(self, driver, name, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, Xpath.LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Xpath.REGISTER_LINK)))
        driver.find_element(By.XPATH, Xpath.REGISTER_LINK).click()
        driver.find_element(By.XPATH, Xpath.NAME_INPUT).send_keys(name)
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(By.XPATH, Xpath.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, Xpath.ERROR_MESSAGE)))
        assert 'Некорректный пароль' in driver.page_source
        driver.quit()
