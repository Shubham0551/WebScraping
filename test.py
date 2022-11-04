# from selenium.webdriver import ActionChains
# from Locators.Locator import *
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pandas as pd
# import util
# from ConfigData.ExcelData import *
# from selenium import webdriver
#
# from Locators.Locator import city
# from selenium.webdriver.common.by import By
# driver= webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://npiregistry.cms.hhs.gov/search')
# driver.maximize_window()
# path = "D:\\project\\Book1.xlsx"
# rows=util.get_row_count(path, 'Sheet1')
# for i in range(2, rows+1):
#     Data_list = []
#     #SR_NO=xl_utils.read_data(path,'list-cities-us-30j',i,1)
#     CITY = util.read_data(path, 'Sheet1', i, 2)
#     STATE = util.read_data(path, 'Sheet1', i, 3)
#     State_Code=util.read_data(path, 'Sheet1', i, 4)
#     city_box = driver.find_element(by=By.XPATH, value=city)
#     city_box.send_keys(CITY)
#     search_btn = driver.find_element(by=By.XPATH, value="//button[@name='search']")
#     # actions = ActionChains(driver)
#     # actions.move_to_element(search_btn).perform()
#     search_btn.click()
#     time.sleep(5)
#     for i in range(1, 8):
#         j = str(i)
#         npii = "/html[1]/body[1]/app-root[1]/main[1]/div[1]/app-results[1]/table[1]/tbody[1]/tr[" + j + "]/td[1]/button[1]"
#         npi_no = driver.find_element(by=By.XPATH, value=npii)
#         npi_no.click()
#         time.sleep(5)
#         data = driver.find_element(By.XPATH, name_link).text
#         Data_list.append(data)
#         data = driver.find_element(By.XPATH, npi_link).text
#         Data_list.append(data)
#         data = driver.find_element(By.XPATH, address_link).text
#         Data_list.append(data)
#         data = driver.find_element(By.XPATH, taxnomoy).text
#         Data_list.append(data)
#         df = pd.DataFrame([Data_list, ])
#         # print(df)
#         # df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
#         with pd.ExcelWriter('C:\\Users\\shubh\\PycharmProjects\\NykaSample\\Automation\\pandas_to_excel.xlsx',
#                             mode='w+') as writer:
#             df.to_excel(writer, sheet_name='Sheet_name_3')
#
#         driver.back()
#         time.sleep(5)
