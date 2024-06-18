import pygame
import math

pygame.init()

fenster_breite = 1400
fenster_hoehe = 900

# Fenster kreieren
fenster = pygame.display.set_mode((fenster_breite, fenster_hoehe))
pygame.display.set_caption("Sonnensystem")

# Attribute Planeten
masse = {"sonne": 1.989 * 10 ** 30, "merkur": 3.285 * 10 ** 23, "venus": 4.87 * 10 ** 24, "erde": 5.97 * 10 ** 24,
         "mars": 6.42 * 10 ** 23, "jupiter": 1.898 * 10 ** 27, "saturn": 5.68 * 10 ** 26, "uranus": 8.68 * 10 ** 25,
         "neptun": 1.02 * 10 ** 26, "mond" : 7.3 * 10 ** 22, "phobos": 1.08 * 10 ** 15, "deimos": 1.8 * 10 ** 15}
geschwindigkeit = {"merkur": 0.003, "venus": 0.002, "erde": 0.0018, "mars": 0.0016, "jupiter": 0.0014, "saturn": 0.0013,
                   "uranus": 0.0012, "neptun": 0.0011, "mond" : 0.0025, "phobos": 0.002, "deimos": 0.002}

# Gravitationskonstante "G" mal den faktor  10 ^ -23
G = 6.6743 * 10 ** -34

# Dauer zwischen dem Update der Position in Sekunden 
ZEITSPRUNG = 750

