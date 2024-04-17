import pygame
import math

pygame.init()

fenster_breite = 1400
fenster_hoehe = 900

# Fenster kreieren
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Sonnensystem")

masse = {"sonne": 1.989 * 10 ** 30, "merkur": 3.285 * 10 ** 23, "venus": 4.87 * 10 ** 24, "erde": 5.97 * 10 ** 24,
         "mars": 6.42 * 10 ** 23, "jupiter": 1.898 * 10 ** 27, "saturn": 5.68 * 10 ** 26, "uranus": 8.68 * 10 ** 25,
         "neptun": 1.02 * 10 ** 26}
radius = {"sonne" : 25, "merkur" : 6, "venus" : 9, "erde" : 9, "mars" : 7, "jupiter" : 15, "saturn" : 13, "uranus" : 12, "neptun" : 12}
geschwindigkeit = {"merkur" : 0.003, "venus" : 0.002, "erde" : 0.001, "mars" : 0.001, "jupiter" : 0.001, "saturn" : 0.001, "uranus" : 0.001, "neptun" : 0.001}


# Gravitationskonstante "G" mal den faktor  10 ^ -23
G = 6.6743 * 10 ** -11 * 10 ** -23

# Dauer zwischen dem Update der Position in Sekunden 

zeitsprung = 1000


class Planet:  # Beinhält die Sonne obwohl die Sonne kein Planet ist

    def __init__(self, farbe, masse, radius, x, y, vy, vx=0):
        self.farbe = farbe
        self.masse = masse
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.umlaufbahn = []

    def zeichnen(self, farbe):
        x = self.x + fenster_breite // 2
        y = self.y + fenster_hoehe // 2
        pygame.draw.circle(fenster, farbe, (x, y), self.radius)

        # Überprüfen ob die Liste genügend Elemente
        if len(self.umlaufbahn) >= 2:
            # Umlaufbahn zentrieren
            angepasste_umlaufbahn = [(point[0] + fenster_breite // 2, point[1] + fenster_hoehe // 2) for point in
                                     self.umlaufbahn]
            pygame.draw.lines(fenster, farbe, False, angepasste_umlaufbahn, 1)

    # Distanz zwischen zwei Körpern berechnen mit Pythagoras
    def distanz(self, other):
        x = self.x - other.x
        y = self.y - other.y

        return math.sqrt(x ** 2 + y ** 2)

    # Anzeihung zwischen zwei Körpern berechnen
    def anziehung(self, other, d):
        Fg = G * ((self.masse * other.masse) / d ** 2)
        winkel = math.atan2((other.y - self.y), (other.x - self.x))
        Fg_x = math.cos(winkel) * Fg
        Fg_y = math.sin(winkel) * Fg

        return Fg_x, Fg_y

    # Neue position eines Körpers berechnen
    def neue_pos(self, zeit):
        fx, fy = self.anziehung(Sonne, self.distanz(Sonne))
        # Geschwindikeit berechnen indem man a * m durch m und dann durch die zeit rechnet
        self.vx += fx / self.masse * zeit
        self.vy += fy / self.masse * zeit

        # die neue position berechnen 
        self.x += self.vx * zeit
        self.y += self.vy * zeit

        # Position speichern um später die Umlaufbahn zu zeichnen
        self.umlaufbahn.append((self.x, self.y))

        # Überschneidungen im Orbit verhindern indem man das erste Element löscht, falls die Liste zu lang wird

        if len(self.umlaufbahn) > 1600:
            self.umlaufbahn.pop(0)

        # planeten kreieren


Sonne = Planet("yellow", masse["sonne"], radius["sonne"], 0, 0, 0)
Merkur = Planet("grey", masse["merkur"], radius["merkur"], 100, 0, geschwindigkeit["merkur"])
Venus = Planet("palegoldenrod", masse["venus"], radius["venus"], 180, 0, geschwindigkeit["venus"])
Erde = Planet("blue", masse["erde"], radius["erde"], 260, 0, geschwindigkeit["erde"])
Mars = Planet("firebrick", masse["mars"], radius["mars"], 340, 0, geschwindigkeit["mars"])
Jupiter = Planet("darkgoldenrod", masse["jupiter"], radius["jupiter"], 420, 0, geschwindigkeit["jupiter"])
Saturn = Planet("lightgoldenrodyellow", masse["saturn"], radius["saturn"], 500, 0, geschwindigkeit["saturn"])
Uranus = Planet("paleturquoise", masse["uranus"], radius["uranus"], 580, 0, geschwindigkeit["uranus"])
Neptun = Planet("steelblue", masse["neptun"], radius["neptun"], 660, 0, geschwindigkeit["neptun"])
planeten = [Merkur, Venus, Erde, Mars, Jupiter, Saturn, Uranus, Neptun]

# Main Game loop
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Position updaten und Planeten zeichnen
    fenster.fill("black")
    Sonne.zeichnen(Sonne.farbe)
    for planet in planeten:
        planet.zeichnen(planet.farbe)
        planet.neue_pos(zeitsprung)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
