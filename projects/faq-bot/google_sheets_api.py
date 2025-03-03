import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_credentials.json", scope)
client = gspread.authorize(creds)

# Open FAQ Sheet
sheet = client.open("Chatbot_FAQs").sheet1

def get_faq(question):
    data = sheet.get_all_records()
    for row in data:
        if row["Question"].lower() in question.lower():
            return row["Answer"]
    return "Sorry, I don't have an answer for that."
