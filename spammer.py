#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = "https://web.whatsapp.com"
search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
alert_text = "Open WhatsApp on your phone and scan the QR code within 300 seconds.\nThis alert will dismiss itself in 5 seconds."
text_box = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"

contact = input("Who do you want to spam? ")
message = input("What do you want to spam? ")
times = int(input("How many times? "))

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 300)
driver.get(url)
driver.execute_script('window.alert(arguments[0])', alert_text)

try:
    alert = driver.switch_to.alert
    sleep(5)
    alert.accept()
except:
    pass

wait.until(EC.element_to_be_clickable((By.XPATH, search))).send_keys(contact + Keys.ENTER)

for i in range(times):
    driver.find_element_by_xpath(text_box).send_keys(message + Keys.ENTER)
    sleep(0.01)
