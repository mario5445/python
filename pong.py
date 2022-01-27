import pyglet
from pyglet import gl
import random

#nastavenie sirky a vysky
from pyglet.window import key

sirka = 1300
vyska = 700

#lopta
velkost_lopty = 20
RYCHLOST = 200
#hrubka deliacej ciary
ciara_hrubka = 20
#palky
dlzka_palky = 10
vyska_palky = 100
RYCHLOST_PALKY = RYCHLOST*3

#font
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#stavove premenne
pozicia_palok = [vyska//2, vyska//2]
pozicia_lopty = [sirka//2, vyska//2]
rychlost_lopty = [0,0]
zmacknute_klavesy = set()
skore = [9,9]
text = "koniec"





def vykresli_obdlznik(x1, y1, x2, y2):
    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()
def nakresli_text(text, x, y, pozicia_x):
    napis = pyglet.text.Label(
        text,
        font_size=VELKOST_FONTU,
        x=x,
        y=y,
        anchor_x=pozicia_x
    )
    napis.draw()


def reset():
    pozicia_lopty[0] = sirka // 2
    pozicia_lopty[1] = vyska // 2
    # X-OVA RYCHLOST
    if random.randint(0, 1):
        rychlost_lopty[0] = RYCHLOST
    else:
        rychlost_lopty[0] = -RYCHLOST

    # y-ova rychlost - uplne nahodna
    rychlost_lopty[1] = random.uniform(-1, 1) * RYCHLOST


def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        zmacknute_klavesy.add(('hore', 0))
    if symbol == key.S:
        zmacknute_klavesy.add(('dole', 0))
    if symbol == key.UP:
        zmacknute_klavesy.add(('hore', 1))
    if symbol == key.DOWN:
        zmacknute_klavesy.add(('dole', 1))

def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        zmacknute_klavesy.discard(('hore', 0))
    if symbol == key.S:
        zmacknute_klavesy.discard(('dole', 0))
    if symbol == key.UP:
        zmacknute_klavesy.discard(('hore', 1))
    if symbol == key.DOWN:
        zmacknute_klavesy.discard(('dole', 1))

def vykresli():
    #vykresli stav hry
    gl.glClear(gl.GL_COLOR_BUFFER_BIT) #smaz obsah okna
    gl.glColor3f(1, 1, 1) #nastav farbu
    vykresli_obdlznik(
        pozicia_lopty[0] - velkost_lopty//2,
        pozicia_lopty[1] - velkost_lopty//2,
        pozicia_lopty[0] + velkost_lopty//2,
        pozicia_lopty[1] + velkost_lopty//2
    )
    for x,y in [(0, pozicia_palok[0]), (sirka, pozicia_palok[1])]:
       vykresli_obdlznik(
            x - dlzka_palky,
            y - vyska_palky // 2,
            x + dlzka_palky,
            y + vyska_palky //2

       )
    for y in range(ciara_hrubka //2, vyska, ciara_hrubka * 2):
        vykresli_obdlznik(
            sirka//2-1,
            y,
            sirka//2+1,
            y + ciara_hrubka
        )
    #skore
    nakresli_text(str(skore[0]), x=ODSADENIE_TEXTU, y=vyska - ODSADENIE_TEXTU - VELKOST_FONTU, pozicia_x='left')
    nakresli_text(str(skore[1]), x=sirka-ODSADENIE_TEXTU, y=vyska-ODSADENIE_TEXTU-VELKOST_FONTU,pozicia_x='right')
    nakresli_text(text, x=ODSADENIE_TEXTU, y=vyska - ODSADENIE_TEXTU - VELKOST_FONTU, pozicia_x='center')


def obnov_stav(dT):
    #pohyb palok
    if skore[0] == 10 or skore[1] == 10:
        nakresli_text(text, x=ODSADENIE_TEXTU, y=vyska - ODSADENIE_TEXTU - VELKOST_FONTU, pozicia_x='center')
    for cislo_palky in (0,1):
        if ('hore', cislo_palky) in zmacknute_klavesy:
            pozicia_palok[cislo_palky] += RYCHLOST_PALKY*dT
        if ('dole', cislo_palky) in zmacknute_klavesy:
            pozicia_palok[cislo_palky] -= RYCHLOST_PALKY * dT

        #dolna zarazka
        if pozicia_palok[cislo_palky] < vyska_palky /2:
            pozicia_palok[cislo_palky] = vyska_palky /2
        #horna zarazka
        if pozicia_palok[cislo_palky] > vyska - vyska_palky/2:
            pozicia_palok[cislo_palky] = vyska - vyska_palky/2
    #pohyb lopty
    pozicia_lopty[0] += rychlost_lopty[0] * dT
    pozicia_lopty[1] += rychlost_lopty[1] * dT

    #odrazenie lopty
    if pozicia_lopty[1] < velkost_lopty:
        rychlost_lopty[1] = abs(rychlost_lopty[1])
    if pozicia_lopty[1] > vyska - velkost_lopty//2:
        rychlost_lopty[1] = -abs(rychlost_lopty[1]) / 2
    #zistenie borderov palky
    palka_min = pozicia_lopty[1] - velkost_lopty/2 - vyska_palky/2
    palka_max = pozicia_lopty[1] + velkost_lopty/2 + vyska_palky/2

    #odraz zlava
    if pozicia_lopty[0] < dlzka_palky + velkost_lopty/2:
        if palka_min < pozicia_palok[0] < palka_max:
            #odrazime loptu
            rychlost_lopty[0] = abs(rychlost_lopty[0])
        else:
            #palka jeinde ako lopta a hrac prehral
            skore[1] += 1
            reset()



    #odarz zprava
    if pozicia_lopty[0] > sirka - (dlzka_palky + velkost_lopty/2):
        if palka_min < pozicia_palok[1] < palka_max:
            # odrazime loptu
            rychlost_lopty[0] = -abs(rychlost_lopty[0])
        else:
            # palka je inde ako lopta a hrac prehral
            skore[0] += 1
            reset()


reset()
window = pyglet.window.Window(width=sirka, height=vyska)
window.push_handlers(
    on_draw = vykresli,
    on_key_press =stisk_klavesnice,
    on_key_release=pusti_klavesnice,
)

pyglet.clock.schedule(obnov_stav)











pyglet.app.run()