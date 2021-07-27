from message import Message
from user import User
import pickle


class Controller():
    def __init__(self):
        self.users = self.read_users_from_file()
        self.logged_user = None

    def log_in(self, nickname, password):
        print(self.users)
        print(self.logged_user)
        for user in self.users:
            if nickname == user.nickname:
                if password == user.password:
                    self.logged_user = user.nickname
                    return self.logged_user

            else:
                print("No user!")
        print(self.logged_user)

    def log_out(self):
        decision = input("Are you sure? ((y)es/(n)o): ")
        if decision == "y" or "yes":
            self.logged_user = None

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

    def save_users_to_file(self, user_list):
        with open("users.pickle", "wb") as fuw:
            pickle.dump(user_list, fuw)

    def read_users_from_file(self):
        with open("users.pickle", "rb") as fur:
            data = pickle.load(fur)
            return data
