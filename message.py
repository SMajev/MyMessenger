from datetime import datetime


class Message:
    def __init__(self, from_user, to_user, text):
        self.from_user = from_user
        self.to_user = to_user
        self.text = text
        self.timestamp = datetime.now().timestamp()
