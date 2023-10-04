def proverka(x):
    if isinstance(x, list):
        count_even = 0
        max_num = float('-inf')
        i = 0
        while i < len(x):
            if x[i] % 2 == 0:
                count_even += 1

            if x[i] > max_num:
                max_num = x[i]

            if x[i] < 0:
                del x[i]
            else:
                i += 1

        print("Количество четных чисел в списке:", count_even)
        print("Максимальное число в списке:", max_num)
        print("Полученный список после удаления отрицательных элементов:", x)

    elif isinstance(x, int):
        reversed_number = int(str(x)[::-1])
        print("Перевернутое число:", reversed_number)

    elif isinstance(x, dict):
        sorted_dict = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
        print("Отсортированный словарь:", sorted_dict)

    elif isinstance(x, str):
        element_count = dict()
        for char in x:
            if char in element_count:
                element_count[char] += 1
            else:
                element_count[char] = 1
        print("Количество вхождений каждого символа:", element_count)

    else:
        print("Некорректный тип данных.")


while True:
    print("Меню:")
    print("1. Ввести число")
    print("2. Ввести словарь")
    print("3. Ввести строку")
    print("4. Ввести список")
    print("0. Выход")

    choice = input("Введите номер выбранного варианта: ")

    if choice == '1':
        while True:
            try:
                x = int(input("Введите целое положительное число: "))
                if x > 0:
                    break
                else:
                    print("Ошибка! Введено некорректное число.")
            except ValueError:
                print("Ошибка! Введено некорректное число.")
        proverka(x)

    elif choice == '2':
        keys = input("Введите ключи словаря через пробел: ")

        while True:
            try:
                values = input("Введите значения словаря через пробел (должны быть целые числа): ")
                value_list = [int(value) for value in values.split()]

                if len(keys.split()) == len(value_list):
                    break
                else:
                    print("Ошибка! Количество ключей и значений не совпадает.")
            except ValueError:
                print("Ошибка! Введено некорректное число.")

        x = dict(zip(keys.split(), value_list))
        proverka(x)

    elif choice == '3':
        print("Вы выбрали Вариант 3")
        string = input("Введите строку: ")
        proverka(string)

    elif choice == '4':
        print("Вы выбрали Вариант 4")
        while True:
            elements = input("Введите элементы списка через пробел: ")
            try:
                x = [int(num) for num in elements.split()]
                proverka(x)
                break
            except ValueError:
                print("Ошибка! Введены некорректные элементы списка. Пожалуйста, введите только числа.")

    elif choice == '0':
        print("Программа завершена.")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")