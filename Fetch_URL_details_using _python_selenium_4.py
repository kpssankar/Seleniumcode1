from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Suman:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def homepage(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
    
    def fetch_url(self):
        return self.driver.current_url
    
    def fetch_title(self):
        return self.driver.title
    
    def fetch_page_source(self):
        return self.driver.page_source

    def shutdown(self):
        self.driver.quit()
    

if __name__ == "__main__":
    suman = Suman("https://www.saucedemo.com/")
    suman.homepage()
    print(suman.fetch_url())
    print(suman.fetch_title())
    print(suman.fetch_page_source())
    suman.shutdown()