from termwapp import Termwapp

class Message(Termwapp):
    def send_message(self, name, message):
        try:
            search_bar = self.driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
            search_bar.send_keys(name)
            search_bar.send_keys(Keys.RETURN)
            text_box = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            text_box.send_keys(message)
            text_box.send_keys(Keys.RETURN)
            sent_icon = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
            if sent_icon:
                print(f"Message sent to {name} successfully.")
        except NoSuchElementException:
            print("Could not find the search bar.")
            self.driver.quit()
            exit()
