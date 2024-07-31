import time

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
from selenium.webdriver.common.by import By

browsers = ["Chrome","Firefox"]
class cross_browser():
    def browser(self):
        for browser in browsers:
            if browser=="Chrome":
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
            elif browser=="Firefox":
                firefox_options = FirefoxOptions()
                firefox_options.add_argument("--headless")
                firefox_options.add_argument("disable-gpu")
                firefox_options.add_argument("--window-size=1920,1080")
                driver =webdriver.Firefox(service=FirefoxService(),options=firefox_options)
            else:
                print("driver is not capable")
            #driver.maximize_window()
            #driver.maximize_window()
            driver.get("https://dev.baps.dev/mis/")
            screenshot_path = os.path.join(os.getcwd(),f"{browser}_screenshort1.png")
            driver.save_screenshot(screenshot_path)
            driver.quit()
            print("Successfully")

smoke_testing=cross_browser()
smoke_testing.browser()



