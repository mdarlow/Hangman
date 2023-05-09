import pygame
import os

pygame.init()
# FULLSCREEN MODE:
# pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#WINDOWED MODE:
WIDTH, HEIGHT = (500, 500)
pygame.display.set_mode((HEIGHT, WIDTH),pygame.RESIZABLE)
pygame.display.set_caption("Hangman")

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) # game runs at steady speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # get mouse's x,y position:
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()