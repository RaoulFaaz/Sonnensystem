import pygame
import math

pygame.init()

# Fenster kreieren
fenster_breite = 1400
fenster_hoehe = 900
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Sonnensystem")

# Attribute Planeten
masse = {"sonne": 1.989 * 10 ** 30, "merkur": 3.285 * 10 ** 23, "venus": 4.87 * 10 ** 24, "erde": 5.97 * 10 ** 24,
         "mars": 6.42 * 10 ** 23, "jupiter": 1.898 * 10 ** 27, "saturn": 5.68 * 10 ** 26, "uranus": 8.68 * 10 ** 25,
         "neptun": 1.02 * 10 ** 26, "mond": 7.3 * 10 ** 22, "phobos": 1.08 * 10 ** 15, "deimos": 1.8 * 10 ** 15}
geschwindigkeit = {"merkur": -0.003, "venus": -0.002, "erde": -0.0018, "mars": -0.0016, "jupiter": -0.0014, "saturn": -0.0013,
                   "uranus": -0.0012, "neptun": -0.0011, "mond": -0.0025, "phobos": -0.002, "deimos": -0.002}
anz_monde = {"merkur": 0, "venus": 0, "erde": 1, "mars": 2, "jupiter": 95, "saturn": 146, "uranus": 28, "neptun": 16}
temp = {"merkur": 167, "venus": 464, "erde": 15, "mars": -65, "jupiter": -110, "saturn": -140, "uranus": -195,
        "neptun": -200}
umlaufdauer = {"merkur": 88, "venus": 225, "erde": 365, "mars": 687, "jupiter": 4331, "saturn": 10747, "uranus": 30589,
               "neptun": 59800}
durchmesser = {"merkur": 4879, "venus": 12104, "erde": 12756, "mars": 6792, "jupiter": 142984, "saturn": 120536,
               "uranus": 51118, "neptun": 49528}
distanz_sonne = {"merkur": 58 * 10 ** 6, "venus": 108 * 10 ** 6, "erde": 150 * 10 ** 6, "mars": 228 * 10 ** 6,
                 "jupiter": 778 * 10 ** 6, "saturn": 1432 * 10 ** 6, "uranus": 2867 * 10 ** 6, "neptun": 4515 * 10 ** 6}

# Gravitationskonstante "G" mal den faktor  10 ^ -23
G = 6.6743 * 10 ** -34
# Dauer zwischen dem Update der Position in Sekunden 
ZEITSPRUNG = 750
# maximal gespeicherte Werte für die Umlaufbahn
MAX = 2500

esc_icon = pygame.image.load("esc.png")
esc_rect = esc_icon.get_rect()


