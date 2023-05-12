import pygame
import os
import math
import random

#################
# Display setup #
#################
pygame.init()
# FULLSCREEN MODE:
# pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#WINDOWED MODE:
WIDTH, HEIGHT = (1000, 700)
win = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Hangman")

###########
# Buttons #
###########
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) /2) # get total row length
starty = 450
A = 65
for i in range(26):
    # "i%13" simulates having 2 rows; RADIUS*2+GAP = length of gap & distance between each gap:
    x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True]) # take character representation of the number 65+i, adding the full alphabet

#########
# Fonts #
#########
LETTER_FONT = pygame.font.SysFont('comicsans', 23)
WORD_FONT = pygame.font.SysFont('comicsans', 31)
TITLE_FONT = pygame.font.SysFont('comicsans', 41)

###############
# Load images #
###############
images = [] # all images
for i in range(7):
    image = pygame.image.load("src/images/hangman" + str(i) + ".png") # get name of an image
    images.append(image) # add each image name

#############
# variables #
#############
hangman_status = 0
guessed = []

##########
# Colors #
##########
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

###################
# Game loop setup #
###################
FPS = 60
clock = pygame.time.Clock()
run = True

###################
# Get Random Word #
###################
def randomWord():
    lines = []
    with open('src/words.txt') as file:
        for line in file:
            lines += [line.strip()]
    return random.choice(lines)
word = randomWord()

########
# Draw #
########
def draw():
    win.fill((WHITE))
    # Draw title:
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Draw word:
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " " # letter-spacing
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (500, 300))
    

    # Draw buttons:
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100)) # blit(images) = draw images
    pygame.display.update() # update display with filling color

# End game message
def display_message(message):
    pygame.time.delay(1500) # 1.5 second delay
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)
        


while run:
    clock.tick(FPS) # game runs at steady speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # get mouse's x,y position:
        if event.type == pygame.MOUSEBUTTONDOWN: 
            m_x, m_y = pygame.mouse.get_pos() # mouse x, mouse y coordinates
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2) # distance
                    if dis < RADIUS:
                        letter[3] = False # hide button
                        guessed.append(ltr)
                        if ltr not in word: # if we guess a letter that's not in the word
                            hangman_status += 1
    
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You won!")
        break

    if hangman_status == 6:
        display_message("You lost!")
        break


pygame.quit()