import pygame
import sys
from labyrinth import *
sys.path.append('../')

#задаем размеры окна
display = (800, 525)
width = 35
height = 35

#задаем цвета элементов игры
wall_color = (0, 0, 0)
hero_color = (255, 0, 0)
path_color = (211, 211, 211)
background_color = (255, 255, 255)

class auto_walker:
	def __init__(self):
                #создание лабиринта и условий игры
		self.visited = []
		self.maze = Labyrinth(width, height)
		self.steps = 0
		self.success = False
		self.start_point, self.end_point = (1, 1), (15, 15)

		while True:
			x = random.randint(1, width - 1)
			y = random.randint(1, height - 1)
			if self.maze.get(x, y) == 'cell':
				self.start_point = (x, y)
				break

		while True:
			endX = random.randint(1, width - 1)
			endY = random.randint(1, height - 1)
			if self.maze.get(endX, endY) == 'cell':
				self.end_point = (endX, endY)
				break

		self.walk(self.start_point)

	def walk(self, start_point):
                #автоматическое прохождение пути
		if start_point == self.end_point or self.success:
			self.success = True
			return

		self.visited.append(start_point)
		neighbours = self.find_neighbours(start_point)
		numberOfNeighbours = len(neighbours)

		while numberOfNeighbours == 1:
			self.steps += 1
			start_point = neighbours[0]
			self.visited.append(start_point)
			if start_point == self.end_point or self.success:
				self.success = True
				return
			neighbours = self.find_neighbours(start_point)
			numberOfNeighbours = len(neighbours)

		for neighbour in neighbours:
			self.steps += 1
			self.walk(neighbour)
			if self.success:
				return
			self.steps += 1

		if start_point == self.end_point:
			return

	def draw_path(self):
		pygame.init()
		pygame.font.init()
		pygame.display.set_caption('Лабиринт')
		self.font = pygame.font.Font(None, 25)
		self.screen = pygame.display.set_mode(display)
		self.screen.fill(background_color)

                #отрисовка пути (следа) персонажа
		for i in range(width):
			for j in range(height):
				if self.maze.get(i, j) == 'wall':
					pygame.draw.rect(self.screen, wall_color, (i * 15, j * 15, 15, 15))
				if (i, j) in self.visited:
					pygame.draw.rect(self.screen, path_color, (i * 15, j * 15, 15, 15))

		pygame.draw.rect(self.screen, hero_color, (self.start_point[0] * 15, self.start_point[1] * 15, 15, 15))
		pygame.draw.rect(self.screen, wall_color, (self.end_point[0] * 15, self.end_point[1] * 15, 15, 15))

                #вывод результата прохождения лабиринта на экран
		stepsCounter = self.font.render("Выход найден за {} шагов.".format(self.steps), True, wall_color)
		self.screen.blit(stepsCounter, (535, 5))
		pygame.display.update()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

	def find_neighbours(self, cell):
                #проверка соседних клеток
		up = (cell[0], cell[1] + 1)
		down = (cell[0], cell[1] - 1)
		left = (cell[0] - 1, cell[1])
		right = (cell[0] + 1, cell[1])
		neighbours = [up, down, left, right]
		cells = []

		for neighbour in neighbours:
			if (neighbour[0] > 0 and neighbour[0] < width) and (neighbour[1] > 0 and neighbour[1] < height):
				if (self.maze.get(neighbour[0], neighbour[1]) != 'wall') and not neighbour in self.visited:
					cells.append(neighbour)

		return cells

if __name__ == '__main__':
	aw = auto_walker()
	aw.draw_path()
