from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")

driver.get("https://www.youtube.com/")
driver.implicitly_wait(5)

search_box = driver.find_element_by_css_selector('input#search')
button = driver.find_element_by_css_selector('button#search-icon-legacy') #button[onclick="total()"]

search_box.send_keys('Maria ozawa')
search_box.send_keys(Keys.ENTER)