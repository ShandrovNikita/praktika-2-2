a=0
while a!='q' and a!='Q':
    print("Решаемые задачи:\n 1. Определение скорости.\n 2. Определение массы.\n 3. Определение температуры по Цельсию.\n 4. Определение работы.\n 5. Определение кинетической энергии.\n 6. Определение потенциальной энергии.\n 7. Определние давления.\n 8. Определение теплоты.\n 9. Определение частоты.\n 10. Определение объёма цилиндра.\n")
    a=input('Введите номер задачи для решения или нажмите "Q" для выхода: ')
    if a==1:
        print('Задача определения скорости.\n')
        S=float(input('Введите расстояние в километрах: '))
        t=float(input('Введите время в часах: '))
        print('Скорость движения: ',S/t,' км/ч')
        


