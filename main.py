#import modules
import pygame
import socketio
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

#Pokemon
class Pokemon:
    def __init__(self, names, lvl, maxLvl, atks, hps, maxHp, AbilityName, Ability):
        self.name = names
        self.lvl = lvl
        self.maxLvl = maxLvl
        self.atks = atks
        self.atk = atks[lvl]
        self.hps = hps
        self.hp = hps[lvl]
        self.maxHp = maxHp
        self.AbilityName = AbilityName
        self.Ability = Ability
def OvergrowBlazeTorrent(obj):
    if obj.hp <= obj.maxHp/2:
        obj.atk *= 2
SBulbadsaur = Pokemon(["Bulbsaur", "Ivysaur", "Venasaur"], 1, 3, [2,3,5],[3,4,10],"Overgrow", OvergrowBlazeTorrent)
SCharmander = Pokemon(["Bulbsaur", "Ivysaur", "Venasaur"], 1, 3, [2,3,5],[3,4,10],"Blaze", OvergrowBlazeTorrent)
SSquirtle = Pokemon(["Bulbsaur", "Ivysaur", "Venasaur"], 1, 3, [2,3,5],[3,4,10],"Overgrow", OvergrowBlazeTorrent)

#Buttons
class Button:
    def __init__(self,x,y,width, height, color, textColor, text, textFont, callBack):
        self.x = x-width//2
        self.y = y-height//2
        self.width = width
        self.height = height
        self.Rectangle = pygame.Rect(self.x,self.y,width,height)
        self.color = color
        self.textColor = textColor
        self.text = text
        self.textFont= textFont
        self.callBack = callBack
    def drawAndClick(self):
        #draw
        pygame.draw.rect(screen, self.color, self.Rectangle)
        pygame.draw.rect(screen, (0,0,0), self.Rectangle,5)
        displayText(self.text, self.textFont, self.x+self.width//2, self.y+self.height//2, self.textColor)
        #check for hover
        if self.Rectangle.collidepoint(pygame.mouse.get_pos()):
            self.Rectangle = pygame.Rect(self.x-2,self.y-2,self.width+4,self.height+4)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.callBack()
        else:
            self.Rectangle = pygame.Rect(self.x,self.y,self.width,self.height)

#states
def CreateButtonCallBack():
    global state
    state = "create"
def JoinButtonCallBack():
    global state
    state = "join"
def BTTButtonCallBack():
    global state
    state = "Title"
CreateButton = Button(width//2, height//2, 150,100, (250,91,5), (101, 30, 0), "Create", textFont, CreateButtonCallBack)
JoinButton = Button(width//2, height//2+120, 150,100, (250,91,5), (101, 30, 0), "Join", textFont, JoinButtonCallBack)
BackToTileButton = Button(width//2, height-100, 150,100, (250,91,5), (101, 30, 0), "Back", textFont, BTTButtonCallBack)

def title():
    displayText('Super Auto Pokemon', titleFont, width//2, height//4, (249,188,5) )
    CreateButton.drawAndClick()
    JoinButton.drawAndClick()

def create():
    displayText('Create', titleFont, width//2, height//4, (249,188,5) )
    BackToTileButton.drawAndClick()

def join():
    displayText('Join', titleFont, width//2, height//4, (249,188,5) )
    BackToTileButton.drawAndClick()


#main game loop
running = True
state = 'Title'
while running:
    #bg color
    screen.fill((111, 207, 240))
    #checking state
    if state == "Title":
        title()
    elif state == "create":
        create()
    elif state == "join":
        join()
    #checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Flip the display
    pygame.display.flip()

pygame.quit()