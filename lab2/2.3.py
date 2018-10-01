#coding=utf8
import random, numpy as np
from math import sqrt, log

#функция для создания матрицы со случайными элементами от 1 до 30
n = int(input('Введите размер квадратной матрицы: '))
def creatArray(n):
    return [[random.randint(1,30) for i in range(n)] for j in range(n)]


#создаем матрицу и выводим на экран
A = np.array(creatArray(n))
print('Первоначальная матрица: \n', A, '\n')

mathExpVals = []
despVals = []

def rowMathExp(i):
	 sigma = 0.0
	 for j in range(n):
	 	sigma += A[i][j]
	 mathExp = sigma/15
	 return mathExp

def rowDispersion(i):
	sigma = 0
	for j in range(n):
		sigma += A[i][j]**2
	dispersion = (sigma/n) - rowMathExp(i)**2
	return dispersion

def mathExpAndDisp():
	for i in range(n):
		mathExpVals.append(rowMathExp(i))
		despVals.append(rowDispersion(i))

def mathExpLists(x,y):
	sigma = 0
	for i in range(n):
		sigma += x[i]*y[i]
	return sigma/n

def mathExpList(x):
	sigma = 0
	for a in x:
		sigma += a
	return sigma/n

def centeredLin(i): 
	x = []
	mathExpX = rowMathExp(i)
	for j in range(n):
		x.append(A[i][j] - mathExpX)
	return x


def centeredExp(i): 
	x = []
	for j in range(n):
		x.append(log(A[i][j])) 
	mathExpX = mathExpList(x)
	for j in range(n):
		x[j] = x[j] - mathExpX
	return x

def dispExp(i):
	x = []
	for j in range(n):
		x.append(log(A[i][j]))
	xMathExp = mathExpList(x)
	for j in range(n):
		x[j] = x[j] ** 2
	sigma = 0
	for j in range(n):
		sigma += x[j] ** 2
	disp = sigma / n - xMathExp ** 2
	return disp

def dispersion(i):
	sigma = 0
	for j in range(n):
		sigma += A[i][j]**2
	return sigma/n - rowMathExp(i)**2

def cor(i,j):
	xVar = dispersion(i)
	yVar = dispersion(j)
	xCentered = centeredLin(i)
	yCentered = centeredLin(j)
	xExpCentered = centeredExp(i)
	xExpDisp = dispExp(i)
	rLin = mathExpLists(xCentered, yCentered)
	RLin = rLin / (sqrt(abs(xVar * yVar)))
	rExp = mathExpLists(xExpCentered, yCentered)
	RExp = rExp / (sqrt(abs(xExpDisp * yVar)))
	result = [RLin, RExp]
	return result


mathExpAndDisp()
for i in range(n):
	print("Ряд:" + str(i+1) + " математическое ожидание: " + str(mathExpVals[i]) + " дисперсия: " + str(despVals[i]))

corCoef = []

for i in range(n):
	for j in range(n):
		corCoef.append(cor(i, j))

print("\n\nВведите погрешность: ")
error = float( input() )

print("Линейно коррелируют ряды: ")
for i in range(n):
	for j in range(i+1, n):
		if abs(corCoef[i * n + j][0]) > 1 - error:
			print(str(i + 1) + " ==> " + str(j + 1) + ", коэф корреляции = " + str(corCoef[i * n + j][0]))


print("\n\nЭкспоненциально коррелируют ряды: ")
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		if (abs(corCoef[i * (n-1) + j][1]) > 1 - error):
			print(str(i + 1) + " ==> " + str(j + 1) + ", коэф корреляции = " + str(corCoef[i * (n-1) + j][1]))

