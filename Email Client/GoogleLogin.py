import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import email
from email import *
import base64
import json
import os

class Login:
    def __init__(self):
        self.SCOPES = ['https://mail.google.com/']
        self.login()
    def login(self):
            """Shows basic usage of the Gmail API.
            Lists the user's Gmail labels.
            """
            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', self.SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            self.service = build('gmail', 'v1', credentials=creds)
    def send_message(self,msg):
        self.service.users().messages().send(userId="me",body=msg).execute()
    def get_profile(self):
        p=self.service.users().getProfile(userId='me').execute()
        return(p["emailAddress"])
    def getMessageList(self):
        self.msglist=self.glogin.service.users().messages().list(userId="me").execute()
        return(self.msglist)
        

if __name__ == '__main__':
    a=Login()
    print(a.get_profile())
