# Shawn Stolsig
# PDX Code Guild 
# Assignment: Python Section Presentation
# Date: 11/11/2019

# This file is mainly taken from the quickstart.py file, provided by Google API documentation
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# created classes
import player
import clan

def get_sheets_data(spreadsheets_id, range_name):
    '''
    '   This function handles the authentication and retrieval of data from a Google Sheet
    '   Parameters: The spreadsheet id and the range of data to pull    Return: 2D nested list of rows/cols
    '''

    # If modifying these scopes, delete the file token.pickle.  (not sure what this is for)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheets_id,
                                range=range_name).execute()
    values = result.get('values', [])

    # if unable to find the sheet
    if not values:
        return 'No data found.'
    # if able to find values, return them 
    else:
        return values

def get_player_dataset(list_data):
    '''
    '   A function for turning the input file (as 2D list of cells) into a dictionary 
    '   Parameters: 2D list of cells        Returns: dictionary dataset (specified below)
    '''

# The ID and range of the test  spreadsheet.
clan_info_spreadsheet_ID = '14oxx0qpWg7VWhRyYIVP6uv5YL40BQI15APGDOwsdZdQ'
range_name = 'KSD Tier 10'

# for seeing if the Google Sheets API get works
# print(get_sheets_data(clan_info_spreadsheet_ID, range_name))

# 2D list of strings from Google Sheets
sheets_output = get_sheets_data(clan_info_spreadsheet_ID, range_name)

clan = clan.Clan(sheets_output)

for p in clan.roster:
    print(p)


# # find the header list
# header = sheets_output[1]

# # try creating a player
# test_player = player.Player(header, sheets_output[2])

# # print out test player
# print(f"Player name is: {test_player.username_wg}")
# print(f"Player join date is: {test_player.join_date}")
# print(f"Player's ships are: {test_player.ships}")