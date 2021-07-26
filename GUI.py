from mediator import Mediator


class GUI:
    def __init__(self):
        self.is_working = True
        print("Elo!")
        print(
            "1: login\n"
            "2: New Account\n"
            "3: Exit"

        )
        self.mediator = Mediator()
        self.main_menu()

    def main_menu(self):

        while self.is_working:
            option = int(input("co robimy?: "))

            if option == 1:

                self.mediator.login()

            elif option == 2:

                self.mediator.create_user()
                self.mediator.login()

            elif option == 3:
                self.is_working = False

            if self.mediator.loged_user is not None:
                print("udalo sie")
