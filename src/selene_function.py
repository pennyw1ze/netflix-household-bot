import requests
from bs4 import BeautifulSoup

def press_button(url):

    # Making a GET request
    r = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Finding the button
    link = soup.find('link', {'as': 'script'})

    if link:
        # Find the real link parsing the href
        href = link.get('href')

        print("Link text:", href)
    else:
        print("Button not found.")

press_button("http://127.0.0.1:5500/page.html")