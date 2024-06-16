# Sonnensystem

Journal:

Nützliche Videos Sammlung:
https://www.youtube.com/watch?v=WTLPmUHTPqo

Git und Github:
https://www.youtube.com/watch?v=tRZGeaHPoaw
- Git instaliert (https://www.git-scm.com/)
- Git repository kreiert und Dateien commited
- Github account erstellt (github.com)
- local repository auf Github gepushed
- Von Vscode auf Github gepushed

Infos Planeten:
https://nssdc.gsfc.nasa.gov/planetary/factsheet/

Pygame:
https://www.pygame.org/


Vorgehensweise:
Pygame Fenster setup und Loop starten
Planeten Klasse initalisieren
Sonne erstellen und Darstellen 
Merkur hinzufügen
Umlaufbahn berechnen



Pygame Fenster integriert und eine simple Gameloop instaliert
Die Klasse Planeten erstellt und mit der __init__ Funktion initialisiert.
Zeichnenfunktion zur Klasse Planeten hinzugefügt. 
Das Objekt Sonne erstellt und gezeichnet.

Ich habe mich dazu entschlossen, mit einer realistischen Masse zu arbeiten, jedoch den Planetradius arbiträr zu wählen. 
Die Masse werde ich mit einem Skalar passend verkleinern

Habe eine Funktion hinzugefügt welche die distanz zwischen zwei Planeten bzw. einem Planeten und der Sonne berechnet. 
https://stackoverflow.com/questions/55780439/how-to-use-a-method-in-a-class-to-compare-two-objects-of-the-class (Habe "other" verwendet)
Funktion hinzugefügt um die Anziehung zwischen zwei Körpern zu berechnen. 


Anziehungsfunktion Geändert, so dass die x- und die y-Komponente ersichtlich sind.
Eine Funktion hinzugefügt welche die Position der Planeten updated.
Kurzeitige Probleme aufgrung eines ZeroDivisionErrors.
Der Fehler lag an der Berechnung des Winkels zwischen der x- und der y-Komponente. 
Ich hatte die beiden vertauscht.
Ein weiteres Problem ist, dass Merkur nicht mehr angezeigt wird. 
Herausgefunden, dass der Fehler an einer viel zu starken Gravitation lag. 
Diese um den Faktor 10^-20 verringert indem ich die Gravitationskonstante "G" mit ihr multipliziert habe.
Planet bewegt sich momentan noch auf der Horizontale und weg von der Sonne.
Warum dies geschieht weiss ich momentan noch nicht. 
Problem behoben indem ich die Winkelfunktion korrigiert habe. 
Die Umlaufbahn des Planeten Merkur hinzugefügt indem ich mit der y-geschwindigkeit experimentiert habe. 

Zeitschritt in Variabel geschpeichert. 
Umlaufbahn programmiert. Fehler das noch nicht genug Werte vorhanden sind.
(ValueError: points argument must contain 2 or more points)
Gelöst indem ich ein If-statment eingefügt habe welches überprüft ob genügend Werte vorhanden sind.
Die Umlaufbahn wurde nicht relativ zum Fenster gezeichnet. Gelöst indem man es an der Fenstermitte orientiert. (ChatGPt) 
Die Umlaufbahn wird mehrmals übereinander gezeichnet, was unschön ist. 
Maximallänge für die Umlaufbahn eingefügt. (Schwachstelle dabei liegt, dass wenn der Zeitschrit zu klein ist, die Umlaufbahn zu kurz ist)

Ich habe für alle Planeten eine Masse, einen angepassten Radius und eine angepasste Geschwindigkeit hinzugefügt. (Notiz: evt. in Zukunft durch ein Dict ersetzen) 

Alle Planeten kreiert.

Planetenfarben hinzugefügt. (https://sites.google.com/view/paztronomer/blog/basic/python-colors)

Alle Atribute der Planeten (Masse, Radius und Geschwindigkeit) in Dictionarrys gepackt um das Programm kürzer und übersichtlicher
zu machen. 

Ich habe die Farbe aller Umlaufbahnen weiss gemacht, um die Simulation übersichtlicher zu machen. 
Überkreuzungen zwischen den Planetenbahnen entfernt. 

Icons hinzugefügt und die Planeten als rects dargestellt. Dabei unteranderem die init-Funktion, die Zeichnen-Funktion und
die Erstellung der Planetobjekten angepasst.
https://www.flaticon.com/
Sonne:
<a href="https://www.flaticon.com/free-icons/sun" title="sun icons">Sun icons created by Freepik - Flaticon</a> 
Merkur:
<a href="https://www.flaticon.com/free-icons/mercury" title="mercury icons">Mercury icons created by Freepik - Flaticon</a>
Venus:
<a href="https://www.flaticon.com/free-icons/venus" title="venus icons">Venus icons created by Freepik - Flaticon</a>
Erde:
<a href="https://www.flaticon.com/free-icons/globe" title="globe icons">Globe icons created by Freepik - Flaticon</a>
Mars:
<a href="https://www.flaticon.com/free-icons/planet" title="planet icons">Planet icons created by Freepik - Flaticon</a>
Jupiter:
<a href="https://www.flaticon.com/free-icons/jupiter" title="jupiter icons">Jupiter icons created by Freepik - Flaticon</a>
Saturn:
<a href="https://www.flaticon.com/free-icons/planet" title="planet icons">Planet icons created by Freepik - Flaticon</a>
Uranus:
<a href="https://www.flaticon.com/free-icons/uranus" title="uranus icons">Uranus icons created by Muhammad_Usman - Flaticon</a>
Neptun:
<a href="https://www.flaticon.com/free-icons/planet" title="planet icons">Planet icons created by Freepik - Flaticon</a>

Funktion hinzugefügt welche testet, ob der Mauszeiger und ein Planet überlappen:
https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint

Radien entfernt da sie nicht mehr zum zeichnen der Kreise benötigt werden. 

Neue Schleife eingebaut welche läuft, wenn man einen Planeten anklickt.
https://www.pygame.org/docs/ref/mouse.html
Problem: Kann noch nicht erkennen welcher Planet geklickt wird. 
Lösung: Planetnamen in die init funktion aufnehmen und nach anklicken speichern. 
Schleife angepasst, so dass sie nur die Erde im Zentrum zeigt wenn man diese Anklickt.
-> Grundlage für die weiteren Schleifen.  
Zoom hinzugefügt:
https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale