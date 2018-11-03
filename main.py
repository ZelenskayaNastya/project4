import random
print('Введите слово из списка букв: А Е Н О С Т')
foo = ['А','Е','Н','О','С','Т']
y = random.sample(foo, 4)
word = (''.join(y))


option = []
i = 1
D = 0
B = 0
while word != option:
    print()
    print('Попытка №', i)
    option = input()
    option = option.upper()
    T = 0
    for y in option:
        if y == word[0] or y == word[1] or \
                y == word[2] or y == word[3]:
            T += 1
    i += 1
    D = 0
    B = 0
    if i > 10:
        print('Вы проиграли:', word)
        break
    if word[0] == option[0]:
        D += 1
    else:
        B += 1
    if word[1] == option[1]:
        D += 1
    else:
        B += 1
    if word[2] == option[2]:
        D += 1
    else:
        B += 1
    if word[3] == option[3]:
        D += 1
    else:
        B += 1
    print('На "своем месте":', D)
    print('На "чужем месте":', T - D)
if word == option:
    print('Вы выиграли!')
