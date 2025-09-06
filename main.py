# main.py

# Ввод количества чисел
n = int(input("Введите количество чисел: "))

# Ввод чисел в список (целые числа)
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Вывод изначального массива
print("Изначальный массив:", numbers)

# Запрос направления сортировки
direction = input("Выберите направление сортировки (asc для возрастания, desc для убывания): ").strip().lower()

# Сортировка пузырьком
for i in range(n):
    for j in range(0, n-i-1):
        if (direction == "asc" and numbers[j] > numbers[j+1]) or \
           (direction == "desc" and numbers[j] < numbers[j+1]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Вывод отсортированного массива
print("Отсортированный массив:", numbers)
input()