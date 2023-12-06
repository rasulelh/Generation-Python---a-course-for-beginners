# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

num = int(input())
digit3 = num % 10
digit2 = (num % 100) // 10
digit1 = num // 100
sum = digit1 + digit2 + digit3
product_of_digits = digit1 * digit2 * digit3

print('Сумма цифр =', sum)
print('Произведение цифр =', product_of_digits)