from message import Message
from user import User


class Controller():
    def __init__(self):
        self.users = []

    def send_msg(self, from_user_nickname, to_user_nickname, text):
        user_to_instance = None
        for user in self.users:
            if to_user_nickname == user.nickname:
                user_to_instance = user
                break

        if user_to_instance:
            new_message = Message(from_user_nickname, to_user_nickname, text)
            user_to_instance.messages.append(new_message)
            print("Wysłano")

        else:
            print("No user!")
            print("yoyo")

    def create_user(self, nickname, password):
        user = User(nickname, password, self)
        self.users.append(user)
        return user

    def print_users(self):
        for i in range(len(self.users)):
            print(i, end=" ")
            print(self.users[i])
