import pygame
import random
from constants import  *
from block import Block

RED = (255, 0, 0)


class Food(Block):
	def __init__(self):
		Block.__init__(self,random.randint(1, COLUMNS-2),random.randint(1, ROWS-2))

	def draw(self,screen):
		Block.draw(self,screen,RED)

	def respawn(self, snake):
		while True:
			x, y = random.randint(1, COLUMNS-2), random.randint(1, ROWS-2)

			for block in snake.blocks:
				if block.is_on(Block(x, y)):
					break

			else:
				self.x, self.y = x,y
				break