# maximal gespeicherte Werte für die Umlaufbahn
MAX = 2500



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

    def zeichnen(self):
        x = self.x + (fenster_breite // 2) - 32
        y = self.y + (fenster_hoehe // 2) - 32

        # Überprüfen ob die Liste genügend Elemente
        if len(self.umlaufbahn) >= 2:
            # Umlaufbahn zentrieren
            angepasste_umlaufbahn = [(point[0] + fenster_breite // 2, point[1] + fenster_hoehe // 2) for point in
                                     self.umlaufbahn]
            pygame.draw.lines(fenster, "white", False, angepasste_umlaufbahn, 1)

        self.rect.center = (self.x + fenster_breite // 2, self.y + fenster_hoehe // 2)
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
    
# Kreiert eine Textbox an Position xy
def textbox(text, x, y):
    box = pygame.font.SysFont("Arial", 20).render(text, True, "white")
    fenster.blit(box, (x, y))

# planeten kreieren
def planeten_kreieren():
    Sonne = Planet("sonne", "planeten/sonne.png", masse["sonne"], 0, 0, 0)
    Merkur = Planet("merkur", "planeten/merkur.png", masse["merkur"], 100, 0, geschwindigkeit["merkur"])
    Venus = Planet("venus", "planeten/venus.png", masse["venus"], 180, 0, geschwindigkeit["venus"])
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

Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()

# Main Game loop
running = True
# Überprüft ob die Jupitermonde schon gezeichnet wurden
erster_durchlauf = True
lst = []
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Position updaten und Planeten zeichnen
    fenster.fill("black")
    Sonne.zeichnen()
    for planet in planeten:
        planet.neue_pos(ZEITSPRUNG, Sonne)
        planet.zeichnen()
        if planet.kollision() and pygame.mouse.get_pressed()[0]:
            name = planet.name
            running = False
        
    pygame.display.flip()
    clock.tick(60)


    # Merkur Schleife
    while not running and name == "merkur":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        fenster.fill("black")
        Merkur = Planet("merkur", "planeten/merkur.png", masse["merkur"], 0, 0, 0)
        Merkur.img = pygame.transform.scale(Merkur.img, (128, 128))
        Merkur.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Merkur.img, Merkur.rect) 
        textbox("Merkur", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Venus Schleife
    while not running and name == "venus":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        fenster.fill("black")
        Venus = Planet("venus", "planeten/venus.png", masse["venus"], 0, 0, 0)
        Venus.img = pygame.transform.scale(Venus.img, (128, 128))
        Venus.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Venus.img, Venus.rect) 
        textbox("Venus", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Erde Schleife
    while not running and name == "erde":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        # G den neuen Umständen anpassen (Physikalisch inkorrekt)
        G_E = 2 * 10 ** -28
        fenster.fill("black")
        Erde = Planet("erde", "planeten/erde.png", masse["erde"], 0, 0, 0)
        Erde.img = pygame.transform.scale(Erde.img, (128, 128))
        Erde.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        Mond.neue_pos(ZEITSPRUNG, Erde, G_E)
        Mond.zeichnen()
        fenster.blit(Erde.img, Erde.rect) 
        textbox("Erde", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Mars Schleife
    while not running and name == "mars":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True
        # G den neuen Umständen anpassen (Physikalisch inkorrekt)
        G_M = 1.5 * 10 ** -27
        fenster.fill("black")
        Mars = Planet("mars", "planeten/mars.png", masse["mars"], 0, 0, 0)
        Mars.img = pygame.transform.scale(Mars.img, (128, 128))
        Mars.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Mars.img, Mars.rect) 
        Phobos.neue_pos(ZEITSPRUNG, Mars, G_M)
        Phobos.zeichnen()
        Deimos.neue_pos(ZEITSPRUNG, Mars, G_M)
        Deimos.zeichnen()
        textbox("Mars", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Jupiter Schleife
    while not running and name == "jupiter":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        # G den neuen Umständen anpassen (Physikalisch inkorrekt)
        G_J = 1.5 * 10 ** -23          
        fenster.fill("black")
        Jupiter = Planet("jupiter", "planeten/jupiter.png", masse["jupiter"], 0, 0, 0)
        Jupiter.img = pygame.transform.scale(Jupiter.img, (128, 128))
        Jupiter.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Jupiter.img, Jupiter.rect) 

        # 92 Monde von Jupiter 
        if erster_durchlauf:
            for i in range(80, 635, 6):
                M = Planet("m", "planeten/mond.png", 10 ** 15, i, 0, geschwindigkeit["mond"])
                M.img = pygame.transform.scale(M.img, (3, 3))
                lst.append(M)
            erster_durchlauf = False 
            

        for m in lst:
            m.neue_pos(ZEITSPRUNG, Jupiter, G_J)
            m.zeichnen()
            
        textbox("Jupiter", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Saturn Schleife
    while not running and name == "saturn":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        fenster.fill("black")
        Saturn = Planet("saturn", "planeten/saturn.png", masse["saturn"], 0, 0, 0)
        Saturn.img = pygame.transform.scale(Saturn.img, (128, 128))
        Saturn.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Saturn.img, Saturn.rect) 
        textbox("Saturn", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Uranus Schleife
    while not running and name == "uranus":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        fenster.fill("black")
        Uranus = Planet("uranus", "planeten/uranus.png", masse["uranus"], 0, 0, 0)
        Uranus.img = pygame.transform.scale(Uranus.img, (128, 128))
        Uranus.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Uranus.img, Uranus.rect) 
        textbox("Uranus", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)

    # Neptun Schleife
    while not running and name == "neptun":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     

            # Methode um zurück zur Standartansicht zu kommen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Sonne, Mond, Phobos, Deimos, planeten = planeten_kreieren()
                    running = True

        fenster.fill("black")
        Neptun  = Planet("neptun", "planeten/neptun.png", masse["neptun"], 0, 0, 0)
        Neptun.img = pygame.transform.scale(Neptun.img, (128, 128))
        Neptun.rect.center = ((fenster_breite // 2) -64, (fenster_hoehe // 2) -64)
        fenster.blit(Neptun.img, Neptun.rect) 
        textbox("Neptun", fenster_breite - 300, 30)  
        textbox("Test", fenster_breite - 300, 50)  

        pygame.display.flip()
        clock.tick(60)