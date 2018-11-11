import pygame
import time
from labyrinth import *

#задаем размеры окна
display = (750, 525)
width = 35
height = 35

#задаем цвета элементов игры
wall_color = (0, 0, 0)
hero_color = (255, 0, 0)
exit_color = (0, 255, 0)
path_color = (211, 211, 211)
background_color = (255, 255, 255)


class Interface:    
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Лабиринт')
        self.screen = pygame.display.set_mode(display)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.heroX = 1
        self.heroY = 1
        self.steps = 0
        self.startPoint = (1, 1)
        self.endPoint = (1, 1)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 25)


    def draw(self):
        self.maze = Labyrinth(width, height)
        self.screen.fill(background_color)
        pygame.draw.rect(self.screen, exit_color, (self.endPoint[0] * 15, self.endPoint[1] * 15, 15, 15) )

        #вывод инструкции на экран
        restart1 = self.font.render("Чтобы начать заново ", True, path_color)
        restart2 = self.font.render("нажмите \"R\"", True, path_color)
        self.screen.blit(restart1, (535, 480))
        self.screen.blit(restart2, (535, 500))

        pygame.display.update()

        #построение лабиринта
        for i in range(width):
            for j in range(height):
                if self.maze.get(i, j) == 'wall':
                    pygame.draw.rect(self.screen, wall_color, (i * 15, j * 15, 15, 15))

        while True:
            self.heroX = random.randint(1, width - 1)
            self.heroY = random.randint(1, height - 1)
            if self.maze.get(self.heroX, self.heroY) == 'cell':
                self.startPoint = (self.heroX, self.heroY)
                break

        while True:
            x = random.randint(1, width - 1)
            y = random.randint(1, height - 1)
            if self.maze.get(x, y) == 'cell':
                self.endPoint = (x, y)
                break


    def main(self):
        self.startTime = time.time()
        self.draw()
        success = False

        while True:
            self.clock.tick(self.FPS)

            if (self.heroX, self.heroY) == self.endPoint:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                self.draw()
                                self.startTime = time.time()
                                self.heroX = self.startPoint[0]
                                self.heroY = self.startPoint[1]
                                break

            for event in pygame.event.get():

                #выход из игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                #настройка управления
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.draw()
                        self.startTime = time.time()

                        while True:
                            self.heroX = random.randint(1, width - 1)
                            self.heroY = random.randint(1, height - 1)
                            if self.maze.get(self.heroX, self.heroY) == 'cell':
                                break

                        while True:
                            x = random.randint(1, width - 1)
                            y = random.randint(1, height - 1)
                            if self.maze.get(x, y) == 'cell':
                                self.endPoint = (x, y)
                                break

                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.maze.get(self.heroX, self.heroY - 1) != 'wall':
                            pygame.draw.rect(self.screen, path_color, (self.heroX * 15, self.heroY * 15, 15, 15))
                            self.heroY -= 1
                            self.steps += 1

                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if self.maze.get(self.heroX - 1, self.heroY) != 'wall':
                            pygame.draw.rect(self.screen, path_color, (self.heroX * 15, self.heroY * 15, 15, 15))
                            self.heroX -= 1
                            self.steps += 1

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.maze.get(self.heroX, self.heroY + 1) != 'wall':
                            pygame.draw.rect(self.screen, path_color, (self.heroX * 15, self.heroY * 15, 15, 15))
                            self.heroY += 1
                            self.steps += 1

                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.maze.get(self.heroX + 1, self.heroY) != 'wall':
                            pygame.draw.rect(self.screen, path_color, (self.heroX * 15, self.heroY * 15, 15, 15))
                            self.heroX += 1
                            self.steps += 1

            pygame.draw.rect(self.screen, hero_color, (self.heroX * 15, self.heroY * 15, 15, 15))

            #вывод статистики на экран
            countedTime = time.time() - self.startTime
            timeCounter = self.font.render("Время: {0:.1f} с ".format(countedTime), True, wall_color, background_color)
            self.screen.blit(timeCounter, (535, 5))

            stepsCounter = self.font.render("Количество шагов : {} ".format(self.steps), True, wall_color, background_color)
            self.screen.blit(stepsCounter, (535, 25))
            
            pygame.display.update()


if __name__ == '__main__':
    interface = Interface()
    interface.main()

