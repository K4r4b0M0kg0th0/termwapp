from termwapp import Termwapp

class Multiple(Termwapp):
    def send_to_multiple(self, names_list, message):
        try:
            for name in names_list:
                self.send_message(name, message)
        except Exception as e:
            print(e)
