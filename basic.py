from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\SeleniumDrivers\chromedriver.exe")
driver.get("https://zoom.us/download")
driver.implicitly_wait(3) #to find element in entire page
my_element = driver.find_element_by_css_selector("a.download")
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element( #custom waiting,until certain condition 
        (By.CLASS_NAME, 'progress-label'), #ELEMENT CLASS NAME
        'Complete!' #Expected Text
    )
)
