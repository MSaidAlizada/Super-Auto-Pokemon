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

#Buttons
class Button:
    def __init__(self,x,y,width, height, color, textColor, text, textFont):
        self.x = x-width//2
        self.y = y-height//2
        self.width = width
        self.height = height
        self.Rectangle = pygame.Rect(self.x,self.y,width,height)
        self.color = color
        self.textColor = textColor
        self.text = text
        self.textFont= textFont
    def drawAndClick(self):
        #draw
        pygame.draw.rect(screen, self.color, self.Rectangle)
        pygame.draw.rect(screen, (0,0,0), self.Rectangle,5)
        displayText(self.text, self.textFont, self.x+self.width//2, self.y+self.height//2, self.textColor)
        #check for hover
        if StartButton.Rectangle.collidepoint(pygame.mouse.get_pos()):
            self.Rectangle = pygame.Rect(self.x-2,self.y-2,self.width+4,self.height+4)
        else:
            self.Rectangle = pygame.Rect(self.x,self.y,self.width,self.height)

#states
StartButton = Button(width//2, height//1.5, 150,100, (250,91,5), (101, 30, 0), "START", textFont)
def title():
    displayText('Super Auto Pokemon', titleFont, width//2, height//3, (249,188,5) )
    StartButton.drawAndClick()

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