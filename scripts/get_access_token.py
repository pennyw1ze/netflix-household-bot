from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

# Define the scopes your application needs
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Path to your OAuth JSON file (replace with your file path)
CLIENT_SECRET_FILE = os.path.join(base_path, '..', 'data', 'secret.json')

def main():
    # Download your credentials JSON from Google Cloud Console
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)

    # This will open a browser for the user to log in & grant access
    creds = flow.run_local_server(port=0)

    print("Access Token:", creds.token)
    print("Refresh Token:", creds.refresh_token)

    # Save tokens for reuse
    with open('../data/token.pickle', 'wb') as token_file:
        pickle.dump(creds, token_file)

    print("Tokens saved to token.pickle")

if __name__ == '__main__':
    main()
