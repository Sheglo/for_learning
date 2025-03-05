from Model import *
from View import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    while True:
        choice = display_menu()
        if choice == '1':
            return x + y
        elif choice == '2':
            return x - y
        elif choice == '3':
            if y == 0:
                return "Ошибка: деление на ноль."
            return x / y
        elif choice == '4':
            return x * y
        elif choice == '5':
            return x ** y
        else:
            return "Некорректный выбор."

    def main():
        while True:
            choice = display_menu()
            if choice == '0':
                print("Выход из программы.")
                break
        else:
            show_message("Неверный выбор, попробуй снова")

main()