class Planet:  # Beinhält die Sonne obwohl die Sonne kein Planet ist

    def __init__(self, name, img, masse, x, y, vy, vx=0):
        self.name = name
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect(center=(x + fenster_breite // 2, y + fenster_hoehe // 2))
        self.masse = masse
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.vx = vx
        self.vy = vy
        self.umlaufbahn = []

    def zeichnen(self, umlaufbahn=True):
        # Zentrieren
        self.rect.center = (self.x + fenster_breite // 2, self.y + fenster_hoehe // 2)

        # Überprüfen ob die Liste genügend Elemente
        if len(self.umlaufbahn) >= 2 and umlaufbahn:
            # Umlaufbahn zentrieren
            angepasste_umlaufbahn = [(point[0] + fenster_breite // 2, point[1] + fenster_hoehe // 2) for point in
                                     self.umlaufbahn]
            pygame.draw.lines(fenster, "white", False, angepasste_umlaufbahn, 1)

        fenster.blit(self.img, self.rect)

    # Distanz zwischen zwei Körpern berechnen mit Pythagoras
    def distanz(self, other):
        x = self.x - other.x
        y = self.y - other.y

        return math.sqrt(x ** 2 + y ** 2)

    # Anzeihung zwischen zwei Körpern berechnen
    def anziehung(self, other, d, konst):
        Fg = konst * ((self.masse * other.masse) / d ** 2)
        winkel = math.atan2((other.y - self.y), (other.x - self.x))
        Fg_x = math.cos(winkel) * Fg
        Fg_y = math.sin(winkel) * Fg

        return Fg_x, Fg_y

    # Neue position eines Körpers berechnen
    def neue_pos(self, zeit, other, konst=G):
        fx, fy = self.anziehung(other, self.distanz(other), konst)
        # Geschwindikeit berechnen indem man a * m durch m und dann durch die Zeit rechnet
        self.vx += fx / self.masse * zeit
        self.vy += fy / self.masse * zeit

        # die neue position berechnen 
        self.x += self.vx * zeit
        self.y += self.vy * zeit

        # Position speichern um später die Umlaufbahn zu zeichnen
        self.umlaufbahn.append((self.x, self.y))

        # Überschneidungen im Orbit verhindern indem man das erste Element löscht, falls die Liste zu lang wird
        if len(self.umlaufbahn) > MAX:
            self.umlaufbahn.pop(0)

    # Überprüft ob der Mauszeiger über einem Planeten ist
    def kollision(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


# Kreiert eine Textbox an Position xy pro Element in der Liste eine Zeile
def textbox(text_liste, x, y):
    linie_h = 30
    for i, linie in enumerate(text_liste):
        box = pygame.font.SysFont("Arial", 20).render(linie, True, "white")
        fenster.blit(box, (x, y + linie_h * i))


# planeten kreieren
def planeten_kreieren():
    Sonne = Planet("sonne", "planeten/sonne.png", masse["sonne"], 0, 0, 0)
    Merkur = Planet("merkur", "planeten/merkur.png", masse["merkur"], 100, 0, geschwindigkeit["merkur"])
    Venus = Planet("venus", "planeten/venus.png", masse["venus"], 200, 0, geschwindigkeit["venus"])
    Erde = Planet("erde", "planeten/erde.png", masse["erde"], 260, 0, geschwindigkeit["erde"])
    Mars = Planet("mars", "planeten/mars.png", masse["mars"], 340, 0, geschwindigkeit["mars"])
    Jupiter = Planet("jupiter", "planeten/jupiter.png", masse["jupiter"], 420, 0, geschwindigkeit["jupiter"])
    Saturn = Planet("saturn", "planeten/saturn.png", masse["saturn"], 500, 0, geschwindigkeit["saturn"])
    Uranus = Planet("uranus", "planeten/uranus.png", masse["uranus"], 580, 0, geschwindigkeit["uranus"])
    Neptun = Planet("neptun", "planeten/neptun.png", masse["neptun"], 660, 0, geschwindigkeit["neptun"])
    Mond = Planet("mond", "planeten/mond.png", masse["mond"], 200, 0, geschwindigkeit["mond"])
    Phobos = Planet("phobos", "planeten/phobos.png", masse["phobos"], 180, 0, geschwindigkeit["phobos"])
    Deimos = Planet("deimos", "planeten/deimos.png", masse["deimos"], 240, 0, geschwindigkeit["deimos"])
    planeten = [Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun]
    return Sonne, Mond, Phobos, Deimos, planeten


def monde_kreieren(planet_name):
    monde = []
    def monde_append(planeten, groesse, start):
            for i in range(start, (planeten * groesse) + start , groesse):
                M = Planet("m", "planeten/mond.png", 10 ** 15, i if i % 2 == 0 else -i, 0, geschwindigkeit["mond"])
                M.img = pygame.transform.scale(M.img, (3, 3))
                monde.append(M)
        
    if planet_name == "jupiter":
        monde_append(95, 5, 80)
    elif planet_name == "saturn":
        monde_append(145, 5, 80)
    elif planet_name == "uranus":
        monde_append(28, 5, 110)
    elif planet_name == "neptun":
        monde_append(16, 7, 110)
    return monde


def monde_update(monde, planet, G):
    for m in monde:
        m.neue_pos(ZEITSPRUNG, planet, G)
        m.zeichnen(False)


def info(name):
    global esc_rect
    textbox([name.upper(), "Monde: {}".format(anz_monde[name]), "Masse: {:.2e} kg".format(masse[name]),
             "Durchschnittstemperatur: {}°C".format(temp[name]), "Umlaufdauer: {} Tage".format(umlaufdauer[name]),
             "Durchmesser: {} km".format(durchmesser[name]), "Distanz zur Sonne: {:.2e} km".format(distanz_sonne[name])],
            fenster_breite - 300, 30)
    esc_icon = pygame.image.load("esc.png")
    esc_rect = esc_icon.get_rect()
    esc_rect.topleft = (10, 10)
    fenster.blit(esc_icon, esc_rect)
    

def planet_update(name, monde=None, G=None):
    fenster.fill("black")
    planet = Planet(name, "planeten_gross/{}.png".format(name), masse[name], 0, 0, 0)
    planet.img = pygame.transform.scale(planet.img, (128, 128))
    fenster.blit(planet.img, planet.rect)
    if monde != None:
        monde_update(monde, planet, G)
    info(name)


def update():
    pygame.display.flip()
    clock.tick(60)


# läst die Planeten kreation vorlaufen um eine Spirale zu umgehen
def vorlaufen(name, G, n=1000):
    planet = Planet(name, "planeten/{}.png".format(name), masse[name], 0, 0, 0)
    for i in range(n):
        for m in monde:
            m.neue_pos(ZEITSPRUNG, planet, G)

def quit_check():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Methode um zurück zur Standartansicht zu kommen
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                        running = True
        elif esc_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
            running = True
                        
Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()

name = ''
jup_gest, sat_gest, ura_gest, nep_gest = False, False, False, False

# G den verschiedenen Umständen anpassen (Physikalisch inkorrekt)
G_E = 2 * 10 ** -28
G_M = 1.5 * 10 ** -27
G_J = 10 ** -30
G_S = 4 * 10 ** -30
G_U = 2 * 10 ** -29
G_N = 10 ** -29

running = True
clock = pygame.time.Clock()

# Main Game loop
while running:

    quit_check()

    # Position updaten und Planeten zeichnen
    fenster.fill("black")
    Sonne.zeichnen()
    for planet in planeten:
        planet.neue_pos(ZEITSPRUNG, Sonne)
        planet.zeichnen()
        if planet.kollision() and pygame.mouse.get_pressed()[0]:
            name = planet.name
            running = False
    update()

    # Merkur Schleife
    while not running and name == "merkur":
        quit_check()
        planet_update(name)
        update()

    # Venus Schleife
    while not running and name == "venus":
        quit_check()
        planet_update(name)
        update()

    # Erde Schleife
    while not running and name == "erde":
        quit_check()
        planet_update(name)
        Erde = Planet("erde", "planeten/erde.png", masse["erde"], 0, 0, 0)
        Mond.neue_pos(ZEITSPRUNG, Erde, G_E)
        Mond.zeichnen()
        update()

    # Mars Schleife
    while not running and name == "mars":
        quit_check()
        planet_update(name)
        Mars = Planet("mars", "planeten/mars.png", masse["mars"], 0, 0, 0)
        Phobos.neue_pos(ZEITSPRUNG, Mars, G_M)
        Phobos.zeichnen()
        Deimos.neue_pos(ZEITSPRUNG, Mars, G_M)
        Deimos.zeichnen()
        update()

    # Jupiter Schleife
    while not running and name == "jupiter":
        if not jup_gest:
            monde = monde_kreieren(name)
            jup_gest = True
            vorlaufen(name, G_J, 2000)

        quit_check()
        planet_update(name, monde, G_J)
        update()

    # Saturn Schleife
    while not running and name == "saturn":
        if not sat_gest:
            monde = monde_kreieren(name)
            sat_gest = True
            vorlaufen(name, G_S, 2000)

        quit_check()
        planet_update(name, monde, G_S)
        update()

    # Uranus Schleife
    while not running and name == "uranus":
        if not ura_gest:
            monde = monde_kreieren(name)
            ura_gest = True
            vorlaufen(name, G_U)
            
        quit_check()
        planet_update(name, monde, G_U)
        update()

    # Neptun Schleife
    while not running and name == "neptun":
        if not nep_gest:
            monde = monde_kreieren(name)
            nep_gest = True
            vorlaufen(name, G_N)

        quit_check()
        planet_update(name, monde, G_N)
        update()
