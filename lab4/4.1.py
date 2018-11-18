import random
import matplotlib.pyplot as plt

num = 50 

#Завтра как вчера
def tomAsYest(nums):
	filtered = []
	filtered.append(nums[0])
	length = len(nums)
	for i in range(1,length):
		filtered.append(nums[i-1])
	return filtered

#Скользящее среднее
def movAv(nums):
	filtered = []
	filtered.append(nums[0])
	filtered.append((nums[0]+nums[1])/2.0)
	summ = nums[0] + nums[1]
	n = 3
	length = len(nums)
	for i in range(2,length):
		summ += nums[i]
		filtered.append( 1.0 * summ / n )
		summ -= nums[i-2]
	return filtered

#Взвешанное скользящее среднее
def weightedMovAv(nums):
	weightNums = [0.06, 0.09, 0.16, 0.29, 0.4]
	filtered = [nums[0]]
	length = len(nums)
	for i in range(1, length):
		y = 0
		weightSum = 0
		for j in range(len(weightNums)):
			if (i - (len(weightNums) - j)) < 0:
				continue
			y += nums[i - (len(weightNums) - j)] * weightNums[j]
			weightSum += weightNums[j]

		filtered.append(y / weightSum)
	return filtered

#Экспоненциальное скользящее среднее
def expFilt(nums):
	filtered = []
	alpha = 0.2
	filtered.append(nums[0])
	length = len(nums)
	for i in range(1,length):
		filtered.append(alpha*nums[i]+(1-alpha)*filtered[i-1])
	return filtered

def createList(left, right, num):
	dat = []
	for i in range(num):
		dat.append(random.randint(left, right))
	return dat

nums = []
nums = createList(0,40,num)
filter1 = tomAsYest(nums)
filter2 = movAv(nums)
filter3 = weightedMovAv(nums)
filter4 = expFilt(nums)


x = []
for i in range(num):
	x.append(i)

plt.subplot(2, 2, 1)
plt.title('Завтра как вчера')
plt.plot(x, nums, label='Исходные значения')
plt.plot(x, filter1, label='Сглаженные значения')
plt.legend()

plt.subplot(2, 2, 2)
plt.title('Скользящее среднее')
plt.plot(x, nums, label='Initial numbers')
plt.plot(x, filter2, label='Moving Avarage')

plt.subplot(2, 2, 3)
plt.title('Взвешанное скользящее среднее')
plt.plot(x, nums, label='Initial numbers')
plt.plot(x, filter3, label='Weighted Moving Avarage')

plt.subplot(2, 2, 4)
plt.title('Экспоненциальное скользящее среднее')
plt.plot(x, nums, label='Initial numbers')
plt.plot(x, filter4, label='Exponential Filter')


plt.grid()
plt.show()