# .../google_api_project/travel_budget/services.py

import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

load_dotenv()

EMAIL_USER = os.environ['EMAIL_USER']
CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']

CREDENTIALS = Credentials.from_service_account_file(
    filename=CREDENTIALS_FILE, scopes=SCOPES
)
SHEETS_SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)
DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=CREDENTIALS)
