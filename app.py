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
credentials_info = json.loads(os.environ['  "type": "service_account",
  "project_id": "deldeskscraper",
  "private_key_id": "b900ed09d5969751b2e745406c7b6b67af62572f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDRMfosmGCUpVHM\n/zAz72LyjkV55ycpIqZ4GWfPlIiEe1tAJjHWsoVp1VUJNt8fTQvYLmBnfqcnoZCM\n+ApIFKW0bAP4OKUysipRHWq9vgR/dq9OGDQJBAs/NvHzAgc3pNxrgNt3lDghGAX6\nl7ZWPqGDk7MmRq7pd+YWbVpNrHO9LMblwLrEJFD2TastJGzjE46ZX5sx5NfwOR6I\n1g13LR1sO8DD7KiBeJj2cqv4G/1B6oIfJk+n+OYIovPelljw7qie2X9KyrJktW/4\nYFlb8XSOKLI2c+pcVyS8ZFC7Pe66Odo2qh3LrPGdDMl5Y1tiRWok164+L8BAttvO\nsT/oZOzPAgMBAAECggEAIceOrJ3MVqRdUZtRVsmMcjtL97O+LJPGSrVbgHbtFmtu\n4Cxqts7r4RuMGClOnRjNVVKjyYJ3jlw14bV5v4rp+PjKKU5ISqffUmrMHihtRIHP\nK+6XlG8dO89tAT7uGGucFhXgGm6KI7nj2UOfM0z4uqzibEdUnil4s11kDA/RPpYN\n5zhUCQytlj3BSfsEHgqsShhcl5OC6gTI/QYrGrv9MCaeSN4HSfFLBWByeVqC2ZJD\nOPMTHOj5ZSUC7/h+IB0LkXgDcrzuydzalI/dA45QMdERwgdJXnkme+ByxhHUrniv\nXH8otTecd4PwGDyp554OkFrVN60zhjRi5plujzI37QKBgQD7eRTnDGGd/I5hFtXT\ng0uuCzYqxLkTd7cUzJswP92nTIuDAIECswm2lraAJJ4xqCFff5Y+nN8sQVh7fQjm\nQyIkh3KHPBIaCfV2N6cBRhAbtn1Czpv+b2XaMNh7kDdUE6ao1DfsJQliNgoym2vf\njrrT3Pfq4WTTbacEnOmFLbkkLQKBgQDU9g7GDYxgDRqPlPN1JZtVcG14s4P60Jgf\nxxyu0f8pYw15d4B/Fu5lMbNYWrHQGSXgQB9fMT9Vy3EgEpt22WkyKBRxnFAsr5Jg\njdPnYdHSkV1VRvFZQxX3Mdw0CDydw5VD6Q5EwKw0NjgrYftylCA6OXiNDcA9bkXR\n69L/nyjGawKBgQDt/Erh1f/UCh2cmIXH5CuNDKM4mnAkklk7X99GLErSd0hYs/Nj\n4JhCqiMQ5panm9vpis9fdgpm0XixdUUk1UfMljq27Qycg+w+8rAkLnA0KeIlhW5v\nvnD/qtZVKciS0v4YLK631t0oisff2OKf8W2x7x7YtHI8/TrgzLbbCMh8CQKBgDqg\niqynai+/K8K/ZM6pTbwVuW1zLjBMYLTO4eyWz0IbjMgVyAA01ehx6Ee4oB8D7VNx\nE7HnIuKBoWEM/lOXwsgWFJq6R7AlnYyLPv0CBvuLHUCuyR6jw1ZMGa0RX26nO154\nuH7g9Adjrc7zqH+Am+arj651TKkcxIfn/ix1KoqFAoGBAPKwbL9wzFD09XHcnkBG\nSFF4i0PWnPGu2AsjjxOSVBHcDsJqigastvmZQiV1WIQcWClUNLTxLLqzp7sXK4g+\ng33z+3CmSlDoTjax12vKuYsHqzLab1L+u+dzEl0rBN6AguA4QM3q+XHsBjdycxIP\n/yAvdTc+NZX6LWW57VhvYPBs\n-----END PRIVATE KEY-----\n",
  "client_email": "sheet-scraper@deldeskscraper.iam.gserviceaccount.com",
  "client_id": "103616948492979427912",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sheet-scraper%40deldeskscraper.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}'])
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
