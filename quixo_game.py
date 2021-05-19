# import modules
import pygame
from pygame.locals import *
pygame.init()

screen_height = 500
screen_width = 500
line_width: int = 15
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Quixo Game')

# define colours
black = (66, 66, 66)
green = (239, 231, 200)
blue = (0, 0, 255)

# define font
font = pygame.font.SysFont(None, 40)

# define variables
clicked = False
player = 1
pos = (0, 0)
markers = []
game_over = False
winner = 0
comp = 0

# setup a rectangle for "Play Again" Option
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

# create empty 5 x 5 list to represent the grid
for x in range(5):
	row = [0] * 5
	markers.append(row)

def draw_board():
	bg = (28, 170, 156)
	grid = (23, 145, 135)
	screen.fill(bg)
	for x in range(1, 5):
		pygame.draw.line(screen, grid, (0, 100 * x), (screen_width, 100 * x), line_width)
		pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, black, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, black, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if (y == -1):
				pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1
		
		
def check_game_over():
	global game_over
	global winner
	print(markers)
	x_pos = 0
	for x in markers:
		# check columns
		if sum(x) == 5:
			winner = 1
			game_over = True
		if sum(x) == -5:
			winner = 2
			game_over = True
		# check rows
		if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] + markers[3][x_pos] + markers[4][x_pos] == 5:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] + markers[3][x_pos] + markers[4][x_pos] == -5:
			winner = 2
			game_over = True
		x_pos += 1

	# check cross
	if markers[0][0] + markers[1][1] + markers[2][2] + markers[3][3] + markers[4][4] == 5 or markers[4][0] + markers[2][2] + markers[0][4] + markers[1][3] + markers[3][1] == 5:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers[2][2] + markers[3][3] + markers[4][4] == -5 or markers[4][0] + markers[2][2] + markers[0][4] + markers[1][3] + markers[3][1] == -5:
		winner = 2
		game_over = True

	# check for tie
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		# if it is a tie, then call game over and set winner to 0 (no one)
		if tie == True:
			game_over = True
			winner = 0
