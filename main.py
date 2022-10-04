from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

chromedriver_path = '/Users/kenton/Documents/Programming/Personal Projects/Web Scrapers/Kayak Flight Web Scraper/chromedriver'

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

kayak = 'https://www.ca.kayak.com/flights/YQB-ATH/2023-03-12-flexible-3days/2023-03-18-flexible-3days?sort=bestflight_a'
driver.get(kayak)

# MIGHT NEED TO TARGET THIS IN ANOTHER WAY IF CLASS ENDS UP BEING DYNAMIC GOOGLE SEARCH XPATHS
xp_popup_close = 'bBPb-closeIcon'
print(xp_popup_close)
driver.find_element_by_class_name(xp_popup_close).click()


