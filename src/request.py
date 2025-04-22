import sys
from playwright.sync_api import sync_playwright

def press_button(link):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(link)
        # click the "Confirm Update" button
        page.click('[data-uia="set-primary-location-action"]')
        # give it a moment to fire
        page.wait_for_timeout(2000)
        # Close the browser
        browser.close()
        print("✅ Clicked Confirm Update button")