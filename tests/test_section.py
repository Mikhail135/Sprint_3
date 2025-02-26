from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lacator import Xpath
from data import Data
class TestSection:
    def test_swap_section_to_sauces(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                        ((By.XPATH, Xpath.SAUCESS_BUTTON)))
        driver.find_element(By.XPATH, Xpath.SAUCESS_BUTTON).click()
        element = driver.find_element(By.XPATH, Xpath.SAUCESS_STR)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert "BurgerIngredient_ingredient__text__yp3dH" in element.get_attribute("class")

    def test_swap_section_to_rolls(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                        ((By.XPATH, Xpath.ROLLS_BUTTON)))
        driver.find_element(By.XPATH, Xpath.SAUCESS_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located
                                        ((By.XPATH, Xpath.ROLLS_BUTTON)))
        driver.find_element(By.XPATH, Xpath.ROLLS_BUTTON).click()
        element = driver.find_element(By.XPATH, Xpath.ROLLS_STR)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert "BurgerIngredient_ingredient__text__yp3dH" in element.get_attribute("class")

    def test_swap_section_to_toppings(self, driver):
        driver.get(Data.SITE)
        driver.find_element(By.XPATH, Xpath.PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Xpath.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Xpath.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Xpath.SHORT_LOG_IN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Xpath.TOPPINGS_BUTTON)))
        driver.find_element(By.XPATH, Xpath.TOPPINGS_BUTTON).click()
        element = driver.find_element(By.XPATH, Xpath.TOPPINGS_STR)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert "BurgerIngredient_ingredient__text__yp3dH" in element.get_attribute("class")
