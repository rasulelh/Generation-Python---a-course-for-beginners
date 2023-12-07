# Напишите программу для нахождения цифр четырёхзначного числа.

# Формат входных данных
# На вход программе подаётся положительное четырёхзначное целое число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# Sample Input 1:

# 3281
# Sample Output 1:

# Цифра в позиции тысяч равна 3
# Цифра в позиции сотен равна 2
# Цифра в позиции десятков равна 8
# Цифра в позиции единиц равна 1

num = int(input())

d1 = (num // 10 ** 3) % 10
d2 = (num // 10 ** 2) % 10 
d3 = (num // 10 ** 1) % 10
d4 = (num // 10 ** 0) % 10

print("Цифра в позиции тысяч равна", d1)
print("Цифра в позиции сотен равна", d2)
print("Цифра в позиции десятков равна", d3)
print("Цифра в позиции единиц равна", d4)