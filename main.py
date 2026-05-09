


# 3. 🔍 Поиск контакта

def find_contact():
    search_contact= input("Введите имя или номер телефона:")
    file_open = open("contacts.txt", "r", encoding="UTF-8")
    found = False
    for i in file_open:
        if search_contact.lower() in i.lower():
            print(i.strip())
            found = True
    if not found:
        print("❌ Контакт не найден.")


# Шаг 2: “Добавить контакт”

def add_contacts():
    name = input("Введите имя: ")
    while name == "":
        print("❌ Имя не может быть пустым. Введите имя ещё раз.")
        name = input("Введите имя: ")
    mobile_tel = input("Введите телефон:")
    while not mobile_tel.isdigit() or len(mobile_tel)!= 12:
        print("❌Телефон должен содержать 12 цифр.")
        mobile_tel = input("Введите телефон:")
    email = input("Введите email: ")
    while "@" not in email or "." not in email or email=="":
        print("❌ Некорректный email. Email должен содержать @ и .")
        email = input("Введите email: ")
    with open("contacts.txt", "a", encoding="UTF-8") as file:
        file.write(f"{name} | {mobile_tel} | {email}\n ")


# Шаг 1. Работа без файлов (самый важный старт)
def run_menu():
    while True:
        print("Выберите действие:")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Обновить контакт")
        print("5. Просмотреть контакты")
        print("6. Выйти")
        choice = input("Введите число (1-6): ")
        if choice == "1":
            add_contacts()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            print("Hello")
        elif choice == "4":
            print("Вы выбрали: Обновить контакт")
        elif choice == "5":
            print("Вы выбрали: Просмотреть контакты")
        elif choice == "6":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

run_menu()



