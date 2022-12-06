# 9 Вариант
# Определить, сколько раз в тексте встречается заданное слово
def l():
    string_ele = input("Введите текст \n")
    word = input("Введите слово которое хотите посчитать - ")

    string_pro = string_ele.split(' ')
    count = 0
    for index in range(len(string_pro)):
        if string_pro[index] == word:
            count += 1
    print("Количество слов ", word, "равно -", count)
l()