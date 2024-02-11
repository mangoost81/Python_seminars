# # На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
#  Ваша задача - определить минимальное количество монеток, которые нужно перевернуть,
# чтобы все монетки лежали одной и той же стороной вверх.

# # Входные данные:

# # На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1,
#  если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# # Выходные данные:

# # Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

# coins = [1, 0, 1, 1, 0]
# count_1 = 0
# count_2 = 0
# for i in coins:
#     if i == 0:
#         count_1 +=1
#     else:
#         count_2 +=1

# print(min(count_1, count_2))    



# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

# s = 12
# p = 27

# res = []
# for i in range(s + p):
#     if i == (s * i - p)**0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)


# n = 16
# s = 1

# while s<=n:
#     print(s)
#     s = s*2

#     print()


users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")