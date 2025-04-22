import requests
from google.auth.transport.requests import Request
from request import click_confirm_button
import pickle
import base64
import os
import webbrowser
import re

SENDER = "Netflix <info@account.netflix.com>"
SUBJECT = "Important: How to update your Netflix Household"
LINK_PATTERN = 'https://www.netflix.com/account/update-primary-location'

def open_link(link):
    # Open the link in a new tab
    webbrowser.open(link, new=2)

def get_latest_email():

    # Base path
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Token path
    token_path = os.path.join(base_path, '..', 'data', 'token.pickle')

    # Load OAuth credentials
    with open(token_path, "rb") as token:
        creds = pickle.load(token)

    # Refresh token if expired
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    # Get access token
    access_token = creds.token
    headers = {"Authorization": f"Bearer {access_token}"}

    # Fetch Gmail history based on latest historyId
    latest_message_url = "https://www.googleapis.com/gmail/v1/users/me/messages?maxResults=1"

    # Get the latest message id
    response = requests.get(latest_message_url, headers=headers)
    latest_message_data = response.json()
    message_id = latest_message_data["messages"][0]["id"]

    # Get the latest email by message id
    email_url = f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}"
    email_response = requests.get(email_url, headers=headers)
    email_data = email_response.json()

    return email_data


def process_mail():
    email_data = get_latest_email()

    # Check if the message is "UNREAD"
    if "UNREAD" in email_data["labelIds"]:

        # Extract sender, subject, and snippet
        headers_list = email_data["payload"]["headers"]
        sender = next(h["value"] for h in headers_list if h["name"] == "From")
        subject = next(h["value"] for h in headers_list if h["name"] == "Subject")

        # Debug print
        # print(f"Latest Unread Email Received:")
        # print(f"Sender: {sender}")
        # print(f"Subject: {subject}")
        # print(f"Snippet: {snippet}")
        
        # Check if sender is in the list
        if sender == SENDER and subject == SUBJECT:
            # Extract payload
            payload = email_data.get('payload', {})
            parts = payload.get('parts', [])
            if parts:
                data = parts[0].get('body', {}).get('data')
                if data:
                    # Decode the base64url encoded data
                    decoded_data = base64.urlsafe_b64decode(data + '=' * (-len(data) % 4))
                    payload_text = decoded_data.decode('utf-8')
                    payload = payload_text

            # Parsing the upload link using regex:
            match = re.search(r"Yes, This Was Me\s*\[\s*(https?://[^\]]+)\s*\]", payload)

            if match:
                link = match.group(1)
                print("Extracted link:", link)
            else:
                print("Could not find the 'Yes, This Was Me' link in the email.")
                return

            # Check if the link is valid
            if LINK_PATTERN not in link:
                print("Invalid link format.")
                return
            
            # Open the link in a new tab
            click_confirm_button(link)
    else:
        print("No new unread emails found.")
