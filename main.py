import os
from time import sleepl
import pygame
from pygame.locals import *

from snake import Snake, Food
from scoreboard import Scoreboard

FPS = 8

CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = (32, 32)
SCREEN_WIDTH_CELLS = 16
SCREEN_HEIGHT_CELLS = 16 

BG_COLOR = (232, 241, 242)

pygame.init()
pygame.display.set_caption("Snake The Game")
screen = pygame.display.set_mode((SCREEN_WIDTH_CELLS * CELL_WIDTH, SCREEN_HEIGHT_CELLS * CELL_HEIGHT))

clock = pygame.time.Clock()

snake = Snake((SCREEN_WIDTH_CELLS // 2, SCREEN_HEIGHT_CELLS // 2))
food = Food()
food.refresh(SCREEN_WIDTH_CELLS, SCREEN_HEIGHT_CELLS)

scoreboard = Scoreboard(screen.get_rect().midtop)

game_over = False
game_over_text_surface = pygame.font.SysFont(None, 64).render("GAME OVER", True, (0, 26, 35))
game_over_text_rect = game_over_text_surface.get_rect(center=screen.get_rect().center)


is_running = True
while is_running:

    frame_time_ms = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_running = False
            elif event.key == K_UP or event.key == K_w:
                snake.set_move_direction_up()
            elif event.key == K_DOWN or event.key == K_s:
                snake.set_move_direction_down() 
            elif event.key == K_RIGHT or event.key == K_d:
                snake.set_move_direction_right()
            elif event.key == K_LEFT or event.key == K_a:
                snake.set_move_direction_left() 

    if not game_over:
        snake.update()
        if snake.head.cell_position == food.cell_position:
            scoreboard.increase_score()
            food.refresh(SCREEN_WIDTH_CELLS-1, SCREEN_HEIGHT_CELLS-1)
            snake.extend()

    if snake.head.cell_x < 0 or snake.head.cell_x > SCREEN_WIDTH_CELLS-1 or snake.head.cell_y < 0 or snake.head.cell_y > SCREEN_HEIGHT_CELLS-1:
        game_over = True
    for segment in snake.segments[1:]:
        if segment.cell_position == snake.head.cell_position:
            game_over = True
            break

    screen.fill(BG_COLOR)
    food.draw(screen, CELL_WIDTH)
    snake.draw(screen, CELL_WIDTH)
    scoreboard.draw(screen)
    if game_over:
        screen.blit(game_over_text_surface, game_over_text_rect)
    pygame.display.update()
    if game_over:
        sleep(2)
        is_running = False

os.system("cls")
