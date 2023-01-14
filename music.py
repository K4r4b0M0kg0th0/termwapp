from termwapp import Termwapp

class Music(Termwapp):
    def send_music(self, music_path):
        try:
            attachment_icon = self.driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/div/span")
            attachment_icon.click()

            document_icon = self.driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button")
            document_icon.click()

            self.driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/div[2]/span[1]/div/div/div[2]/input").send_keys(music_path)
            send_icon = self.driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[2]/span/div/div/div[2]/span[2]/button")
            send_icon.click()
            print("Music sent successfully.")
        except NoSuchElementException:
            print("Could not find the attachment icon.")
            self.driver.quit()
            exit()
