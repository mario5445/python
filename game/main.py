import pygame
import random
import sys


#generating of enemies
def generate_enemy():
    return {
        "x":random.choice(range(10,780,50)),
        "y":random.choice(range(-10, -600, -50))

    }






if __name__ == "__main__":
    #begining formula
    pygame.init()
    cas = pygame.time.Clock()
    #numbers
    skore = 0
    enemies = []
    font = pygame.font.SysFont('Times New Roman', 30)
    sirka = 800
    vyska = 600
    lod_x = sirka//2
    lod_y = vyska//2+220
    skore_x = sirka - 100
    skore_y = 33
    enemy_speed = 3
    enemy_count = 0
    enemy_plus = 4
    #image load
    pozadie = pygame.image.load("vesmir.jpg")
    ufo = pygame.image.load("lod.png")
    enemy_img = pygame.image.load('nepriatel.png')
    #window create
    window = pygame.display.set_mode((sirka, vyska))

    #append of enemy
    for i in range(enemy_count):
        enemies.append(generate_enemy())
    #game
    while True:
        skore_vypis = font.render(f"Score {skore}", True, (255,255,255))
        #enemy speed+, count+
        if len(enemies) == 0:
            for i in range(5):
                enemies.append(generate_enemy())
            enemy_speed += 0.8
            enemy_count += enemy_plus

        #exit formula
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #game control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if lod_x > 2:
                lod_x -= 8
        if key[pygame.K_RIGHT]:
            if lod_x < 714:
                lod_x += 8
        #draw
        window.blit(pozadie, (0,0))
        window.blit(ufo, (lod_x, lod_y))
        window.blit(skore_vypis, (skore_x, skore_y))
        #enemy move, score count
        for enemy in enemies[:]: #copy of the list
            window.blit(enemy_img, (enemy["x"], enemy["y"]))
            enemy["y"] += enemy_speed
            if enemy["y"] > 600:
                enemies.remove(enemy)
                skore += 1
        #end formula
        cas.tick(30)
        pygame.display.update()

