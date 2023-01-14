from selenium import webdriver
class Termwapp:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com/")
        input("Scan the QR code and press enter to continue...")
