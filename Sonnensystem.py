import pygame
import math
import webbrowser

pygame.init()

# Fenster kreieren
fenster_breite = 1400
fenster_hoehe = 900
icon = pygame.image.load("erde_klein.png")
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Sonnensystem")
pygame.display.set_icon(icon)


# Attribute Planeten
masse = {"sonne": 1.989 * 10 ** 30, "merkur": 3.285 * 10 ** 23, "venus": 4.87 * 10 ** 24, "erde": 5.97 * 10 ** 24,
         "mars": 6.42 * 10 ** 23, "jupiter": 1.898 * 10 ** 27, "saturn": 5.68 * 10 ** 26, "uranus": 8.68 * 10 ** 25,
         "neptun": 1.02 * 10 ** 26, "mond": 7.3 * 10 ** 22, "phobos": 1.08 * 10 ** 15, "deimos": 1.8 * 10 ** 15,
         "io": 8.932 * 10 ** 22, "europa": 4.8 * 10 ** 22,  "ganymed": 1.482 * 10 ** 23, "callisto": 1.076 * 10 ** 23, 
         "rhea": 2.31 * 10 ** 21, "titan": 1.345 * 10 ** 23, "titania": 3.42 * 10 ** 21, "oberon": 2.88 * 10 ** 21,
         "triton": 2.14 * 10 ** 22}
geschwindigkeit = {"merkur": -0.003, "venus": -0.002, "erde": -0.0018, "mars": -0.0016, "jupiter": -0.0014, "saturn": -0.0013,
                   "uranus": -0.0012, "neptun": -0.0011, "mond": -0.0025, "phobos": -0.002, "deimos": -0.002, "io": -0.002,
                   "europa": -0.0019, "ganymed": -0.0018, "callisto": -0.0017, "rhea": -0.002, "titan": -0.002, "titania": -0.002,
                   "oberon": -0.002, "triton": 0.002}
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

wiki_text = "Mehr lesen in Wikipedia"
wiki_font = pygame.font.SysFont("Arial", 20)
wiki_link = wiki_font.render(wiki_text, True, "blue")
wiki_rect = wiki_link.get_rect()


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
    Io = Planet("io", "planeten/io.png", masse["io"], 250, 0, geschwindigkeit["io"])
    Europa = Planet("europa", "planeten/europa.png", masse["europa"], 300, 0, geschwindigkeit["europa"])
    Ganymed = Planet("ganymed", "planeten/ganymed.png", masse["ganymed"], 350, 0, geschwindigkeit["ganymed"])
    Callisto = Planet("callisto", "planeten/callisto.png", masse["callisto"], 400, 0, geschwindigkeit["callisto"])
    Rhea = Planet("rhea", "planeten/rhea.png", masse["rhea"], 300, 0, geschwindigkeit["rhea"])
    Titan = Planet("titan", "planeten/titan.png", masse["titan"], 400, 0, geschwindigkeit["titan"])
    Titania = Planet("titania", "planeten/titania.png", masse["titania"], 300, 0, geschwindigkeit["titania"])
    Oberon =  Planet("oberon", "planeten/oberon.png", masse["oberon"], 350, 0, geschwindigkeit["oberon"])
    Triton = Planet("triton", "planeten/triton.png", masse["triton"], 250, 0, geschwindigkeit["triton"])
    planeten = [Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun]
    return Sonne, Mond, Phobos, Deimos, Io, Europa, Ganymed, Callisto, Rhea, Titan, Titania, Oberon, Triton, planeten

def monde_kreieren():
    monde = []
    def monde_append(planeten, groesse, start):
            for i in range(start, (planeten * groesse) + start , groesse):
                M = Planet("m", "planeten/mond.png", 10 ** 15, i if i % 2 == 0 else -i, 0, geschwindigkeit["mond"])
                M.img = pygame.transform.scale(M.img, (3, 3))
                monde.append(M)
        
    if name == "jupiter":
        monde_append(91, 5, 80)
    elif name == "saturn":
        monde_append(143, 5, 80)
    elif name == "uranus":
        monde_append(26, 5, 110)
    elif name == "neptun":
        monde_append(15, 7, 110)
    return monde

def monde_update(monde, planet, G):
    for m in monde:
        m.neue_pos(ZEITSPRUNG, planet, G)
        m.zeichnen(False)
        
def mond_update(mond, G):
    planet = Planet(name, "planeten/{}.png".format(name), masse[name], 0, 0, 0)
    mond.neue_pos(ZEITSPRUNG, planet, G)
    mond.zeichnen()
    if mond != Mond:
        beschriften(mond)

