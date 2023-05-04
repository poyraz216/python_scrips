from pg import DB
import psycopg2
from bs4 import BeautifulSoup
import requests
import urllib.parse
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from PIL import Image
from selenium.webdriver.common.by import By
import pandas as pd
import cx_Oracle
import datetime
import seleniummailer as smail
import psycopg2

from selenium.webdriver.chrome.service import Service
import csv
from datetime import date
from datetime import datetime,timedelta
today = date.today()
start_time = datetime.now()

//DB info

curRepo = conRepo.cursor()						
#xxx


cdriver = "E:\\trend.exe"
chromeOptions = Options()
chromeOptions.add_argument("--headless")
#chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--window-size=1660,1050')
chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument('--no-sandbox')

browser = webdriver.Chrome(cdriver,options=chromeOptions)
browser.set_window_position(-5, 0)

#browser.maximize_window()
#browser.save_screenshot('screen_shotav.png')

#xxxx

conRepo.commit()
URL = "https://URL"

try:
	browser.get(URL)
	time.sleep(5)
	#find_element(By.XPATH, ‘xpath’) 
	#browser.find_element("xpath",'/html/body/div/div[2]/button[3]').click()
	time.sleep(2)
	#browser.find_element("xpath",'//*[@id="proceed-link"]').click()
	time.sleep(2)
	browser.switch_to.frame('popupFrame')
	time.sleep(2)

	browser.find_element("xpath",'//*[@id="confirm"]').click()
	browser.switch_to.default_content()

	time.sleep(5)
	browser.find_element("name","username").send_keys("Username")
	browser.find_element("id","password").send_keys("password")

	time.sleep(5)

	browser.find_element("id","submit").click()
	time.sleep(10)
	browser.find_element("id","jpwClose").click()
	time.sleep(5)
	browser.switch_to.default_content()
	time.sleep(2)
	browser.find_element("id","z_top_logo_id").click()

except:
	print("There is problem")

browser.close()
browser.quit()
curRepo.close()
conRepo.close()
