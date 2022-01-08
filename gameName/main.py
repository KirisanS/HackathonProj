import pygame

pygame.init()

width = 700

window = pygame.display.set_mode((width,width))

pygame.display.set_caption("PlaceHolder")

window.fill((255,255,255)) 


def start():
    run = True


    while run:
        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False




    pygame.quit()





start()

