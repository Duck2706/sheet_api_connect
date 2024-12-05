# sheets_helper.py

import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Hàm lấy ID từ URL Google Sheet
def extract_spreadsheet_id(url):
    return url.split("/d/")[1].split("/")[0]

# Hàm đọc dữ liệu từ Google Sheet
def read_google_sheet(spreadsheet_id, range_name="Sheet1!A1:Z"):
    # Lấy thông tin xác thực từ file credentials.json
    creds = service_account.Credentials.from_service_account_file('credentials.json')

    # Xây dựng service Google Sheets API
    service = build('sheets', 'v4', credentials=creds)

    # Đọc dữ liệu từ Google Sheet
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    
    # Lấy dữ liệu dưới dạng list
    values = result.get('values', [])
    
    # Trả về dữ liệu
    return values
