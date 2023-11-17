from flask import Flask, render_template
from google.oauth2 import service_account
import gspread

app = Flask(__name__)

# Load the credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service_account_key.json',  # Replace with your service account key file path
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

@app.route('/')
def login():
    # Replace 'YOUR_SPREADSHEET_ID' and 'Sheet1' with your actual spreadsheet ID and sheet name
    spreadsheet_id = 'YOUR_SPREADSHEET_ID'
    sheet_name = 'Sheet1'

    # Access the Google Sheet
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_key(spreadsheet_id).worksheet(sheet_name)

    # Get data from the sheet
    data = sheet.get_all_records()

    # Pass the data to the template
    return render_template('login.html', data=data)

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

if __name__ == '__main__':
    app.run(debug=True)
