import time
from openpyxl import Workbook
import pytest
import util
from Locators.Locator import *
from selenium.webdriver.common.by import By
from conftest import driver
path = "D:\\project\\Book1.xlsx"
rows = util.get_row_count(path, 'Sheet1')
# print(city)
fixdata = []


class TestLoginPage:

    @pytest.mark.usefixtures("initiate_driver")
    def test_send_city(self, initiate_driver):
        for i in range(1, rows + 1):

        #for i in range(1, 11):
            #CITY = util.read_data(path, 'Sheet1', i, 1)
            CITY = util.read_data(path, 'Sheet1', i, 1)
            # STATE = util.read_data(path, 'Sheet1', i, 3)
            # State_Code = util.read_data(path, 'Sheet1', i, 4)
            city_box = driver.find_element(by=By.XPATH, value=city)
            city_box.clear()
            city_box.send_keys(CITY)
            search_btn = driver.find_element(by=By.XPATH, value=search)
            time.sleep(5)
            search_btn.click()
            time.sleep(5)
            for q in range(1, 11):
                Data_list = []
                j = str(q)
                npii = "/html[1]/body[1]/app-root[1]/main[1]/div[1]/app-results[1]/table[1]/tbody[1]/tr[" + j + \
                       "]/td[1]/button[1]"
                driver.execute_script("window.scrollBy(0," + j + "*72,"");")
                time.sleep(2)
                npi_no = driver.find_element(by=By.XPATH, value=npii)
                npi_no.click()
                time.sleep(3)
                data = driver.find_element(By.XPATH, name_link).text
                Data_list.append(data)
                data = driver.find_element(By.XPATH, npi_link).text
                Data_list.append(data)
                data = driver.find_element(By.XPATH, address_link).text
                Data_list.append(data)
                data = driver.find_element(By.XPATH, taxnomoy).text
                Data_list.append(data)
                fixdata.append(Data_list)
                # print(df)
                # df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
                wb = Workbook()
                ws = wb.active
                for data in fixdata:
                    ws.append(data)
                wb.save("demoexecl.xlsx")

                #     df.to_excel(writer, startrow=, sheet_name='Sheet_name_3')
                driver.back()
                time.sleep(3)

            driver.back()