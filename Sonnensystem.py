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

# Gravitationskonstante "G"
G = 6.6743 * 10 ** -11


class Planet:  # Beinhält die Sonne obwohl die Sonne kein Planet ist

    def __init__(self, masse, radius, x, y):
        self.masse = masse
        self.radius = radius
        self.x = x
        self.y = y

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
        return G * ((self.masse * other.masse) / d ** 2)


Sonne = Planet(sonne_masse, sonne_radius, 0, 0)
Merkur = Planet(merkur_masse, merkur_radius, 100, 0)

print(Merkur.anziehung(Sonne, Merkur.distanz(Sonne)))

# Main Game loop

running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenster.fill("black")

    # Planeten zeichnen
    Sonne.zeichnen("yellow")
    Merkur.zeichnen("orange")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
