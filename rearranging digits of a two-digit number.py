# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.

num = int(input())
last_digit = num % 10
first_digit = num // 10

print('Искомое число =', last_digit * 10 + first_digit)
