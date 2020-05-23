import pygame
import random
from constants import  *
from block import Block

class Snake:
	def __init__(self):
		self.vel = RIGHT
		self.blocks = [Block(1,1)]
		self.head = 0

	def change_direction(self, vel):
		"""Change the direction in which the snake is moving"""
		self.vel = vel

	def add_block(self):
		"""Updates the snakes position"""

		# Adds a new block to the snake
		current_head = self.blocks[len(self.blocks)-1]
		self.blocks.append(Block(current_head.x + self.vel[0], current_head.y + self.vel[1]))
		self.head = self.head+1

	def remove_block(self):
		self.blocks.pop(0)
		self.head = self.head-1

	def respawn(self):
		self.vel = RIGHT
		self.blocks = [Block(1,1)]
		self.head = 0

	def draw(self, screen):
		for c, block in enumerate(self.blocks):
			if c == self.head:
				color = (0,0,0)
			else:
				color = DARK_GREEN
			block.draw(screen,color)

	def is_on_food(self, food):
		return self.blocks[self.head].is_on(food)

	def is_on_self(self):
		for block in self.blocks[:self.head]:
			if self.blocks[self.head].is_on(block):
				return True
		else:
			return False

	def is_on_wall(self):
		for c in range(COLUMNS):
			for r in range(ROWS):
				if c  == 0 or c == COLUMNS-1 or r == 0 or r == ROWS-1:
					if self.blocks[self.head].is_on(Block(c,r)):
						return True
		else:
			return False

	def __repr__(self):
		string = "["
		for block in self.blocks:
			string = string + ",({},{}),".format(block.x,block.y)
		string = string + "]"

		return string