# ВВОД ДАННЫХ

a = 0
print('Введите сегодняшнюю дату в формате dd.mm.yyyy')
date = input() # строка с сегодняшней датой
while a == 0:
    if len(date) == 10: # проверяем формат сегодняшней даты

        try:
            check = int(date[0]) and int(date[1]) and int(date[3]) and int(date[4]) and int(date[6]) and int(date[7]) and int(date[8]) and int(date[9]) # проверяем возможность перевода нужных чисел из строки в числовой формат
        except: 
            print('Не могу понять что Вы написали... Попробуйте еще раз в правильном формате :)')
            date = input()
        else:
            
            d = int(date[0]+date[1]) 
            m = int(date[3]+date[4])
            y = int(date[6]+date[7]+date[8]+date[9])
            if(m<=12):
                if(d>=31 and m==2 or m==4 or m==6 or m==9 or m==11) or (d>31) or (d>28 and m==2):
                    if (d==29 and ((y%4==0 and y%100!=0) or y%400==0) and m==2):
                        a=1
                    else:
                        print('В это месяце чутка меньше дней, чем вы указали.')
                        date = input()
                else:
                    a = 1
            else:
                print('По моим данным в году 12 месяцев, а не ', m)
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
            if(bm<=12):
                if(bd>=31 and bm==2 or bm==4 or bm==6 or bm==9 or bm==11) or (bd>31) or (bd>28 and bm==2):
                    if (bd==29 and ((by%4==0 and by%100!=0) or by%400==0) and bm==2):
                        a=0
                    else:
                        print('В это месяце чутка меньше дней, чем вы указали.')
                        date = input()
                else:
                    a = 1
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
                  
if age < 0:
    print('Хотели меня обмануть??? Человек, который еще не родился, не мооожет написать сюда свои данные =)')
elif 0 <= age < 3:
    print('Ваш возраст:', age,'лет. А Вы читать-то умеете?')
elif 3 <= age < 6:
    print('Вам', age,'лет. Кто Вас в таком возрасте к компьютеру пустил?')
elif 6 <= age < 100:
    print('На данный момент Вам', age,'полных лет.')
elif 100 <= age < 120:
    print('Приветствую тебя долгожитель! Тебе', age,'лет!')
else:
    print('Вам', age,'лет. А Вы человек? о_0')

# ВЫВОД ЗАКОНЧЕН

input()
