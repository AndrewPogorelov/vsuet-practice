#  В переменной age хранится возраст. Вывести на экран "Поздравляем вы поступили в ВГУИТ",
#если age больше или равно "16", или если age меньше 16 - "Сначала нужно окончить школу!".
#     1.Проверить, что значение age больше 0 и меньше 75.
#     2.Проверить, что поступающего зовут не Иван.
#     3.Если Абитуериенту меньше 16 вывести на экран сколько лет ему еще учиться в школе.

print('Сколько вам лет?')
age=int(input())
print('Как вас зовут?')
name=input()
if name!='Иван':
    if age>0 and age<75:
        if age>=16:
            print('Поздравляем вы поступили в ВГУИТ')
        else:
            print('Сначала нужно окончить школу!')
            print('Сколько лет осталось учиться?')
else:
    print('Сколько лет осталось учиться?')
    name=input()
    print('Ну иди и учись!')
