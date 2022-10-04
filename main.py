from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
# from kayak import Kayak
from skyskanner import Skyscanner

city_from = 'YQB'
city_to = 'lis'
date_start = '2023-03-12'
date_to = '2023-03-18'

skyscanner = Skyscanner(city_from, city_to, date_start, date_to)
skyscanner.start_skyscanner()



# NOT WORKING, JUST A PROBLEM WITH OOP
# kayak = Kayak('YQB', 'ATH', '2023-03-12', '2023-03-18')
# print(kayak)
# # kayak.start_kayak()








