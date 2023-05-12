import pygame
import os

#################
# Display setup #
#################
pygame.init()
# FULLSCREEN MODE:
# pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#WINDOWED MODE:
WIDTH, HEIGHT = (500, 500)
win = pygame.display.set_mode((HEIGHT, WIDTH),pygame.RESIZABLE)
pygame.display.set_caption("Hangman")

###############
# Load images #
###############
images = [] # all images
for i in range(7):
    image = pygame.image.load("src/images/hangman" + str(i) + ".png") # get name of an image
    images.append(image) # add each image name

############################################################################################## Create img with surface of 209x216x32

#############
# variables #
#############
hangman_status = 0

##########
# Colors #
##########
WHITE = (255, 255, 255)

###################
# Game loop setup #
###################
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) # game runs at steady speed

    win.fill((WHITE))
    win.blit(images[hangman_status], (150, 100)) # blit(images) = draw images
    pygame.display.update() # update display with filling color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # get mouse's x,y position:
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()