# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.

num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Сумма цифр =', last_digit + first_digit)