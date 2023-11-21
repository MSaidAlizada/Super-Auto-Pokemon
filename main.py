#import modules
import pygame
pygame.init()

#set up screen
height = 600
width = 1000
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Super Auto Pokemon')

#writing texts and fonts
titleFont = pygame.font.Font('freesansbold.ttf', 80)
headingFont = pygame.font.Font('freesansbold.ttf', 60)
textFont = pygame.font.Font('freesansbold.ttf', 40)
miniFont = pygame.font.Font('freesansbold.ttf', 10)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
def displayText(text, f, x, y, color):
    text = f.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

#states
def title():
    displayText('Super Auto Pokemon', titleFont, width//2, height//3, (249,188,5) )

#main game loop
running = True
state = 'Title'
while running:
    #bg color
    screen.fill((111, 207, 240))
    #checking state
    if state == "Title":
        title()

    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

pygame.quit()