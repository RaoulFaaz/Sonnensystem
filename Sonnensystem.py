import pygame
import math

pygame.init()

fenster_breite = 1200
fenster_hoehe = 900

# Fenster kreieren
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Sonnensystem")

# Infos Sonne
sonne_masse = 1.989 * 10 ** 30
sonne_radius = 25

# Infos Merkur
merkur_masse = 3.285 * 10 ** 23
merkur_radius = 6
merkur_geschwindigkeit = 0.003
# Infos Venus
venus_masse = 4.87 * 10 ** 24
venus_radius = 9
# Infos Erde
erde_masse = 5.97 * 10 ** 24
erde_radius = 9
# Infos Mars
mars_masse = 6.42 * 10 ** 23
mars_radius = 7
# Infos Jupiter
jupiter_masse = 1.898 * 10 ** 27
jupiter_radius = 15
# Infos Saturn
saturn_masse = 5.68 * 10 ** 26
saturn_radius = 13
# Infos Uranus
uranus_masse = 8.68 * 10 ** 25
uranus_radius = 12
# Infos Neptun
neptun_masse = 1.02 * 10 ** 26
nepturn_radius = 12



# Gravitationskonstante "G" mal den faktor  10 ^ -23
G = 6.6743 * 10 ** -11 * 10 ** -23

# Dauer zwischen dem Update der Position in Sekunden 

zeitsprung = 1000

class Planet:  # Beinhält die Sonne obwohl die Sonne kein Planet ist

    def __init__(self, masse, radius, x, y, vx = 0, vy = 0):
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
            angepasste_umlaufbahn = [(point[0] + fenster_breite // 2, point[1] + fenster_hoehe // 2) for point in self.umlaufbahn]
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
        
        if len(self.umlaufbahn) > 2000:
            self.umlaufbahn.pop(0) 

        


Sonne = Planet(sonne_masse, sonne_radius, 0, 0)
Merkur = Planet(merkur_masse, merkur_radius, 100, 0)
Merkur.vy = merkur_geschwindigkeit

# Main Game loop

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenster.fill("black")

    # position updaten
    Merkur.neue_pos(zeitsprung)

    # Planeten zeichnen
    Sonne.zeichnen("yellow")
    Merkur.zeichnen("orange")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
