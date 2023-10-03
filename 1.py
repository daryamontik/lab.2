def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(x):
    count = 0
    num = 2
    while count < x:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

while True:
    try:
        x = int(input('Введите номер простого числа: '))
        if x <= 0:
            print("Номер простого числа должен быть положительным.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

result = prime(x)
print(result)
