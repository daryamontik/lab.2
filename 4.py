def calculate_arithmetic_progression(first_term, common_difference, n):
    try:
        if common_difference == 0:
            raise ValueError("Разность прогрессии не может быть равна нулю.")

        # Вычисляем сумму n членов арифметической прогрессии
        numerator = 2 * first_term + (n - 1) * common_difference
        sum_n = (n * numerator) / 2

        # Вычисляем последний член арифметической прогрессии
        last_term = first_term + (n - 1) * common_difference

        return sum_n, last_term

    except ValueError as ve:
        # Обрабатываем ошибку, когда разность равна нулю
        print("Ошибка:", str(ve))
        return None, None

    finally:
        # Блок finally выполняется всегда, независимо от того, было ли исключение или нет
        print("Выполнение блока finally.")


# Ввод данных пользователем
while True:
    try:
       first_term = int(input("Введите первый член арифметической прогрессии: "))
       break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

while True:
    try:
       common_difference = int(input("Введите разность арифметической прогрессии: "))
       break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

while True:
    try:
      n = int(input("Введите количество членов арифметической прогрессии: "))
      if n<=0:
          print("Количество членов прогрессии должно быть положительным")
      else:
          break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")


sum_n, last_term = calculate_arithmetic_progression(first_term, common_difference, n)

print("Сумма первых", n, "членов арифметической прогрессии:", sum_n)
print("Последний член арифметической прогрессии:", last_term)