#libraries used
import pygame
import numpy as np                  
import random
from pygame import mixer
import sys

#global variables
row = 12
column = 15
maze = [[0 for i in range(column)] for y in range(row)]
matrix = [[0 for i in range(column)] for y in range(row)]
done = False
if_key_pressed = 0
time_limit = 10

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
BLUE_GREEN = (0,255,170)
LIME = (180,255,100)
MAGENTA = (255, 0, 230)
YELLOW = (255, 255, 0)

#each square parameters in maze
WIDTH = 50
HEIGHT = 50
MARGIN = 5

pygame.init()
font = pygame.font.SysFont("Segoe UI", 100, True)
font2 = pygame.font.SysFont("Segoe UI", 46, True)
timer_font = pygame.font.SysFont("Segoe UI", 50, True)
#icon movement parameters
current_row = 0
current_col = 0

#game window parameters
w = 1400#830 #screen width
h = 666 #screen height

#icon parameters
x = 30
y = 30
vel = 55

#generating a random maze
def valid_maze():
    while True:
        maze = np.random.randint(2, size=[row, column])
        if solve_maze(maze):
            return maze

def movable(maze, x, y):
    return x >= 0 and x < row and y >= 0 and y < column and maze[x][y] == 1

def matrix_path(maze, x, y, matrix):
    if x == row - 1 and y == column - 1 and maze[x][y] == 1:  # if we've come out of the maze
        matrix[x][y] = 1
        return True
    if movable(maze, x, y):
        if matrix[x][y] == 1:  # backtracking
            return False
        matrix[x][y] = 1
        if matrix_path(maze, x + 1, y, matrix):  # if we can move down
            return True
        if matrix_path(maze, x, y + 1, matrix):  # if we can move right
            return True
        if matrix_path(maze, x - 1, y, matrix):  # if we can move up
            return True
        if matrix_path(maze, x, y - 1, matrix):  # if we can move left
            return True
        matrix[x][y] = 0
        return False

def solve_maze(maze):
    return matrix_path(maze, 0, 0, matrix)

maze = valid_maze()

def draw_grid():
    for i in range(row):
        for j in range(column):
            if maze[i][j] == 1:
                color = WHITE
            if maze[i][j] == 0:
                color = GREY
            if matrix[i][j] == -1:
                color = BLUE_GREEN
            if (i, j) == (row - 1, column - 1):
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * j + MARGIN, (MARGIN + HEIGHT) * i + MARGIN, WIDTH, HEIGHT])
            
def move_icon(dir):
    global current_row, current_col, x, y, screen
    matrix[current_row][current_col] = -1
    if dir == "r" and movable(maze, current_row, current_col + 1):
        current_col += 1
        x += vel
    if dir == "l" and movable(maze, current_row, current_col - 1):
        current_col -= 1
        x -= vel
    if dir == "u" and movable(maze, current_row - 1, current_col):
        current_row -= 1
        y -= vel
    if dir == "d" and movable(maze, current_row + 1, current_col): 
        current_row += 1
        y += vel

def music():
    mixer.init()
    mixer.music.load("quiet_time.mp3")
    mixer.music.set_volume(0.05)
    mixer.music.play()

def get_movements():
    global done, time_limit, timer_font, if_key_pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # If user clicked close
            pygame.quit()
            sys.exit()
            done = False
        if event.type == pygame.KEYUP:
            if_key_pressed += 1
        if event.type == timer:
            if if_key_pressed >= 1:
                timer_func()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_icon("r")
            if event.key == pygame.K_DOWN:
                move_icon("d")
            if event.key == pygame.K_UP:
                move_icon("u")
            if event.key == pygame.K_LEFT:
                move_icon("l")

def update_screen():
    global rect, time_limit
    screen.fill(BLACK)
    draw_grid()
    rect = my_image.get_rect()
    rect.center = (x, y)
    screen.blit(my_image, rect)
    timer_text = timer_font.render("  Timer : %02d" % time_limit, True, GREEN)
    screen.blit(timer_text,(950 - (timer_text.get_width() // 2), 400 - (timer_text.get_height() // 2)))
    game_instr = font2.render("  Get to the ", True, WHITE)
    screen.blit(game_instr,(950 - (timer_text.get_width() // 2), 200 - (timer_text.get_height() // 2)))
    game_instr = font2.render("red block ", True, RED)
    screen.blit(game_instr,(1210 - (timer_text.get_width() // 2), 200 - (timer_text.get_height() // 2)))    
    game_instr = font2.render("  before the time runs out",True,WHITE)
    screen.blit(game_instr,(950 - (timer_text.get_width() // 2), 300 - (timer_text.get_height() // 2)))
    clock.tick(60)
    pygame.display.flip()

def timer_func():
    global time_limit
    if time_limit > 0:
        time_limit -= 1
    else:
        print_game_over()
        done = True
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.mixer.quit()
        pygame.quit()
        sys.exit()

def print_vic():
    screen.fill(BLACK)
    victory_text = font.render("VICTORY!",True, MAGENTA)
    screen.blit(victory_text,(700 - (victory_text.get_width() // 2), 250 - (victory_text.get_height() // 2)))
    time_text = font.render("Time taken: " + str(10 - time_limit) + " seconds",True, LIME)
    screen.blit(time_text, (680 - (time_text.get_width() // 2), 400 - (time_text.get_height() // 2)))

def print_game_over():
    global time_seconds
    screen.fill(BLACK)
    game_over_text = font.render("You Lose!",True, YELLOW)
    screen.blit(game_over_text,(700 - (game_over_text.get_width() // 2), 300 - (game_over_text.get_height() // 2)))
    
pygame.display.set_caption("Maze game")
music()
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
clock = pygame.time.Clock()
my_icon = pygame.image.load('emoji.png')             #creating icon
my_image = pygame.transform.scale(my_icon, (40, 40))
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)

while not done:
    get_movements()
    update_screen()
    if (current_row, current_col) == (row - 1, column - 1):
        print_vic()   
        done = True
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.mixer.quit()
        pygame.quit()
