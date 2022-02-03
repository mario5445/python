import pygame
import random


if __name__ == "__main__":
    cas = pygame.time.Clock()
    sirka = 800
    vyska = 600
    ufo = pygame.image.load("ufo.jpg")
    window = pygame.display.set_mode((sirka, vyska))
    pozadie = pygame.image.load("vesmir.jpg")
    while True:
        for dej in pygame.event.get():
            if dej.type == pygame.QUIT:
                pygame.quit()

        window.blit(pozadie, (0,0))
        window.blit(ufo, (sirka//2, vyska//2+190))



        cas.tick(30)
        pygame.display.update()

