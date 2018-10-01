#coding=utf8
import random
import math

#Функция ввода массива случайных натуральных чисел 
#(для удобства тестирования)
def randArr(length):
	numbers = []
	for i in range(length):
		numbers.append(random.randint(0,100))
	return numbers

#Функция ввода массива натуральных чисел пользователем
def arrImput():
	print("Введите массив натуральных чисел\nЧисла будут записаны до введения пробела")
	numbers = []
	while(1):
		number = raw_input()
		if(number == ' '):
			break 
		else:
			if (int(number) < 0):
				print("Введите натуральное число")
			else:
				numbers.append(number)
	numbers = list(map(int, numbers))
	return numbers

#Пузырьковая сортировка
#Элементы от нулевого до предпоследнего сдвигаются по массиву вправо, пока не встанут слева от большего элемента
def bubbleSort(numbers):
	length = len(numbers)-1
	for i in range(length):
		for j in range(length-i):
			if(numbers[j+1]<numbers[j]):
				temp = numbers[j+1]
				numbers[j+1] = numbers[j]
				numbers[j] = temp
	return numbers

#Гномья сортировка
def gnomeSort(numbers):
	i = 1
	#Массив проверяется, начиная с первого элемента и до последнего
	while (i<len(numbers)):
		#Если элемент больше предыдущего, индекс увеливается и происходит шаг по массиву вперед
		if(numbers[i]>=numbers[i-1]):
			i += 1
		else:
			#Если элемент меньше предыдущего, они меняются местами
			tmp = numbers[i-1]
			numbers[i-1] = numbers[i]
			numbers[i] = tmp
			#И происходит шаг назад по массиву
			i -= 1
			if (i == 0):
				i = 1
	return numbers

#Блочная сортировка
def bucketSort(numbers, depth = 0):
	numSum = 0
	flag = 0
	#Создается двухмерный массив блоков
	#20 блоков для возможности работы с отрицательными числами
	buckets = [] 
	for i in range(20):
		buckets.append([])

	#Каждое число из заданного массива распределяется по блокам
	#Индекс блока в массиве блоков для данного числа такой же, как цифра данного числа, находящаяся на порядке таком же, как глубина рекурсии
	for i in range(len(numbers)): 
		if(numbers[i] < 0): #Для работы с отрицательными числами
			token = (-1)*numbers[i]
			flag = 1
		else:
			token = numbers[i]
			flag = 0
		remainder = (token // (10 ** depth))%10 #Определение цифры
		numSum += remainder #Сумма цифр всех чисел на данном уровне рекурсии
		#Определение индексов чисел
		if(flag == 1):
			index = 9 - remainder
		else:
			index = 10 + remainder
		buckets[index].append(numbers[i])

	#Перезапись массива из блоков
	numIndex = 0 
	for i in range(20):
		for j in range(len(buckets[i])):
			numbers[numIndex] = buckets[i][j]
			numIndex += 1


	depth += 1
	#Если в данном порядке цифры всех чисел не равны нулю, переход на следующий уровень рекурсии - седующий порядок
	if(numSum != 0):
		bucketSort(numbers, depth)

	return numbers

#Пирамидальная сортировка
def heapSort (numbers):
	#Свап элементов массива
    def swapItems (i1, i2):
        if numbers[i1] < numbers[i2]:
        	tmp =  numbers[i1]
        	numbers[i1] = numbers[i2]     
        	numbers[i2] = tmp

    #Спуск больших элементов вниз
    def siftDown (parent, limit):
        while (1):
            child = parent * 2 + 2
            #выбирается наименьший потомок
            if child < limit:
                if numbers[child] < numbers[child - 1]:
                    child -= 1
                #выбранный потомок свапается с предком
                swapItems(parent, child)
                #за предка принимается потомок
                parent = child
            else:
                break
    #Тело функции heapSort
    length = len(numbers)
    #Формирование первичной пирамиды
    for i in range((length // 2) - 1, -1, -1):
        siftDown(i, length)
    #Окончательное упорядочивание
    for i in range(length - 1, 0, -1):
        swapItems(i, 0)
        siftDown(0, i)

    return numbers


			
#Ввод массива и вывод результатов сортировок
numbers = arrImput()

print("Array "+str(numbers))

bubbleSorted = bubbleSort(numbers)
print("\nBubble Sort \t"+str(bubbleSorted))

gnomeSorted = gnomeSort(numbers)
print("Gnome Sort \t"+str(gnomeSorted))

buckedSorted = bucketSort(numbers)
print("Bucket Sort \t" + str(buckedSorted))

heapSorted = heapSort(numbers)
print("Heap Sort \t" + str(heapSorted))
