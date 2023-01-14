from selenium import webdriver

class Termwapp:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://web.whatsapp.com/")
        input("Scan the QR code and press enter to continue...")
        
    def close_driver(self):
        self.driver.close()
if __name__ == "__main__":
    driver = webdriver.Chrome()
    tp = Termwapp(driver)
    #other functionalities
    tp.close_driver()
