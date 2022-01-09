import pygame
from pygame.constants import KEYDOWN, KEYUP

pygame.init()

width = 700

fps = 60

window = pygame.display.set_mode((width,width))

pygame.display.set_caption("PlaceHolder")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

CIRCLE_RADIUS = 10

x = 350
y = 350

window.fill(WHITE)

def render():
    window.fill(WHITE)
    pygame.draw.circle(window, RED, [x, y], CIRCLE_RADIUS, 0)



class Button():
  def __init__(self, x,y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)

  
  def draw(self):
    action = False
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1:
        action = True
    window.blit(self.image, (self.rect.x, self.rect.y))

    return action

startImg = pygame.image.load('start.png').convert_alpha()
optionsImg = pygame.image.load('options.png').convert_alpha()

startButton = Button(265, 100, startImg)
optionsButton = Button(257, 150, optionsImg)

def start():
    run = True

    up = down = left = right = False
    shoot = False

    while run:
        
        if startButton.draw() == True:
          print("Start the game")


  


        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            render()
            if event.type == KEYDOWN:
                y = 0
                x = 0

                if event.key == pygame.K_w:
                    up = True
                    print("w")
                    y -= 3

                if event.key == pygame.K_s:
                    down = True
                    print("s")
                    y += 3

                if event.key == pygame.K_a:
                    left = True
                    print("a")
                    x -= 3

                if event.key == pygame.K_d:
                    right = True
                    print("d")
                    x += 3

                if event.key == pygame.K_SPACE:
                    shoot = True
                    print("space")


            if event.type == KEYUP:

                if event.key == pygame.K_w:
                    up = False
                    print("w")

                if event.key == pygame.K_s:
                    down = False
                    print("s")

                if event.key == pygame.K_a:
                    left = False
                    print("a")

                if event.key == pygame.K_d:
                    right = False
                    print("d")

                if event.key == pygame.K_SPACE:
                    shoot = False
                    print("space")


        if up:
            print("up")

        if down:
            print("down")

        if left:
            print("left")

        if right:
            print("right")

        if shoot:
            print("shoot")





        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

start()
