import time 

#создание матриц для проверки
matrix1 = [[2, 5, 7], [3, 1, 7], [4, 6, 1]]
matrix2 = [[7], [8], [9]]
matrix3 = [[3, 2, 1]]


def row(matrix):
	return len(matrix)


def col(matrix):
	return len(matrix[0])


def swap(matrix,i):
	k = 0
	if i == col(matrix) or i == row(matrix):
		pass
	else:
		for step in range (col(matrix)-i):
			if matrix[i][i] == 0:
				matrix[i], matrix[i + step] = matrix[i + step], matrix[i]
			else: 
				k = 1
	return matrix, k


def  check(matrix):
	list = []
	for i in range (0, row(matrix)):
		flag = 0
		for j in range(0, col(matrix)):
			if matrix[i][j] != 0: 
				flag = 1
		if flag == 0:
			list.append(i)

	step = 0
	for i in list:
		del matrix[i - step]
		step += 1

	list = []
	for j in range(0,len(matrix[0])):
		flag = 0
		for i in range (0, row(matrix)):
			if matrix [i] [j] != 0: 
				flag = 1
		if flag == 0:
			list.append(j)

	step = 0
	for j in list:
		for i in range(0,row(matrix)):
			del matrix[i][j - step]
		step += 1

	return matrix

def multiplication(matrix1, matrix2):
	i, j, k = 0, 0, 0
	resultLine = 0

	if row(matrix2) == col(matrix1):
		result = []
		for i in range(row(matrix1)):
			line=[]
			for j in range (len(matrix2[i])):
				for k in range(col(matrix1)):
					resultLine += matrix1[i][k] * matrix2[k][j]
				line.append(resultLine)
				resultLine = 0
			result.append(line)
	else:
		return "Перемножение матриц возможно."
	
	return result

def power(matrix,power):
	i, j, k, p = 0, 0, 0, 1
	result_power = 0

	if row(matrix) == col(matrix):
		new_matrix = []
		while p < power:
			p += 1
			for i in range (row(matrix)):
				line = []
				for j in range(col(matrix)):
					for k in range (row(matrix[i])):
						result_power += matrix[i][k] * matrix[k][j]
					line.append(result_power)
					resultPower = 0
				new_matrix.append(line)
	else:
		return "Матрица должна быть квадратной."

	return new_matrix


def rank(matrix,n):
	checkMatrix = check(matrix)
	fMatrix, k = swap(checkMatrix, n)
	minim = row(fMatrix) if (row(fMatrix)) <= col (fMatrix) else col(fMatrix)
	rank_g = row(matrix)
	N = n
	if (n < minim - 1) or k != 0:
		for i in range(n + 1, row(fMatrix)):
			koef = -fMatrix[i][n] / fMatrix[n][n]
			for j in range(n, col(fMatrix)):
				fMatrix[i][j] = koef * fMatrix[n][j] + fMatrix[i][j]
		return rank(fMatrix, n + 1)
	else:
		return rank_g


def observability_of_matrix(matrix1,matrix2):
	n = len(matrix2) * len(matrix2[0])
	result = [0] * n
	for i in range(n):
		result[i] = [0] * len(matrix2[0])
		
	result[0] = matrix2
	i = 0 
	while i < (len(matrix2[0]) - 1):
		i += 1
		result[i] = multiplication(matrix2,matrix1)
		matrix1 = power(matrix1,i + 1)
		
	result1 = [0] * n
	for i in range(n):
		result1[i] = []
		
	i = 0
	for j in range(len(matrix2[0])):
		for k in range(len(result[0])):
			result1[i] = result[j][k]
			i +=1
			
	return result1


def check_observability(matrix1,matrix2):
	rank_of_matrix = rank(observability_of_matrix(matrix1,matrix2),0)
	Columns = col(matrix2)
	if Columns == rank_of_matrix:
		return "Матрица наблюдаема."
	else:
		return "Матрица не является наблюдаемой."


def controllability_of_matrix(matrix1,matrix2):
	n = len(matrix2) * len(matrix2[0])
	result = [0] * n
	for i in range(n):
		result[i] = [0] * len(matrix2)
		
	result[0] = matrix2
	i = 0
	while i < (len(matrix2) - 1):
		i += 1
		result[i] = multiplication(matrix1,matrix2)
		matrix1 = power(matrix1,i + 1)
		
	result1 = [0] * len(matrix2)
	for i in range(len(matrix2)):
		result1[i] = []
		
	for i in range(len(matrix2)):
		for j in range(len(matrix2)):
			result1[i] = result1[i] + result[j][i]
			
	return result1


def check_controllability(matrix1,matrix2):
	rank_of_matrix = rank(controllability_of_matrix(matrix1,matrix2),0)
	rows = row(matrix2)
	if rows == rank_of_matrix:
		return "Матрица управляема."
	else:
		return "Матрица не является управляемой."

#вывод результатов на экран
print("Первая матрица: \n", matrix1)
print("Вторая матрица: \n", matrix2)
print("Третья матрица: \n", matrix3)
start_time = time.time()
print("Ранг матрицы равен:", rank(matrix1, 0))
print(check_observability(matrix1, matrix3))
print(check_controllability(matrix1, matrix2))
end_time = time.time()
time = end_time - start_time
print("Время вычисления: " + str(time))
