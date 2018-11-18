import numpy as np
A = np.random.randint(-10, 10, (3, 3))
print("Матрица А")
print(A)
print("\n")
def polinom(a):
	koefs = []
	k0 = 1
	koefs.append(k0)
	k1 = - a[0][0] - a[1][1] - a[2][2]
	koefs.append(k1)
	k2 = a[0][0]*a[1][1] + a[0][0]*a[2][2] + a[1][1]*a[2][2] - a[1][2]*a[2][1] - a[0][1]*a[1][0] - a[0][2]*a[2][0]
	koefs.append(k2)
	k3 = -a[0][0]*a[1][1]*a[2][2] + a[0][0]*a[1][2]*a[2][1] + a[0][1]*a[1][0]*a[2][2] - a[0][1]*a[1][2]*a[2][0] - a[0][2]*a[1][0]*a[2][1] + a[0][2]*a[1][1]*a[2][0]
	koefs.append(k3)

	return koefs
	
def gurv(a):
	koefs = polinom(a)
	M = [[koefs[1],koefs[3],0],[koefs[0],koefs[2],0],[0,koefs[1],koefs[3]]]
	print ("Матрица Гурвица:")
	print (M)
	print ("\n")
	print ("Проверка устойчивости по Гурвицу:")
	if (koefs[1] > 0) and (koefs[2]*koefs[1]-koefs[3]*koefs[0] > 0) and (koefs[3]>0):
		return "Система устойчива"
	if (koefs[1] < 0) or (koefs[2]*koefs[1]-koefs[3]*koefs[0] < 0) or (koefs[3]<0):
		return "Система неустойчива"
	if (koefs[1] > 0) and (koefs[2]*koefs[1]-koefs[3]*koefs[0] > 0) and (koefs[3]==0):
		return "Система на апериодической гнанице устойчивости"	
	if (koefs[1] > 0) and (koefs[2]*koefs[1]-koefs[3]*koefs[0] == 0) and (koefs[3]>0):
		return "Система на колебательной гнанице устойчивости"
	


koefs = polinom(A)

print('Характеристический полином матрицы А')
print(str(koefs[0])+'sˆ3 + '+str(koefs[1])+'sˆ2 + '+str(koefs[2])+'s + '+str(koefs[3])+' = 0')

print(gurv(A))
