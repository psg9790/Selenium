from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["글번호", "날짜", "제목+내용"])


url = 'https://gall.dcinside.com/mgallery/board/lists/?id=mugimido'
driver = webdriver.Chrome('C:/Users/PSG/Desktop/Selenuim/chromedriver')
driver.get(url)

driver.implicitly_wait(2)

btn = driver.find_element(
    By.CSS_SELECTOR, '#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody > tr:nth-child(11) > td.gall_tit.ub-word > a')
btn.send_keys(Keys.CONTROL + '\n')
driver.implicitly_wait(1)
driver.switch_to.window(driver.window_handles[-1])
driver.implicitly_wait(1)
txt = driver.find_element(
    By.CSS_SELECTOR, '#container > section > article:nth-child(3) > div.view_content_wrap > div > div.inner.clear > div.writing_view_box > div.write_div')
print(txt.text)


driver.implicitly_wait(1)
driver.close()
driver.switch_to.window(driver.window_handles[-1])
driver.implicitly_wait(1)
# '#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody > tr:nth-child(11) > td.gall_tit.ub-word > a'
# for i in range(11, 53):
#     arti = driver.find_element(
#         By.CSS_SELECTOR, '#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody > tr:nth-child(' + str(i) + ') > td.gall_tit.ub-word > a')
#     print(arti.text)
driver.close()
workbook.save("DC코인갤.xlsx")
