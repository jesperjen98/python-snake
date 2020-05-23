import random, pygame, sys, copy
from constants import *
from snake import Snake
from block import Block
from food import Food
pygame.init()

# Fonts
FONT = pygame.font.Font('freesansbold.ttf', BLOCK_SIZE // 2)


class Text:
	def __init__(self,text):
		self.text = FONT.render(text, True, (0,0,0))
		self.text_rect = self.text.get_rect()

	def draw(self,screen):
		screen.blit(self.text,self.text_rect)

	def update(self,text):
		self.text = FONT.render(text, True, (0, 0, 0))


class Background:
	def __init__(self,canvas_color,board_color1,board_color2):
		self.canvas_color = canvas_color
		self.board_color1, self.board_color2 = board_color1, board_color2

	def draw(self, screen):
		screen.fill(self.canvas_color)

		for r in range(ROWS):
			for c in range(COLUMNS):
				if 0 < c < COLUMNS - 1 and 0 < r < ROWS - 1:
					if (c + r) % 2 == 0:
						color = self.board_color1
					else:
						color = self.board_color2
					pygame.draw.rect(screen, color, [c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])


def main():
	snake = Snake()
	food = Food()
	background = Background(DARK_GREEN,LIGHT_GREEN,GREEN)

	length_text = Text('Snake length: {}'.format(len(snake.blocks)))
	length_text.text_rect.topleft = (BLOCK_SIZE//4,BLOCK_SIZE//4)

	higscore_text = Text('High score: '.format(len(snake.blocks)))
	higscore_text.text_rect.topright = (WINDOW_WIDTH - BLOCK_SIZE//4,BLOCK_SIZE//4)

	game_objects = [background,food,snake,length_text,higscore_text]

	# define a variable to control the main loop
	running = True
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					if snake.vel != RIGHT:
						snake.change_direction(LEFT)
					break
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					if snake.vel != LEFT:
						snake.change_direction(RIGHT)
					break
				elif event.key == pygame.K_UP or event.key == pygame.K_w:
					if snake.vel != DOWN:
						snake.change_direction(UP)
					break
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					if snake.vel != UP:
						snake.change_direction(DOWN)
					break

		# Snakes logic

		snake.add_block()
		print(snake)

		if snake.is_on_self() or snake.is_on_wall():
			snake.respawn()
			food.respawn(snake)

		elif snake.is_on_food(food):
			food.respawn(snake)
			length_text.update('Snake length: {}'.format(len(snake.blocks)))
			higscore_text.text_rect.topright = (WINDOW_WIDTH - BLOCK_SIZE // 4, BLOCK_SIZE // 4)

		else:
			snake.remove_block()

		# Draw all game objects
		for obj in game_objects:
			obj.draw(screen)

		pygame.display.flip()

		pygame.time.delay(100)


if __name__ == "__main__":
	main()