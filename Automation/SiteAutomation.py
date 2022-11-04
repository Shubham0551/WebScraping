import time
from Utilities.DataScraping import scraping_data
import pytest
import util
from Utilities.CommonUtilities import CommonUtil
from Locators.Locator import *
from selenium.webdriver.common.by import By
from conftest import driver
path = "D:\\project\\Book1.xlsx"
rows = util.get_row_count(path, 'Sheet1')
# print(city)
fixdata = []


class TestLoginPage:

    cu = CommonUtil()
    @pytest.mark.usefixtures("initiate_driver")
    def test_send_city(self, initiate_driver):
        for i in range(1, 11):
            CITY = util.read_data(path, 'Sheet1', i, 1)
            city_box = driver.find_element(by=By.XPATH, value=city)
            city_box.clear()
            city_box.send_keys(CITY)
            self.cu.click_element(search)
            time.sleep(5)
            for q in range(0, 11):
                Data_list = []
                # j = str(q)
                # npii = "/html[1]/body[1]/app-root[1]/main[1]/div[1]/app-results[1]/table[1]/tbody[1]/tr[" + j + \
                #        "]/td[1]/button[1]"
                # driver.execute_script("window.scrollBy(0," + j + "*72,"");")
                npii = "//tbody/tr/td[1]/button"
                time.sleep(2)
                npi_no = driver.find_elements(by=By.XPATH, value=npii)[q]
                npi_no.click()
                time.sleep(3)
                # data = self.cu.get_element_text(name_link)
                # Data_list.append(data)
                # data = self.cu.get_element_text(npi_link)
                # Data_list.append(data)
                # data = self.cu.get_element_text(address_link)
                # Data_list.append(data)
                # data = self.cu.get_element_text(taxnomoy)
                # Data_list.append(data)
                # fixdata.append(Data_list)
                # # print(df)
                # # df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
                # wb = Workbook()
                # ws = wb.active
                # for data in fixdata:
                #     ws.append(data)
                # wb.save("demoexecl.xlsx")

                #     df.to_excel(writer, startrow=, sheet_name='Sheet_name_3')
                scraping_data()
                driver.back()
                time.sleep(3)

            driver.back()
