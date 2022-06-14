import math
import random
import pyglet
from pyglet import gl
from pyglet.window import key

"---------Globalne konštanty a premenne----------"

"Window constants"
WIDTH = 1200
HEIGHT = 800

"Game constants"
ACCELERATION = 120              #Zrýchlenie rakety
ROTATION_SPEED = 0.05           #Rýchlosť otáčania rakety

game_objects = []
batch = pyglet.graphics.Batch() #ZOZNAM SPRITOV PRE ZJEDNODUŠENÉ VYKRESLENIE
pressed_keyboards = set()       #MNOŽINA ZMAČKNUTÝCH KLÁVES

# Todo: Pridaj KONŠTANTY pre delay na strelbu, laserlifetime, laserspeed
SHOT_DELAY = 0.5
LASER_LIFETIME = 29
LASER_SPEED = 350

SHIELD_LIFETIME = 3
shield_position_x = 0
shield_position_y = 0
shield_rotation = 0

lifes = 3
"Score"
score = 0
scoreLabel = pyglet.text.Label(text=str(score), font_size=40,x = 1150, y = 760, anchor_x='right', anchor_y='center', batch=batch )

"------------------- FUNKCIE __________________"

"""
Vycentruj ukotvenie obrázka na stred
"""
def set_anchor_of_image_to_center(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2


"""
Pomocna funkcia na zobrazenia kolizneho kolecka
"""
def draw_circle(x, y, radius):
    iterations = 20
    s = math.sin(2 * math.pi / iterations)
    c = math.cos(2 * math.pi / iterations)

    dx, dy = radius, 0

    gl.glBegin(gl.GL_LINE_STRIP)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou
    for i in range(iterations + 1):
        gl.glVertex2f(x + dx, y + dy)
        dx, dy = (dx * c - dy * s), (dy * c + dx * s)
    gl.glEnd()


"----------------VLASTNÉ TRIEDY----------------"

"""
Rodičovská trieda
"""
class SpaceObject:
    "Konštruktor"
    def __init__(self, sprite, x, y, speed_x= 0, speed_y = 0):
        self.x_speed = speed_x
        self.y_speed = speed_y
        self.rotation = 1.57  # radiany -> smeruje hore

        self.sprite = pyglet.sprite.Sprite(sprite, batch=batch)
        self.sprite.x = x
        self.sprite.y = y
        self.radius = (self.sprite.height + self.sprite.width) // 4

    """
    Výpočet vzdialenosti medzi dvoma objektami
    Pytagorova veta
    """
    def distance(self, other):
        x = abs(self.sprite.x - other.sprite.x)
        y = abs(self.sprite.y - other.sprite.y)
        return (x**2 + y**2) ** 0.5 #pytagorova veta

    """
    Kolizná metóda s loďou - nie je nutné defunovať, 
    Definujeme až v odvodenej triede
    """
    def hit_by_spaceship(self, ship):
        pass

    """
    Kolízna metóda s laserom - nie je nutné defynovať
    Definujeme až v odvodenej triede
    """
    def hit_by_laser(self, laser):
        pass

    "Metoda ktora deletne objekt"
    def delete(self, dt =0 ):
        self.sprite.delete()
        game_objects.remove(self)

    """
    Metóda pre kontrolu pozície či sa nachádzame na okraji
    """
    def checkBoundaries(self):
        if self.sprite.x > WIDTH:
            self.sprite.x = 0

        if self.sprite.x < 0:
            self.sprite.x = WIDTH

        if self.sprite.y < 0:
            self.sprite.y = HEIGHT

        if self.sprite.y > HEIGHT:
            self.sprite.y = 0

    """
    Metoda tick spoločná pre všetky podtriedy
    """
    def tick(self, dt):
        "Posunutie vesmírnej lode na novú pozíciu"
        self.sprite.x += dt * self.x_speed
        self.sprite.y += dt * self.y_speed
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        "Kontrola či sme prešli kraj"
        self.checkBoundaries()

"""
Trieda Spaceship
Hlavný objekt hry, predstavuje hráča
"""
class Shield(SpaceObject):
    def __init__(self, sprite, x, y, speed_x=0, speed_y=0):
        super().__init__(sprite, x, y, speed_x, speed_y)
        self.shieldlifetime = SHIELD_LIFETIME

    def tick(self, dt):
        global shield_position_y, shield_position_x
        super().tick(dt) 
        self.sprite.x = shield_position_x
        self.sprite.y = shield_position_y
        self.rotation = shield_rotation
        self.shieldlifetime -= dt
        if self.shieldlifetime <= 0:
            self.delete()   
   
        

class Spaceship(SpaceObject):

    "Konśtruktor"
    def __init__(self, sprite, x ,y):
        super().__init__(sprite,x,y)
        self.ready_laser = True
        self.shield = False

        flame_img = pyglet.image.load(r'Assetss\PNG\Effects\fire16.png')
        set_anchor_of_image_to_center(flame_img)
        self.flame = pyglet.sprite.Sprite(flame_img, batch=batch)
        self.flame.visible = False
    """
    Metóda zodpovedná za vystrelenie laseru
    """
    def shoot(self):
        # Todo: Vytvor nový objekt typu Laser a nastav parameter fire na hodnotu delayu
        laser_img_list = ['Assetss\PNG\Lasers\laserBlue01.png',
        'Assetss\PNG\Lasers\laserBlue02.png',
        'Assetss\PNG\Lasers\laserBlue03.png',
        'Assetss\PNG\Lasers\laserBlue04.png',
        'Assetss\PNG\Lasers\laserBlue05.png',
        'Assetss\PNG\Lasers\laserBlue06.png',
        'Assetss\PNG\Lasers\laserBlue07.png',
        'Assetss\PNG\Lasers\laserBlue08.png',
        'Assetss\PNG\Lasers\laserBlue09.png',
        'Assetss\PNG\Lasers\laserBlue10.png',
        'Assetss\PNG\Lasers\laserBlue11.png',
        'Assetss\PNG\Lasers\laserBlue12.png',
        'Assetss\PNG\Lasers\laserBlue13.png',
        'Assetss\PNG\Lasers\laserBlue14.png',
        'Assetss\PNG\Lasers\laserBlue15.png',
        'Assetss\PNG\Lasers\laserBlue16.png',
        ]

        laser_img = pyglet.image.load(random.choice(laser_img_list))
        set_anchor_of_image_to_center(laser_img)
        laser_x = self.sprite.x + math.cos(self.rotation) * self.radius
        laser_y = self.sprite.y + math.cos(self.rotation) * self.radius
        laser = Laser(laser_img, laser_x, laser_y)
        laser.rotation = self.rotation
        game_objects.append(laser)
        pass
    
    def activate_shield(self):
        self.shield = True
        shield_img = pyglet.image.load('Assetss\PNG\Effects\shield1.png')
        set_anchor_of_image_to_center(shield_img)
        shield = Shield(shield_img, self.sprite.x, self.sprite.y)
        shield.rotation = shield_rotation
        game_objects.append(shield)
        pyglet.clock.schedule_once(self.deactivate_shield, SHIELD_LIFETIME)
    def deactivate_shield(self, dt):
        self.shield = False

    def get_position(self):
        global shield_position_x, shield_rotation, shield_position_y
        shield_position_x = self.sprite.x
        shield_position_y = self.sprite.y
        shield_rotation = self.rotation  
    """
    Každý frame sa vykoná táto metóda to znamená v našom prípade:
    60 simkov * za sekundu
    Mechanic of spaceship - rotation, movement, controls
    """
    def tick(self, dt):
        super().tick(dt)

        "Zrýchlenie po kliknutí klávesy W. Výpočet novej rýchlosti"
        if 'W' in pressed_keyboards:
            self.x_speed = self.x_speed + dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed = self.y_speed + dt * ACCELERATION * math.sin(self.rotation)

            self.flame.visible = True
            self.flame.x = self.sprite.x - math.cos(self.rotation) * self.radius
            self.flame.y = self.sprite.y - math.sin(self.rotation) * self.radius
            self.flame.rotation = self.sprite.rotation
        else:
            self.flame.visible = False

        "Spomalenie/spätný chod po kliknutí klávesy S"
        if 'S' in pressed_keyboards:
            self.x_speed = self.x_speed - dt * ACCELERATION * math.cos(self.rotation)
            self.y_speed = self.y_speed - dt * ACCELERATION * math.sin(self.rotation)

        "Otočenie doľava - A"
        if 'A' in pressed_keyboards:
            self.rotation += ROTATION_SPEED

        "Otočenie doprava - D"
        if 'D' in pressed_keyboards:
            self.rotation -= ROTATION_SPEED

        "Ručná brzda - SHIFT"
        if 'SHIFT' in pressed_keyboards:
            self.x_speed = 0
            self.y_speed = 0
        
        if self.shield == True:
            self.get_position()

        # Todo: pridaj akciu po stlačení tlačítka SPACE = shoot
        #self.fire -= dt # TodoW: Je treba odčítať delay z fire
        if 'SPACE' in pressed_keyboards and self.ready_laser:
            self.shoot()
            self.ready_laser = False
            pyglet.clock.schedule_once(self.reload, SHOT_DELAY)

        "VYBERIE VŠETKY OSTATNE OBJEKTY OKREM SEBA SAMA"
        for obj in [o for o in game_objects if o != self]:
            # d = distance medzi objektami
            d = self.distance(obj)
            if d < self.radius + obj.radius:
                obj.hit_by_spaceship(self)
                break

    "Metóda zodpovedná za reset pozície rakety"
    def reset(self):
        self.sprite.x = WIDTH // 2
        self.sprite.y = HEIGHT // 2
        self.rotation = 1.57  # radiany -> smeruje hore
        self.x_speed = 0
        self.y_speed = 0
        self.activate_shield()
        
        
    def reload(self, dt):
        self.ready_laser = True


"""
Trieda Asteroid
"""
class Asteroid(SpaceObject):
    "Metóda ktorá sa vykoná ak dôjde ku kolízii lode a asteroidu"
    def hit_by_spaceship(self, ship):
        global score, scoreLabel, lifes
        if ship.shield == False:
            pressed_keyboards.clear()
            ship.reset()
            self.delete()
            lifes -= 1
            if score >= 0 and score < 50:
                if score >= 10:
                    score -= 10
                else:
                    pass
            else:
                score -= 50
        else:
            self.delete()

    "Metóda ktorá sa vykoná ak dôjde ku kolíziiwwwww a asteroidu"
    def hit_by_laser(self, laser):
        global score
        # Todo: update score + kolizia
        pressed_keyboards.clear()
        self.delete() 
        laser.delete()
        score += 10
        
        pass

"""
Trieda Laser
"""
class Laser(SpaceObject):
    #Todo: dorobiť triedu Laser
    def __init__(self, sprite, x, y, speed_x=0, speed_y=0):
        super().__init__(sprite, x, y, speed_x, speed_y)
        self.laserlifetime = LASER_LIFETIME

    def tick(self, dt):
        super().tick(dt)
        self.laserlifetime -= 0.5
        if self.laserlifetime == 0:
            self.delete()

        self.x_speed =  LASER_SPEED * math.cos(self.rotation)
        self.y_speed = LASER_SPEED * math.sin(self.rotation)    

        for obj in [o for o in game_objects if o != self and o != Spaceship]:
            d = self.distance(obj)
            if d < self.radius + obj.radius:
                obj.hit_by_laser(self)
                break
    pass


"""
GAME WINDOW CLASS
"""
class Game:
    """
    Konstruktor
    """
    def __init__(self):
        self.window = None
        game_objects = []

    """
    Načítanie všetkých spritov
    """
    def load_resources(self):
        list_of_spaceship = ['Assetss/PNG/playerShip1_blue.png',
        'Assetss\PNG\playerShip1_green.png',
        'Assetss\PNG\playerShip1_orange.png',
        'Assetss\PNG\playerShip1_red.png',
        'Assetss\PNG\playerShip2_blue.png',
        'Assetss\PNG\playerShip2_green.png',
        'Assetss\PNG\playerShip2_orange.png',
        'Assetss\PNG\playerShip2_red.png',
        'Assetss\PNG\playerShip3_blue.png',
        'Assetss\PNG\playerShip3_green.png',
        'Assetss\PNG\playerShip3_orange.png',
        'Assetss\PNG\playerShip3_red.png']
        self.playerShip_image = pyglet.image.load(random.choice(list_of_spaceship))
        set_anchor_of_image_to_center(self.playerShip_image)
        list_of_backgrounds = [r'Assetss\Backgrounds\black.png',
        r'Assetss\Backgrounds\blue.png',
        'Assetss\Backgrounds\darkPurple.png',
        'Assetss\Backgrounds\purple.png']
        self.background_image = pyglet.image.load(random.choice(list_of_backgrounds))
        self.asteroid_images = ['Assetss/PNG/Meteors/meteorGrey_big1.png',
                           'Assetss/PNG/Meteors/meteorGrey_med1.png',
                           'Assetss/PNG/Meteors/meteorGrey_small1.png',
                           'Assetss/PNG/Meteors/meteorGrey_tiny1.png',
                           'Assetss\PNG\Meteors\meteorBrown_big1.png',
                           'Assetss\PNG\Meteors\meteorBrown_big2.png',
                           'Assetss\PNG\Meteors\meteorBrown_big3.png',
                           'Assetss\PNG\Meteors\meteorBrown_big4.png',
                           'Assetss\PNG\Meteors\meteorBrown_med1.png',
                           'Assetss\PNG\Meteors\meteorBrown_med3.png',
                           'Assetss\PNG\Meteors\meteorBrown_small1.png',
                           'Assetss\PNG\Meteors\meteorBrown_small2.png',
                           'Assetss\PNG\Meteors\meteorBrown_tiny1.png',
                           'Assetss\PNG\Meteors\meteorBrown_tiny2.png',
                           'Assetss\PNG\Meteors\meteorGrey_big2.png',
                           'Assetss\PNG\Meteors\meteorGrey_big3.png',
                           'Assetss\PNG\Meteors\meteorGrey_big4.png',
                           'Assetss\PNG\Meteors\meteorGrey_med2.png',
                           'Assetss\PNG\Meteors\meteorGrey_small2.png',
                           'Assetss\PNG\Meteors\meteorGrey_tiny2.png']

    """
    Vytvorenie objektov pre začiatok hry
    """
    def init_objects(self):
        #Vytvorenie lode
        spaceShip = Spaceship(self.playerShip_image, WIDTH // 2, HEIGHT//2)
        game_objects.append(spaceShip)

        #Nastavenie pozadia a prescalovanie
        self.background = pyglet.sprite.Sprite(self.background_image)
        self.background.scale_x = 6
        self.background.scale_y = 4

        #Vytvorenie Meteoritov
        self.create_asteroids(count=7)
        #Pridavanie novych asteroidoch každych 10 sekund
        pyglet.clock.schedule_interval(self.create_asteroids, 8, 3)

    def create_asteroids(self, dt=0, count=1):
        "Vytvorenie X asteroidov"
        for i in range(count):
            # Výber asteroidu náhodne
            asteroids_img = pyglet.image.load(random.choice(self.asteroid_images))
            set_anchor_of_image_to_center(asteroids_img)

            # Nastavenie pozície na okraji obrazovky náhodne
            position = [0, 0]
            dimension = [WIDTH, HEIGHT]
            axis = random.choice([0, 1])
            position[axis] = random.uniform(0, dimension[axis])

            # Nastavenie rýchlosti
            tmp_speed_x = random.uniform(-100, 100)
            tmp_speed_y = random.uniform(-100, 100)

            #Temp asteroid object
            asteroid = Asteroid(asteroids_img, position[0], position[1], tmp_speed_x, tmp_speed_y)
            game_objects.append(asteroid)
    
    def lifes_draw(self):
        global lifes        
        life_image = pyglet.image.load(r'Assetss\PNG\UI\playerLife1_blue.png')
        life_x = 10
        for i in range(lifes):
            
            life = pyglet.sprite.Sprite(life_image, life_x, HEIGHT - 40)
            life_x += 40
            life.draw()
    
    def game_over(self):
        global lifes
        if lifes == 0:
            self.window.clear()
            game_objects.clear()
            game_over_label = pyglet.text.Label('Prehral si. Hra sa skončila!', font_size=60, x = WIDTH//2, y = HEIGHT//2 ,anchor_x='center', anchor_y='center')
            game_over_label.draw()

    """
    Event metóda ktorá sa volá na udalosť on_draw stále dookola
    """
    def draw_game(self):
        global score, scoreLabel
        # Vymaže aktualny obsah okna
        self.window.clear()
        # Vykreslenie pozadia
        self.background.draw()
        scoreLabel = pyglet.text.Label(text=str(score), font_size=40,x = 1150, y = 760, anchor_x='right', anchor_y='center')
        scoreLabel.draw()
        
        "Vykreslenie koliznych koliečok"
        """
        for o in game_objects:
            draw_circle(o.sprite.x, o.sprite.y, o.radius)"""
        
        
        # Táto časť sa stará o to aby bol prechod cez okraje okna plynulý a nie skokový
        for x_offset in (-self.window.width, 0, self.window.width):
            for y_offset in (-self.window.height, 0, self.window.height):
                # Remember the current state
                gl.glPushMatrix()
                # Move everything drawn from now on by (x_offset, y_offset, 0)
                gl.glTranslatef(x_offset, y_offset, 0)

                # Draw !!! -> Toto vykreslí všetky naše sprites
                batch.draw()

                # Restore remembered state (this cancels the glTranslatef)
                gl.glPopMatrix()
        self.lifes_draw()
        self.game_over()
    """
    Event metóda pre spracovanie klávesových vstupov
    """
    def key_press(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.add('W')
        if symbol == key.S:
            pressed_keyboards.add('S')
        if symbol == key.A:
            pressed_keyboards.add('A')
        if symbol == key.D:
            pressed_keyboards.add('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.add('SHIFT')
        if symbol == key.SPACE:
            pressed_keyboards.add("SPACE")
        #Todo: SPACE

    """
    Event metóda pre spracovanie klávesových výstupov
    """
    def key_release(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.discard('W')
        if symbol == key.S:
            pressed_keyboards.discard('S')
        if symbol == key.A:
            pressed_keyboards.discard('A')
        if symbol == key.D:
            pressed_keyboards.discard('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.discard('SHIFT')
        if symbol == key.SPACE:
            pressed_keyboards.discard("SPACE")
        # Todo: SPACE

    """
    Update metóda
    """
    def update(self, dt):
        for obj in game_objects:
            obj.tick(dt)

    """
    Start game metóda 
    """
    def start(self):
        "Vytvorenie hlavneho okna"
        self.window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

        "Nastavenie udalosti (eventov)"
        self.window.push_handlers(
            on_draw=self.draw_game,
            on_key_press=self.key_press,
            on_key_release=self.key_release
        )

        "Load resources"
        self.load_resources()

        "Inicializacia objektov"
        self.init_objects()

        "Nastavenie timeru pre update metódu v intervale 1./60 = 60FPS"
        pyglet.clock.schedule_interval(self.update, 1. / 60)

        pyglet.app.run()  # all is set, the game can start

"----------- StartGame -----------"
Game().start()


