def i(a):
    return a

print(i(5))

# -----------
i_1 = lambda a: a

print(i_1(5))

# -----------

print((lambda a: a)(5))


lst = '1 2 4 8 9'.split()

print(lst)


lst_1 = list(map(int, lst))

print(lst_1)


lst_2 = list(map(lambda a: a + 2, lst_1))

print(lst_2)


lst_3 = list(filter(lambda a: 0, lst_1))

print(lst_3)

# ------------

lst_new = [(6, 8), (3, 7), (3, 2)]

lst_4 = list(filter(lambda a: (a[0] + a[1]) < 10, lst_new))

print(lst_4)


print(*max(orbits, key = lambda pair: pair[0] * pair[1] * (pair[0] != pair[1])))