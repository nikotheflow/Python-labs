#coding=utf8
#импортируем необходимые библиотеки
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import webbrowser 
import random
import matplotlib.pyplot as plt
import numpy as np
import math

rowsNumber = 18
def createData():
	xmin = int(raw_input("Введите минимальную абсциссу\t"))
	xmax = int(raw_input("Введите максимальную абсциссу\t"))
	while (xmax <= xmin):
		xmax = int(raw_input("Введите максимальную абсциссу (больше минимальной)\t"))
	ymin = int(raw_input("Введите минимальную ординату\t"))
	ymax = int(raw_input("Введите максимальную ординату\t"))
	while (ymax <= ymin):
		ymax = int(raw_input("Введите максимальную ординату (больше минимальной)\t"))

	coords = []

	xValues = set([random.randint(xmin, xmax) for i in range(rowsNumber)])
	while(len(xValues) != rowsNumber):
		xValues.add(random.randint(xmin, xmax))

	yValues = set([random.randint(ymin, ymax) for i in range(rowsNumber)])
	while(len(yValues) != rowsNumber):
		yValues.add(random.randint(ymin, ymax))

	xValues = list(xValues)
	yValues = list(yValues)
	xValues.sort()
	yValues.sort()
	for i in range(rowsNumber):
		coords.append([])
		coords[i].append(xValues[i])
		coords[i].append(yValues[i])

	return coords


CREDENTIALS_FILE = 'SysPO-64f3ebc3b4ff.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Мой документ', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 19, 'columnCount': 2}}}]
}).execute()


driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
shareRes = driveService.permissions().create(
    fileId = spreadsheet['spreadsheetId'],
    body = {'type': 'anyone', 'role': 'reader'},  # доступ на чтение кому угодно
    fields = 'id'
).execute()

link = "https://docs.google.com/spreadsheets/d/" + str(spreadsheet['spreadsheetId']) + "/edit"

results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "Лист1!A1:B1",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": [["X", "Y"]]},
    ]
}).execute()

coords = createData()
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "Лист1!A2:B19",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": coords},
    ]
}).execute()

webbrowser.open_new(link)

sumx = 0.0
sumy = 0.0
sumx2 = 0.0 
sumxy = 0.0

for i in range(rowsNumber):
	sumx += coords[i][0]
	sumx2 += coords[i][0]**2
	sumy += coords[i][1]
	sumxy += coords[i][0]*coords[i][1]

a = float((rowsNumber*sumxy - sumx*sumy)/(rowsNumber*sumx2 - sumx**2))
b = (sumy - a*sumx)/rowsNumber

print("Rows Number " + str(rowsNumber))
print("Sum X " + str(sumx))
print("Sum Y " + str(sumy))
print("Sum XY " + str(sumxy))
print("Sum X2 " + str(sumx2))

length = math.fabs(coords[rowsNumber-1][0] - coords[0][0])
leftBorder = coords[0][0] - 0.1*length
rightBorder = coords[rowsNumber-1][0] + 0.1*length
x = np.linspace(leftBorder, rightBorder, 1000)
#print(x)
y = []
for i in range(len(x)):
	y.append(a*x[i]+b)
#print(y)
print(a)
print(b)
xDots = []
yDots = []
for i in range(rowsNumber):
	xDots.append(coords[i][0])
	yDots.append(coords[i][1])
plt.plot(x, y, label='Approximation')
plt.plot(xDots, yDots, 'bo',label='Data')

plt.xlabel('x')
plt.ylabel('y')

plt.title("Linear Approximation")

plt.legend(loc=2)
plt.grid()
plt.show()


