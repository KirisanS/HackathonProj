import pygame

pygame.init()

width = 700

fps = 30

window = pygame.display.set_mode((width,width))

pygame.display.set_caption("PlaceHolder")

clock = pygame.time.Clock()

window.fill((255,255,255)) 


def start():
    run = True


    while run:
        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()





start()

