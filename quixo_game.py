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