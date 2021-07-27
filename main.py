from controller import Controller
from GUI import GUI

msg = """Wzorzec projektowy Mediator jest podobny do wzorca Observer, 
w tym sensie, że opisuje sposób wykonywania żądania i jego obsługi.
Wzorzec ten warto zastosować, gdy w aplikacji, znajdziemy wiele komponentów, 
które w jakiś sposób się ze sobą komunikują."""


def main():
    gui = GUI()



if __name__ == "__main__":
    main()

    tomek = controller.create_user("Tomek", "12345")
    karolina = controller.create_user("Karolina", "54321")
    tomek.send_message("Karolina", msg)
    karolina.print_messages()
