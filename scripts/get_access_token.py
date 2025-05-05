from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import pickle

# Define the scopes your application needs
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Paths
CLIENT_SECRET_FILE = os.path.join(base_path, '..', 'data', 'secret.json')
TOKEN_FILE = os.path.join(base_path, '..', 'data', 'token.pickle')

def main():
    creds = None

    # Check if token.pickle exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, go through the auth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Automatically refresh the token
            print("Token refreshed")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            print("New token obtained")

        # Save the credentials for next time
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
            print("Tokens saved to token.pickle")

    print("Access Token:", creds.token)
    print("Refresh Token:", creds.refresh_token)

if __name__ == '__main__':
    main()
