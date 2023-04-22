import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)


if __name__ == "__main__":
    print("[+] Usage : python3 login.py <website> <username> <password>")
    print("[+] website -> linkedin OR icegate")
    if len(sys.argv) != 4:
        print("[-] Please provide proper args.")
        sys.exit()
    website = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    browser = Browser("./chromedriver")

    if website == "icegate":

        browser.open_page("https://foservices.icegate.gov.in/#/login")
        time.sleep(3)

        browser.add_input(by=By.ID, value="icegateId", text=username)
        browser.add_input(by=By.ID, value="password", text=password)
        browser.click_button(by=By.CLASS_NAME, value="login")
        time.sleep(10)

    else:

        browser.open_page("https://linkedin.com")
        time.sleep(3)

        browser.add_input(by=By.ID, value="session_key", text=username)
        browser.add_input(by=By.ID, value="session_password", text=password)
        browser.click_button(by=By.CLASS_NAME, value="sign-in-form__submit-btn--full-width")

        time.sleep(10)

        if browser.browser.current_url == "https://www.linkedin.com/uas/login-submit":
            print("Login Failed")
        else:
            print("Login Successful")

    browser.close_browser()
