from controller import Controller


class GUI:
    def __init__(self):
        self.is_working = True
        print("Elo!")
        print(
            "1: login\n"
            "2: New Account\n"
            "3: Exit"

        )
        self.controller = Controller()
        self.main_menu()

    def main_menu(self):

        while self.is_working:
            option = int(input("co robimy?: "))

            if option == 1:
                user_nickname = input("Nickname: ")
                user_password = input("Password: ")

                self.controller.log_in(user_nickname, user_password)

            elif option == 2:

                self.controller.create_user()
                self.controller.login()

            elif option == 3:
                self.is_working = False

            if self.controller.logged_user is not None:
                print("udalo sie")
