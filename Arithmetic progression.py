# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. 

# Тестовые данные 🟢
# Sample Input 1:

# 1
# 2
# 3
# Sample Output 1:

# YES
# Sample Input 2:

# 1
# 2
# 4
# Sample Output 2:

# NO


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

difference_num_2_num1 = num_2 - num_1
difference_num_3_num2 = num_3 - num_2

if difference_num_2_num1 == difference_num_3_num2:
    print("YES")
else:
    print("NO")
