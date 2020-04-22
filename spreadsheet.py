# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Онлайн шахматный клуб СПХФУ").sheet1

list_of_hashes = sheet.get_all_records()


def next_available_col(worksheet):
    str_list = list(filter(None, worksheet.row_values(1)))
    return str(len(str_list) + 1)


def write(col_name, nicknames):
    next_col = next_available_col(sheet)
    sheet.update_cell(1, next_col, col_name)
    for i in range(len(list_of_hashes)):
        nick = list_of_hashes[i]['Ник на lichess.org']
        if nick in nicknames:
            sheet.update_cell(i + 2, next_col, '1')
