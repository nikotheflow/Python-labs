import numpy as np
import time

#создание матриц для проверки
matrix1 = [[2, 5, 7], [3, 1, 7], [4, 6, 1]]
matrix2 = [[7], [8], [9]]
matrix3 = [[3, 2, 1]]

def observability_of_matrix(matrix1,matrix2):
	size = np.shape(matrix2)
	n = size[0] * size[1]
	result = [0] * n
	for i in range (n):
		result[i] = [0] * size[1]
		
	result[0] = matrix2
	i = 0 
	while i < (size[1] - 1):
		i += 1
		result[i] = np.dot(matrix2,matrix1)
		matrix1 = np.linalg.matrix_power(matrix1, i+1)
		
	result1 = [0] * n
	for i in range(n):
		result1[i] = []
		
	i = 0
	for j in range(size[1]):
		for k in range(len(result[0])):
			result1[i] =result[j][k]
			i += 1
			
	resultend = np.array ([result1[0], result1[1], result1[2]])
	return resultend


def check_observability(matrix1,matrix2):
	rank_of_matrix = np.linalg.matrix_rank(observability_of_matrix(matrix1,matrix2))
	size = np.shape(matrix2)
	n = size[1]
	if n == rank_of_matrix:
		return "Матрица наблюдаема."
	else:
		return "Матрица не является наблюдаемой."


def controllability_of_matrix(matrix1,matrix2):
	size = np.shape(matrix2)
	n = size[0] * size[1]
	result = [0] * n
	for i in range (n):
		result[i] = [0] * size[0]
		
	result[0] = matrix2
	i = 0
	while i < (size[0] - 1):
		i += 1
		result[i] = np.dot(matrix1,matrix2)
		matrix1 = np.linalg.matrix_power(matrix1, i + 1)
		
	result1 = [0] * size[0]
	for i in range(size[0]):
		result1[i] = []
		
	for i in range(size[0]):
		for j in range (size[0]):
			result1[i] = np. concatenate( [result1[i], result[j][i]])

	return result1


def check_controllability(matrix1,matrix2):
	rangMatrix = np.linalg.matrix_rank(controllability_of_matrix(matrix1,matrix2))
	size = np.shape(matrix2)
	n = size[0]
	if n == rangMatrix:
		return "Матрица управляема."
	else:
		return "Матрица не является управляемой."


#вывод результата вычислений на экран
print("Первая матрица: \n", matrix1)
print("Вторая матрица: \n", matrix2)
print("Третья матрица: \n", matrix3)
start_time = time.time()
print("Ранг матрицы равен:", np.linalg.matrix_rank(matrix1))
print(check_observability(matrix1, matrix3)) 
print(check_controllability(matrix1, matrix2))
end_time = time.time()
time = end_time - start_time
print("Время вычисления: " + str(time))
