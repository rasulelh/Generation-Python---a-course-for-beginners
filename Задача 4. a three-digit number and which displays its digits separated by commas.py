# Задача 4. Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую).

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(digit1, digit2, digit3, sep=',')