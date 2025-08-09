import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# Example: Open sheet and read data
spreadsheet = client.open("Your Spreadsheet Name")
sheet = spreadsheet.sheet1

data = sheet.get_all_records()
df = pd.DataFrame(data)

print(df)
