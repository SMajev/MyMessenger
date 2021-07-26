from datetime import datetime


class User:
    def __init__(self, nickname, password, controller):
        self.nickname = nickname
        self.password = password
        self.messages = []
        self.controller = controller

    def send_message(self, nickname_to, text):
        self.controller.send_msg(self.nickname, nickname_to, text)

    def print_messages(self):
        for message in self.messages:
            formated_time = datetime.fromtimestamp(message.timestamp)
            print(f"*    {message.from_user} - {formated_time.strftime('%m/%d/%Y, %H:%M:%S')}\n"
                  f"*    {message.text}\n")
