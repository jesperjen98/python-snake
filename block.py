import pygame
import random
from constants import  *


class Block:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def update(self, x, y):
		self.x = self.x + x
		self.y = self.y + y

	def is_on(self, block):
		return self.x == block.x and self.y == block.y

	def draw(self, screen, color):
		pygame.draw.rect(screen, color, [self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
		pygame.draw.rect(screen, (0, 0, 0), [self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE], 2)
