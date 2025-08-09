from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import gspread
import os
import json
from google.oauth2.service_account import Credentials

# Google Sheets setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials_info = json.loads(os.environ['GOOGLE_CREDENTIALS_JSON'])
creds = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)

SPREADSHEET_ID = '1NEPCQOqgWUWA2zv947KT4ySONqQu_yZxjsWJOkZccOA'
SHEET_NAME = 'data'

client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Selenium setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path='/usr/lib/chromium/chromedriver', options=chrome_options)

try:
    driver.get('https://del-desk.excitel.in/login')

    driver.find_element(By.NAME, 'userId').send_keys('backoffice1')
    driver.find_element(By.NAME, 'password').send_keys('123456789')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(5)

    driver.get('https://del-desk.excitel.in/tickets/advancedSearch/1?listData=%7B%22sortBy%22:%7B%7D,%22currentPage%22:1,%22timestamp%22:1754761622480%7D')

    time.sleep(5)

    body_text = driver.find_element(By.TAG_NAME, 'body').text

    sheet.clear()
    lines = body_text.split('\n')
    rows = [[line] for line in lines if line.strip() != '']
    sheet.update('A1', rows)

finally:
    driver.quit()
