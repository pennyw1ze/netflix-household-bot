import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_confirm_button(url):    
    options = Options()
    # options.add_argument('--headless')  # Uncomment for headless mode

    service = Service(executable_path="/usr/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url)

    wait = WebDriverWait(driver, 20)

    try:
        # Make sure the body has loaded
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Now wait for the button to be clickable using CSS Selector
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pressable_styles__a6ynkg0 button_styles__1kwr4ym0  default-ltr-cache-1dytctv-StyledBaseButton e1ax5wel2")))

        # Click the button
        button.click()
        print("Button clicked!")

    except Exception as e:
        print(f"Failed to click button: {e}")

    finally:
        time.sleep(5)  # Observe before closing
        driver.quit()
