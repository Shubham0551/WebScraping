import time
from openpyxl import Workbook
import pytest
import util
from Locators.Locator import *
from selenium.webdriver.common.by import By
from conftest import driver
from Utilities.CommonUtilities import CommonUtil
path = "D:\\project\\Book1.xlsx"
rows = util.get_row_count(path, 'Sheet1')
fix_data = []
cu = CommonUtil()


class TestLoginPage:

    @pytest.mark.DataScrap
    @pytest.mark.usefixtures("initiate_driver")
    def test_send_city(self, initiate_driver):
        for i in range(1, rows + 1):
            city_name = util.read_data(path, 'Sheet1', i, 1)
            city_box = driver.find_element(by=By.XPATH, value=city)
            city_box.clear()
            city_box.send_keys(city_name)
            cu.click_element(search)
            time.sleep(2)
            for p in range(1, 10):
                data_list = []
                for q in range(1, 7):
                    npii = "//tbody/tr[" + str(p) + "]/td[" + str(q) + "]"
                    data = driver.find_element(By.XPATH, npii).text
                    data_list.append(data)
                fix_data.append(data_list)
                # print(df)
                # df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
                wb = Workbook()
                ws = wb.active
                for data in fix_data:
                    ws.append(data)
                wb.save("demo_excel3.xlsx")
            driver.back()
