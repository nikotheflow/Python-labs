#ввод чисел пользователем
print('Введите числа через запятую')
lst = input().split(',')

'''
#заданный список чисел для проверки работоспособности программы
lst = ['-1', '7', '-54.6', '0', '2 + 3i', '43.4', '-7', '25', '14', '28', '-1 + 3i', '19']
'''

#создание списков
N = []
Z = []
Q = []
comp = []
even = []
odd = []
simple = []

for i in lst:
    try:
        #нахождение натуральных чисел
        if float(i) > 0 and str(int(float(i))) == i:
            N.append(i)
        #нахождение целых чисел
        if str(int(float(i))) == i:
            Z.append(i)
        #нахождение рациональных чисел
        if float(i) != 0:
            Q.append(i)
        #нахождение четных чисел
        if float(i) % 2 == 0 and float(i) != 0:
            even.append(i)
        #нахождение нечетных чисел
        if float(i) % 2 == 1 and float(i) != 0:
            odd.append(i)
    except ValueError:
        pass       

#нахождение комплексных чисел
for num in lst:
    for sym in num:
        if sym == 'i':
            comp.append(num)
    
#нахождение простых чисел
for i in N:
    num = int(i)
    div = 2
    while num > div and (num % div) != 0:
        div += 1
    if num == div:
        simple.append(i)   

#вывод полученных списков
print('Натуральные: ', end = '')
print(', '.join(N))

print('Целые: ', end = '')
print(', '.join(Z))

print('Рациональные: ', end = '')
print(', '.join(Q))

print('Комплексные: ', end = '')
print(', '.join(comp))

print('Четные: ', end = '')
print(', '.join(even))

print('Нечетные: ', end = '')
print(', '.join(odd))

print('Простые: ', end = '')
print(', '.join(simple))
