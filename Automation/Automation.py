import time
import pandas as pd
import openpyxl
import pytest
from Locators.Locator import *
from selenium.webdriver.common.by import By
from conftest import driver


class TestLoginPage:

    @pytest.mark.usefixtures("initiate_driver")
    def test_send_city(self, initiate_driver):
        Data_list=[]
        city_box = driver.find_element(by=By.XPATH, value=city)
        city_box.send_keys("Birmingham")
        search_btn = driver.find_element(by=By.XPATH, value=search)
        time.sleep(5)
        search_btn.click()
        time.sleep(5)
        npi_no = driver.find_element(by=By.XPATH, value=npi)
        npi_no.click()
        time.sleep(5)
        data = driver.find_element(By.XPATH,name_link).text
        Data_list.append(data)
        data = driver.find_element(By.XPATH,npi_link).text
        Data_list.append(data)
        data = driver.find_element(By.XPATH, address_link).text
        Data_list.append(data)
        data = driver.find_element(By.XPATH, taxnomoy).text
        Data_list.append(data)
        df = pd.DataFrame([Data_list,])
        print(df)
        df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')