def info():
    global esc_rect, wiki_rect
    
    textbox([name.upper(), "Monde: {}".format(anz_monde[name]), "Masse: {:.2e} kg".format(masse[name]),
             "Durchschnittstemperatur: {}°C".format(temp[name]), "Umlaufdauer: {} Tage".format(umlaufdauer[name]),
             "Durchmesser: {} km".format(durchmesser[name]), "Distanz zur Sonne: {:.2e} km".format(distanz_sonne[name])],
            fenster_breite - 300, 30)
    
    wiki_text = "Mehr lesen in Wikipedia"
    wiki_font = pygame.font.SysFont("Arial", 20)
    wiki_link = wiki_font.render(wiki_text, True, "blue")
    wiki_rect = wiki_link.get_rect()
    wiki_rect.topleft = (fenster_breite - 300, 240)
    fenster.blit(wiki_link, wiki_rect)
    
    esc_icon = pygame.image.load("esc.png")
    esc_rect = esc_icon.get_rect()
    esc_rect.topleft = (10, 10)
    fenster.blit(esc_icon, esc_rect)

def beschriften(mond, x_verschiebung=10, y_verschiebung=25):
    font = pygame.font.SysFont("Arial", 15)
    text = font.render(mond.name.capitalize(), True, "white")
    text_rect = text.get_rect(center=(mond.rect.centerx + x_verschiebung, mond.rect.centery + y_verschiebung))
    fenster.blit(text, text_rect)
    
def planet_update(monde=None, G=None):
    fenster.fill("black")
    planet = Planet(name, "planeten_gross/{}.png".format(name), masse[name], 0, 0, 0)
    planet.img = pygame.transform.scale(planet.img, (128, 128))
    fenster.blit(planet.img, planet.rect)
    if monde != None:
        monde_update(monde, planet, G)
    info()

def update():
    pygame.display.flip()
    clock.tick(60)

# läst die Planeten kreation vorlaufen um eine Spirale zu umgehen
def vorlaufen(G, n=1000):
    planet = Planet(name, "planeten/{}.png".format(name), masse[name], 0, 0, 0)
    for i in range(n):
        for m in monde:
            m.neue_pos(ZEITSPRUNG, planet, G)

def starten():
    global monde, jup_gest, sat_gest, ura_gest, nep_gest
    
    if name == "jupiter" and not jup_gest:
        monde = monde_kreieren()
        jup_gest = True
        vorlaufen(G_J, 2000)
    elif name == "saturn" and not sat_gest:
        monde = monde_kreieren()
        sat_gest = True
        vorlaufen(G_S, 2000)
    elif name == "uranus" and not ura_gest:
        monde = monde_kreieren()
        ura_gest = True
        vorlaufen(G_U)
    elif name == "neptun" and not nep_gest:
        monde = monde_kreieren()
        nep_gest = True
        vorlaufen(G_N)
        
def quit_check():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Methode um zurück zur Standartansicht zu kommen
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Sonne, Mond, Phobos, Deimos, Io, Europa, Ganymed, Callisto, Rhea, Titan, Titania, Oberon, Triton, planeten = planeten_kreieren()
                        running = True
        elif esc_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Sonne, Mond, Phobos, Deimos, Io, Europa, Ganymed, Callisto, Rhea, Titan, Titania, Oberon, Triton, planeten = planeten_kreieren()
            running = True
        elif wiki_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if name != "erde": 
                webbrowser.open("https://de.wikipedia.org/wiki/{}_(Planet)".format(name.capitalize()))    
            else:
                webbrowser.open("https://de.wikipedia.org/wiki/Erde")
                   
Sonne, Mond, Phobos, Deimos, Io, Europa, Ganymed, Callisto, Rhea, Titan, Titania, Oberon, Triton, planeten = planeten_kreieren()

name = ''
monde = ''
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
        planet_update()
        update()

    # Venus Schleife
    while not running and name == "venus":
        quit_check()
        planet_update()
        update()

    # Erde Schleife
    while not running and name == "erde":
        quit_check()
        planet_update()
        mond_update(Mond, G_E)
        update()

    # Mars Schleife
    while not running and name == "mars":
        quit_check()
        planet_update()
        mond_update(Phobos, G_M)
        mond_update(Deimos, G_M)
        update()

    # Jupiter Schleife
    while not running and name == "jupiter":
        starten()            
        quit_check()
        planet_update(monde, G_J)
        mond_update(Io, G_J)
        mond_update(Europa, G_J)
        mond_update(Ganymed, G_J)
        mond_update(Callisto, G_J)
        update()

    # Saturn Schleife
    while not running and name == "saturn":
        starten()
        quit_check()
        planet_update(monde, G_S)
        mond_update(Rhea, G_S)
        mond_update(Titan, G_S)
        update()

    # Uranus Schleife
    while not running and name == "uranus":
        starten()
        quit_check()
        planet_update(monde, G_U)
        mond_update(Titania, G_U)
        mond_update(Oberon, G_U)
        update()

    # Neptun Schleife
    while not running and name == "neptun":
        starten()
        quit_check()
        planet_update(monde, G_N)
        mond_update(Triton, G_N)
        update()
