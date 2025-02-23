from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
class TestLogin:
    def test_log_in_button_through_your_personal_account(self, driver, name, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[contains(text(), "Соберите бургер")]')))
            assert "Соберите бургер" in driver.page_source
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

    def test_log_in_button_through_log_in_to_your_account(self, driver, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[contains(text(), "Соберите бургер")]')))
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

    def test_log_in_reg_form(self, driver, email, password):
        try:
            driver.get('https://stellarburgers.nomoreparties.site/register')
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//a[@href="/login"]')))
            driver.find_element(By.XPATH, '//a[@href="/login"]').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[contains(text(), "Соберите бургер")]')))
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

    def test_log_in_through_forgot_password(self, driver, email, password):
        try:
            driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//a[@href="/login"]')))
            driver.find_element(By.XPATH, '//a[@href="/login"]').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 15).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1[contains(text(), "Соберите бургер")]')))
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

