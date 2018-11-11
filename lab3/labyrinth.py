import random
from math import copysign

class Labyrinth:
	def __init__(self, height, width):
		self.w = width
		self.h = height
		self.maze = []
		for i in range(self.w):
			self.maze.append([])
			for j in range(self.h):
				if ((i % 2 != 0) and (j % 2 != 0) and (i < self.w and j < self.h)):
					self.maze[i].append('cell')
				else:
					self.maze[i].append('wall')

		self.createLabyrinth()

	def removeWall(self, first, second, v, nv):
		dx = second[0] - first[0]
		dy = second[1] - first[1]

		if dx == 0:
			addx = 0
		else:
			addx = copysign(1, dx)

		if dy == 0:
			addy = 0
		else:
			addy = copysign(1, dy)

		x = int(first[0] + addx)
		y = int(first[1] + addy)

		self.maze[x][y] = 'cell'
		v.append( (x, y) )
		nv.remove( (x, y) )

		return v, nv
	
	def getNeighbours(self, cell, v):
		up = (cell[0], cell[1]+2)
		down = (cell[0], cell[1]-2)
		right = (cell[0]+2, cell[1])
		left = (cell[0]-2, cell[1])
		neighbours = [up, down, right, left]
		cells = []

		for n in neighbours:
			if ( n[0] > 0 and n[0] < self.w ) and ( n[1] > 0 and n[1] < self.h ):

				if ( not self.maze[n[0]][n[1]] == 'wall' ) and not ( n in v ):
					cells.append(n)
					
		return cells

	def getUnvisited(self, v):
		unvisited = []
		for i in range(1, self.w):
			for j in range(1, self.h):
				if not (i, j) in v:
					unvisited.append( (i, j) )

		return unvisited

	def createLabyrinth(self):
		stack = []
		visited = [(1,1)]
		none_visited = self.getUnvisited(visited)
                
		current_cell = (1,1)

		while len(none_visited) != 0:
			neighbours = self.getNeighbours(current_cell, visited)
			if neighbours:
				neighbour_cell = random.choice(neighbours)
				stack.append(current_cell)
				visited, none_visited = self.removeWall(current_cell, neighbour_cell, visited, none_visited)
				current_cell = neighbour_cell
				visited.append(current_cell)
				none_visited.remove(current_cell)
				neighbours = 0
			elif stack:
				current_cell = stack.pop()
			else:
				current_cell = random.choice(none_visited)
				visited.append(current_cell)
				none_visited.remove(current_cell)

	def get(self, i, j):
		return self.maze[i][j]
