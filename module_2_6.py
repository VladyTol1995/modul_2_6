def get_numbers (number):
    numbers = ''
    for i in range (1, number):
        for j in range (2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                numbers += str(i) + str(j)
    return numbers
n = int(input("Введите число от 3 до 20: "))

result = get_numbers(n)
print(result)