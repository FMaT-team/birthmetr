# Birthday v1.2
# Created by spb-t13 & gen-maksim

# ВВОД ДАННЫХ

a = 0
print('Введите сегодняшнюю дату в формате dd.mm.yyyy')
date = input()
while a == 0:
    if len(date) == 10:

        try:
            check = int(date[0]) and int(date[1]) and int(date[3]) and int(date[4]) and int(date[6]) and int(date[7]) and int(date[8]) and int(date[9])
        except: 
            print('Не могу понять что Вы написали... Попробуйте еще раз в правильном формате :)')
            date = input()
        else: 
            d = int(date[0]+date[1]) 
            m = int(date[3]+date[4])
            y = int(date[6]+date[7]+date[8]+date[9])
            if(m<=12):
                if(d >= 31 and (m == 2 or m == 4 or m == 6 or m == 9 or m == 11)) or (d > 31) or (d > 28 and m == 2):
                    if (d == 29 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and m == 2):
                        a = 1
                    else:
                        print('В это месяце чутка меньше дней, чем вы указали.')
                        date = input()
                else:
                    a = 1
            else:
                print('По моим данным в году 12 месяцев, а не', m)
                date = input()
    
    else:
        print('Кажется, вы ошиблись, введите сегодняшнюю дату в формате dd.mm.yyyy еще разок ;)')
        date = input()

print('Введите дату Вашего рождения в формате dd.mm.yyyy')
bdate = input()
while a == 1:
    if len(bdate) == 10: 
        
        try:
            check = int(bdate[0]) and int(bdate[1]) and int(bdate[3]) and int(bdate[4]) and int(bdate[6]) and int(bdate[7]) and int(bdate[8]) and int(bdate[9])
        except:
            print('Где-то закаралась ошибка, нужно исправить!!')
            bdate = input()
        else:
            bd = int(bdate[0]+bdate[1])
            bm = int(bdate[3]+bdate[4])
            by = int(bdate[6]+bdate[7]+bdate[8]+bdate[9])
            if(bm <= 12):
                if(bd>=31 and (bm == 2 or bm == 4 or bm == 6 or bm == 9 or bm == 11)) or (bd > 31) or (bd > 28 and bm == 2):
                    if (bd == 29 and ((by % 4 == 0 and by % 100 != 0) or by % 400 == 0) and bm == 2):
                        a = 0
                    else:
                        print('В это месяце чутка меньше дней, чем вы указали.')
                        date = input()
                else:
                    a = 0
            else:
                print('По моим данным в году 12 месяцев, а не ', bm)
                date = input()
            
    else:
        print('Упс, что-то пошло не так, введите дату Вашего рождения в формате dd.mm.yyyy снова =)')
        bdate = input()

# ВВОД ДАННЫХ ЗАКОНЧЕН

# ВЫЧИСЛЕНИЕ

a = by-y
if bm > m:
    age = y - by - 1
elif bm == m:
    if bd > d:
        age = y - by - 1
    else:
        age = y - by
else:
    age = y - by

# ВЫЧИСЛЕНИЕ ЗАКОНЧЕНО

# ВЫВОД

f = age % 10                  
if age < 0:
    print('Хотели меня обмануть??? Человек, который еще не родился, не мооожет написать сюда свои данные =)')
elif 0 <= age < 3:
    if age == 1:
        print('Ваш возраст: 1 год. А Вы читать-то умеете?')
    elif age == 2:
        print('Вам 2 года. Когда вы познакомились с компьютером?')
    else:
        print('Интересно, а Вы в 0 лет ходить научились уже?')
elif 3 <= age < 6:
    if age == 3 or age == 4:
        print('Сейчас вам', age,'года.')
    else:
        print('Вам', age,'лет. Кто Вас в таком возрасте к компьютеру пустил?')
elif 6 <= age < 100:
    if age > 20 and f == 1:
        print('Эта земля носит Вас уже', age, 'год.')
    elif age > 20 and 1 < f < 5:
        print('Вы живете ужe', age, 'года.')
    else:
        print('Ha данный момент Вам', age,'полных лет.')
elif 100 <= age <= 120:
    if age == 101:
        print('Вы прожили невероятно долгую жизнь, длиной в 101 год.')
    elif 101 < age < 105:
        print('Преклоняюсь перед таким человеком. Ваш возраст', age, 'года.')
    else:
        print('Приветствую тебя долгожитель! Тебе', age,'лет!')
elif 120 < age < 200:
    if f == 1:
        print('Вы живете на этой земле уже', age, 'год. Серьезно? :D')
    elif 1 < f < 5:
        print('Вы либо самый старый человек в мире, либо врете, что Вам', age, 'года.')
    else:
        print('По моим подсчетам Вам', age,'лет. Вы вообще человек? о_0')
else:
    print('Ну это уже перебор. Я ни за что не поверю, что вам столько лет.')

# ВЫВОД ЗАКОНЧЕН

input()
