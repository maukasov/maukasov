import random
print('Гениратор случайных чисел для Альбины Альбертовны, от Мансура 7С!')
print('Если хотите выйти, то в вопросе про класс напишите 0')
while True:
    while True:
        b = int(input('Сколько человек в классе(Не более 30): '))
        c = str(b)
        if b > 30:
            pass
        elif b == 000:
            print('Поставьте пожалуйста Мансуру 5!')
            exit('Вы завершили программу!')
        else:
            break
    while True:
        a = int(input('Сколько человек вы хотите спросить(1-' + c + '): '))
        if a >= b+1:
            pass
        else:
            print(random.sample(range(1, b+1), a))
            break
