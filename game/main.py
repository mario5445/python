import pygame
import random


"""
def generate_enemy():
    
"""
if __name__ == "__main__":
    pygame.init()
    cas = pygame.time.Clock()
    skore = 0
    font = pygame.font.SysFont('Times New Roman', 30)
    sirka = 800
    vyska = 600
    lod_x = sirka//2
    lod_y = vyska//2+220
    skore_x = sirka - 100
    skore_y = 33
    pozadie = pygame.image.load("vesmir.jpg")
    ufo = pygame.image.load("lod.png")
    enemy = pygame.image.load('nepriatel.png')

    window = pygame.display.set_mode((sirka, vyska))

    while True:
        skore_vypis = font.render(f"Score {skore}", True, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if lod_x > 2:
                lod_x -= 8
        if key[pygame.K_RIGHT]:
            if lod_x < 714:
                lod_x += 8

        window.blit(pozadie, (0,0))
        window.blit(ufo, (lod_x, lod_y))
        window.blit(enemy, (100, 100))
        window.blit(skore_vypis, (skore_x, skore_y))


        cas.tick(30)
        pygame.display.update()

