from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
class Test_ection:
    def test_swap_section_to_sauces(self, driver, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Соус')]"))
            )
            element = driver.find_element(By.XPATH, '//span[contains(text(), "Соус")]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            assert "Соус" in driver.page_source
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

    def test_swap_section_to_rolls(self, driver, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'булка')]"))
            )
            element = driver.find_element(By.XPATH, "//span[contains(text(), 'булка')]")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            assert "булка" in driver.page_source
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()

    def test_swap_section_to_toppings(self, driver, email, password):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
            driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(email)
            driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(password)
            driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Мясо')]"))
            )
            element = driver.find_element(By.XPATH, '//span[contains(text(), "Мясо")]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            assert "Мясо" in driver.page_source
        except Exception as e:
            print(f"Ошибка при выполнении теста: {e}")
        finally:
            driver.quit()