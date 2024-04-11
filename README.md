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
Problem behoben in dem ich die Winkelfunktion korrigiert habe. 

