import random, numpy as np

#функция для создания матрицы со случайными элементами от 1 до 30
def creatArray():
    n = int(input('Введите размер квадратной матрицы: '))
    return [[random.randint(1,30) for i in range(n)] for j in range(n)]


#создаем матрицу и выводим на экран
A = np.array(creatArray())
print('Первоначальная матрица: \n', A, '\n')


#удаление десяти случайных элементов (считаем, что если элемент равен нулю, он удален)
A_del = np.copy(A)
zero = 0 #количество удаленных элементов
while zero != 10:
    #берем случайный элемент
    i_rand = random.randint(0, A_del.shape[0]-1)
    j_rand = random.randint(0, A_del.shape[0]-1)
    #проверяем, удален ли элемент, и удаляем, если нет
    if A_del[i_rand][j_rand] == 0:
        continue
    else:        
        A_del[i_rand][j_rand] = 0
        zero += 1
        
print('Полученная после удаления десяти элементов матрица: \n', A_del, '\n')


#метод винзорирования
A_vin = np.copy(A_del)

for i in np.arange(A_vin.shape[0]):
    for j in np.arange(A_vin.shape[1]):
        if A_vin[i, j] == 0:
            if A_vin[i, j-1] != 0 and (j-1) >= 0:
                A_vin[i, j] = A_vin[i, j-1]
            else:
                if A_vin[i, j+1] != 0 and (j+1) <= (A_vin.shape[0] - 1):
                    A_vin[i, j] = A_vin[i, j+1]
                else:
                    A_vin[i, j] = 1

print('Восстановленная методом винзорирования матрица: \n', A_vin, '\n')


#метод линейной аппроксимации
A_lin = np.copy(A_del)

for i in np.arange(A_lin.shape[0]):
    for j in np.arange(A_lin.shape[1]):
        if A_lin[i, j] == 0:
            A_lin[i, j] = np.mean(A_lin[i])

print('Восстановленная методом линейной аппроксимации матрица: \n', A_lin, '\n')


#метод корреляционного восстановления       
A_cor = np.copy(A_del)

n = int(input('Номер восстанавливаемого ряда: '))
m = int(input('Номер коррелирующего с указанным ряда: '))

try:
    for j in range(0, A_cor.shape[0]):
        if A_cor[n, j] == 0:
            if j != A_cor.shape[0]: 
                A_cor[n, j] = (A_cor[n, j+1]*A_cor[m, j+1])/A_cor[m, j]
            elif j == A_cor.shape[0]: #для послежнего столбца
                A_cor[n, j] = (A_cor[n, j-1]*A_cor[m, j-1])/A_cor[m, j]
except BaseException: #избегаем ошибки в случае, если утеряно слишком много данных
    print('\nВосстановить удалось не все данные')
    pass

print('\nВосстановленная методом корреляционного восстановления матрица: \n', A_cor, '\n')
