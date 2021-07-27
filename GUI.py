from controller import Controller


class GUI:
    def __init__(self):
        self.is_working = True
        print("Elo!")
        # menu_switch()
        self.controller = Controller()
        self.main_menu()

    def menu_switch(self):
        print(
            "1: login\n"
            "2: New Account\n"
            "3: Exit"

        )

    def main_menu(self):

        while self.is_working:
            if self.controller.logged_user is None:
                self.menu_switch()
                option = int(input("co robimy?: "))

                if option == 1:
                    user_nickname = input("Nickname: ")
                    user_password = input("Password: ")

                    self.controller.log_in(user_nickname, user_password)

                elif option == 2:
                    user_nickname = input("Nickname: ")
                    user_password = input("Password: ")
                    self.controller.create_user(user_nickname, user_password)
                    self.controller.log_in(user_nickname, user_password)

                elif option == 3:
                    self.controller.save_users_to_file(self.controller.users)
                    self.is_working = False

            elif self.controller.logged_user is not None:
                print("You are logged!")
                print(
                    "1: Send message\n"
                    "2: Show messages\n"
                    "3: Logged out\n"
                )
                decision = int(input("What's next?: "))

                if decision == 3:
                    self.controller.log_out()
