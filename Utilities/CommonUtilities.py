from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC


class CommonUtil:

    def get_element_text(self, element: str) -> str:
        """
        Return text of the element
        :param element: string
        :return: str
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element)))
        text = driver.find_element(by=By.XPATH, value=element).text
        return text

    def click_element(self, element: str) -> None:
        """
        Click on the given Element locator
        :param element: String
        :return: None
        """
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element)))
        driver.find_element(by=By.XPATH, value=element).click()

    def fill_data(self, element, data):
        """
        Click fill the given data in the located element
        :param element: Any
        :param data: String or Integer
        :return: None
        """
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element)))
        driver.find_element(by=By.XPATH, value=element).send_keys(data)
