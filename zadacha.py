a=0
while a!='q' and a!='Q':
    print("Решаемые задачи:\n 1. Определение скорости.\n 2. Определение массы.\n 3. Определение температуры по Цельсию.\n 4. Определение работы.\n 5. Определение кинетической энергии.\n 6. Определение потенциальной энергии.\n 7. Определние давления.\n 8. Определение теплоты.\n 9. Определение частоты.\n 10. Определение объёма цилиндра.\n")
    a=input('Введите номер задачи для решения или нажмите "Q" для выхода: ')
    if a==1:
        print('Задача определения скорости.\n')
        S=float(input('Введите расстояние в километрах: '))
        t=float(input('Введите время в часах: '))
        print('Скорость движения: ',S/t,' км/ч')
    elif a==2:
        print('Задача определения массы.\n')
        F=float(input('Введите силу в Ньютонах: '))
        a=float(input('Введите ускорение в м/с^2: '))
        print('Масса тела: ',F/a,' кг')
    elif a==3:
        print('Задача определения температуры в градусах по Цельсию.\n')
        T=float(input('Введите температуру в градусах по Фаренгейту: '))
        print('Температура в градусах по Цельсию: ',5*(T-32)/9,'\u2103')
    elif a==4:
        print('Задача определения работы.\n')
        F=float(input('Введите силу в Ньютонах: '))
        S=float(input('Введите расстояние в метрах: '))
        print('Работа по перемещению тела равна: ',F*S,' Дж')
    elif a==5:
        print('Определение кинетической энергии.\n')
        m=float(input('Введите значение массы в кг: '))
        v=float(input('Введите значение скорости в м/с: '))
        print('Кинтеическая энергия тела: ',m*v*v/2,' Дж')
    elif a==6:
        print('Задача определения потенциальной энергии.\n')
        m=float(input('Введите значение массы тела в килограммах: '))
        h=float(input('Введите значение высоты в метрах: '))
        g=float(input('Введите значение ускорения свободного падения в м/с^2: '))
        print('Потенциальная энергия тела: ',m*g*h,' Дж')
    elif a==7:
        print('Задача определения давления.\n')
        F=float(input('Введите силу в Ньютонах: '))
        S=float(input('Введите площадь в м^2: '))
        print('Давление: ',F/S,' Па')
    elif a==8:
        print('Задача определения теплоты.\n')
        m=float(input('Введите массу в килограммах: '))
        c=float(input('Введите удельную теплоёмкость в Дж/кг*\u2103: '))
        T=float(input('Введите изменение температуры в \u2103: '))
        print('Теплота: ',c*m*T,' Дж')
    elif a==9:
        print('Задача определения частоты.\n')
        T=float(input('Введите значение периода в секундах: '))
        if T==0:
            print('Колебания отсутствуют, их период не может быть равен 0.')
        else:
            print('Частота колебаний: ',1/T,' Гц')
