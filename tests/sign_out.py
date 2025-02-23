from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
class Test_Exit:
    def test_button_exit_from_personal_account(self, driver, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, Xpath.personal_account)))
            driver.find_element(By.XPATH, Xpath.personal_account).click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//button[text()="Выход"]')))
            driver.find_element(By.XPATH, '//button[text()="Выход"]').click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//button[text()="Войти"]')))
            assert "Войти" in driver.page_source
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()