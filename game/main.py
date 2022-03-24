import pygame
import random
import sys


#generating of enemies
def generate_enemy(image):
    return {
        "x":random.choice(range(10,780,50)),
        "y":random.choice(range(-10, -600, -50)),
        "mask": pygame.mask.from_surface(image)
    }


def colision_check(mask1, mask2, mask1_coordinates, mask2_coordinates):
    x = mask2_coordinates[0] - mask1_coordinates[0]
    y = mask2_coordinates[1] - mask1_coordinates[1]
    if mask1.overlap(mask2, (x,y)):
        return True
    else:
        return False




if __name__ == "__main__":
    #begining formula
    pygame.init()
    cas = pygame.time.Clock()
    #numbers
    skore = 0
    enemies = []
    end = False
    font = pygame.font.SysFont('Times New Roman', 30)
    sirka = 800
    vyska = 600
    ufo_x = sirka//2
    ufo_y = vyska//2+220
    skore_x = sirka - 120
    skore_y = 33
    enemy_speed = 3
    #image load
    pozadie1 = pygame.image.load("vesmir.jpg")
    pozadie2 = pygame.image.load("Star_wars.jpg")
    ufo = pygame.image.load("lod.png")
    enemy_img = pygame.image.load('nepriatel.png')
    #mask creating(for ship)
    ufo_mask = pygame.mask.from_surface(ufo)
    #window create
    window = pygame.display.set_mode((sirka, vyska))

    #append of enemy

    #game
    while True:
        skore_vypis = font.render(f"Score {skore}", True, (255,255,255))
        #enemy speed+, count+
        if len(enemies) == 0:
            for i in range(10):
                enemies.append(generate_enemy(enemy_img))
            enemy_speed += 0.8


        #exit formula
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #game control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if ufo_x > 2:
                ufo_x -= 8
        if key[pygame.K_RIGHT]:
            if ufo_x < 714:
                ufo_x += 8
        #draw
        if skore < 50:
            window.blit(pozadie1, (0,0))
        else:
            window.blit(pozadie2, (-350, -200))
        window.blit(ufo, (ufo_x, ufo_y))
        window.blit(skore_vypis, (skore_x, skore_y))
        #enemy move, score count
        if not end:
            for enemy in enemies[:]: #copy of the list
                window.blit(enemy_img, (enemy["x"], enemy["y"]))
                enemy["y"] += enemy_speed
                if enemy["y"] > 600:
                    enemies.remove(enemy)
                    skore += 1
                if colision_check(ufo_mask, enemy["mask"], (ufo_x, ufo_y), (enemy["x"], enemy["y"])):
                    end = True
        else:
            end_font = pygame.font.SysFont("Times New Roman", 50)
            end_vypis = end_font.render("Game over", True, (255, 10, 10))
            window.blit(end_vypis, (sirka//2 - 100, vyska//2))
        #end formula
        cas.tick(30)
        pygame.display.update()

