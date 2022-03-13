import requests
#import BeautifulSoup4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')


URL539 = "https://www.taiwanlottery.com.tw/lotto/dailycash/history.aspx"
driver.get(URL539)
driver.find_element_by_id('D539Control_history1$txtNO').send_keys("111000060")
driver.find_element_by_id('D539Control_history1$btnSubmit').click()


response = requests.get(URL539)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
TableID = "D539Control_history1_dlQuery"
table = soup.find('table', id=TableID)
#table
print(type(table))
number1 = soup.find('span',id = "D539Control_history1_dlQuery_SNo1_0")
number2 = soup.find('span',id = "D539Control_history1_dlQuery_SNo2_0")
number3 = soup.find('span',id = "D539Control_history1_dlQuery_SNo3_0")
number4 = soup.find('span',id = "D539Control_history1_dlQuery_SNo4_0")
number5 = soup.find('span',id = "D539Control_history1_dlQuery_SNo5_0")
print(number1.text,number2.text,number3.text,number4.text,number5.text)

'''
要抓的值的名稱有兩種
第一種是依照開講順序顯示
D539Control_history1_dlQuery_SNo1_0
第二種是依照大小順序顯示
D539Control_history1_dlQuery_No1_0

尾碼的0代表第一個表格，也就是該頁面顯示的最近一期的結果
而下一期的表格內容會顯示如下

D539Control_history1_dlQuery_SNo1_1
D539Control_history1_dlQuery_No1_1
依此類推




about click web page reference
https://stackoverflow.com/questions/52306514/how-to-enter-values-into-a-web-page-and-click-on-a-checkbox-using-python


You can't do it with requests.

You can do it easily using selenium.

================================
Click
=================================
from selenium import webdriver

driver = webdriver.Chrome('path to chromedriver')
driver.get('website url')

button = driver.find_element_by_css_selector('css selector')
button.click()
========================================
Write text to form input
=======================================
from selenium import webdriver

driver = webdriver.Chrome('path to chromedriver')
driver.get('website url')

text_input = driver.find_element_by_css_selector('css selector')
text_input.send_keys('hello world')
'''