while True:
    try:
        rows = int(input("Введите количество строк: "))
        if rows <= 0:
            print("Число строк должно быть положительным.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

while True:
    try:
        columns = int(input("Введите количество столбцов: "))
        if columns <= 0:
            print("Число столбцов должно быть положительным.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")


def create_matrix(rows, columns):
    """Создает матрицу с заданным количеством строк и столбцов."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    element = float(input(f"Введите элемент [{i}][{j}]: "))
                    break
                except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите число.")
            row.append(element)
        matrix.append(row)
    return matrix


# Создание матрицы с использованием функции create_matrix
matrix = create_matrix(rows, columns)

sum_negative = 0
count_negative = 0

for j in range(columns):
    all_negative = True  # Переменная, указывающая, что все элементы столбца отрицательные
    for i in range(rows):
        if matrix[i][j] >= 0:
            all_negative = False  # Если хотя бы один элемент не отрицательный, меняем значение на False
            break  # Прерываем цикл, так как уже известно, что столбец не удовлетворяет условию

    if all_negative:
        for i in range(rows):
            sum_negative += matrix[i][j]
        count_negative += rows

print("Матрица:")
for row in matrix:
    print(row)


if count_negative == 0:
    sr_arif = 0
    print("В матрице нет столбца, в котором все элементы отрицательные")
else:
    sr_arif = sum_negative / count_negative
    print("Среднее арифметическое элементов столбца, в котором все элементы отрицательные:", sr_arif)