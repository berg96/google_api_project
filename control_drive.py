import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from pprint import pprint

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

load_dotenv()

CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']


# Функция авторизации.
def auth():
    credentials = Credentials.from_service_account_file(
        filename=CREDENTIALS_FILE, scopes=SCOPES
    )
    service = discovery.build('drive', 'v3', credentials=credentials)
    return service


def get_list_obj(service):
    response = service.files().list(
        q='mimeType="application/vnd.google-apps.spreadsheet"'
    )
    return response.execute()


def clear_disk(service, spreadsheets):
    for spreadsheet in spreadsheets:
        response = service.files().delete(fileId=spreadsheet['id'])
        response.execute()

service = auth()
spreadsheets = get_list_obj(service)['files']
print(spreadsheets)
# clear_disk(service, spreadsheets)
