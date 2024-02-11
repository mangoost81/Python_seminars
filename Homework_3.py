# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 3, 4, 5]
# k = 3

# count = 0
# for i in list_1:
#     if i == k:
#         count +=1
# print(count)


# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k 
# и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.

# a = [1, 2, 3, 4, 5, 16, 6]
# b = 12



# num = list()
# number=0
# for i in range (len(a)):
#     num.append(abs(a[i]-b)) 

# b = num.index(min(num))
# print(num)
# print(b)
# print(a[b])

# print(min(a, key=lambda c:abs(c-b)))


# english = {1:"AEIOULNSTR", 2:"DG", 3:"BCMP",
#            4:"FHVWY", 5:"K", 8:"JX", 10:"QZ"}

# russian = {1:"АВЕИНОРСТ", 2:"ДКЛМПУ", 3:"БГЁЬЯ",
#             4:"ЙЫ", 5:"ЖЗХЦЧ", 8:"ШЭЮ", 10:"ФЩЪ"}

# Это с инвертированными ключами-значениями:
english = {"AEIOULNSTR":1, "DG":2, "BCMP":3, 
           "FHVWY":4, "K":5, "JX":8, "QZ":10} 

russian = {"АВЕИНОРСТ":1, "ДКЛМПУ":2, "БГЁЬЯ":3, 
            "ЙЫ":4, "ЖЗХЦЧ":5, "ШЭЮ":8, "ФЩЪ":10}


word = "DErrim"



count = 0
for letter in word:
    for key in russian:
        if letter.upper() in key:
            count += russian.get(key)

if count > 0:
    print(count)

count = 0
for letter in word:
    for key in english:
        if letter.upper() in key:
            count += english.get(key)

if count > 0:
    print(count)

