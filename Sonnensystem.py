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
sonne_radius = 20

# Infos Merkur
merkur_masse = 3.285 * 10 ** 23
merkur_radius = 3



# Gravitationskonstante "G" mal den faktor  10 ^ -23
G = 6.6743 * 10 ** -11 * 10 ** -23


class Planet:  # Beinhält die Sonne obwohl die Sonne kein Planet ist

    def __init__(self, masse, radius, x, y, vx = 0, vy = 0):
        self.masse = masse
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def zeichnen(self, farbe):
        x = self.x + fenster_breite // 2
        y = self.y + fenster_hoehe // 2
        pygame.draw.circle(fenster, farbe, (x, y), self.radius)

    # Distanz zwischen zwei Körpern berechnen mit Pythagoras
    def distanz(self, other):
        x = self.x - other.x
        y = self.y - other.y

        return math.sqrt(x ** 2 + y ** 2)

    def anziehung(self, other, d):
        Fg = G * ((self.masse * other.masse) / d ** 2)
        winkel = math.atan2((self.y - other.y), (self.x - other.x))
        Fg_x = math.cos(winkel) * Fg
        Fg_y = math.sin(winkel) * Fg

        return Fg_x, Fg_y
    
    def neue_pos(self, zeit):
        fx, fy = self.anziehung(Sonne, self.distanz(Sonne))
        # Geschwindikeit berechnen indem man a * m durch m und dann durch die zeit rechnet
        self.vx += fx / self.masse * zeit
        self.vy += fy / self.masse * zeit

        # die neue position berechnen
        self.x += self.vx * zeit
        self.y += self.vy * zeit
    


Sonne = Planet(sonne_masse, sonne_radius, 0, 0)
Merkur = Planet(merkur_masse, merkur_radius, 100, 0)
planeten = [Sonne, Merkur]

# Main Game loop

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenster.fill("black")

    # position updaten
    Merkur.neue_pos(100)

    # Planeten zeichnen
    Sonne.zeichnen("yellow")
    Merkur.zeichnen("orange")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
