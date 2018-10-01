print('Введите, разделяя пробелом, вероятности происхождения события у Сони, Максима и Саши.')
C = 8
D = 300

while 1 == 1:
    #ввод значений вероятностей
    Sonya, Maksim, Sasha = map(float, input().split())
    #сообщение о некорректно введеных значениях
    if ((Sonya > 1) or (Maksim > 1) or (Sasha > 1) or (Sonya < 0) or (Maksim < 0) or (Sasha < 0)):
            print('Значения вероятностей должны лежать в пределах от 0 до 1, попробуйте еще раз.')
            continue
    #подсчет вероятности
    else:
            result = float((1 - (1 - Sonya)**(D/C))*(1 - Maksim**(D/C))*(1 - Sasha**(D/C)))
            result = round(result, 3)
            print('Вероятность ужасной прокрастинации Сони равна', result)
            break
