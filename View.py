# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - сложить, 2 - отнять, 3 - разделить,4 - умножить,5 -возведение в степень,0 - выход")
    choice = input("Введи номер действия: ")

    x = int(input("введи первое число:"))
    y = int(input("введи второе число:"))
    return choice

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное число.")

