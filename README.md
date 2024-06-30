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
Die Klasse Planeten erstellt und mit der **init** Funktion initialisiert.
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

Mond Objekt hinzugefügt:
<a href="https://www.flaticon.com/free-icons/full-moon" title="full moon icons">Full moon icons created by vectorsmarket15 - Flaticon</a>
Mond in die Erde Schleife eingefügt indem ich die neue_pos-Funktion verallgemeinert habe.
Problem: Anziehung zwischen Mond und Erde zu klein und unerklärliche Bewegungen.
Lösung: Das Erde-Objekt neu definieren und die Gravitationskonstante G anpassen.
Dies ist pysikalsich nicht korrekt, da eine Konstante konstant bleiben sollte.

Funktion hinzugefügt, welche eine Textbox kreiert.
https://www.youtube.com/watch?v=ndtFoWWBAoE
Problem: Nur eine Zeile
Lösung: Momentan mehrere Befehle

Mit Escape kann man nun zur vorherigen Ansicht zurückkehren.
Problem: Planeten sind weggeschleudert worden.
Versuch eins: Die Planeten mit einer Funktion zu kreieren und diese noch mals aufzurufen wenn man esc drückt.
-> Funktioniert immer noch nicht
Lösung:
Die Funktion neue_pos so addaptiert das sie auch eine andere Gravitationskonstante Akzeptiert und als Standartwert G nimmt.
Die Planeten wurden Aufgrund der höheren Gravitation zu stark von der Sonne angezogen.
Mit einer neuen Konstante G_E wurde dieses Problem gelöst.

Merkur Schleife Hinzugefügt.
Venus Schleife Hinzugefügt.
Mars, Jupiter und Saturn Schleifen hinzugefügt. (Monde vorerst ignotiert)
Bei Jupiter, Saturn, Uranus und Neptun muss ich mich auf einige Monde begrenzen, da Sie zu viele haben.
Uranus und Neptun Schleifen hinzugefügt.

Monde:
https://nssdc.gsfc.nasa.gov/planetary/factsheet/
Icons für Phobos und Deimos, Monde von Mars generiert und zu PNGs konvertiert.
92 Monde von Jupiter mit einer for-Schleife gezeichnet, jedoch bewegen sie sich nicht.
Lösung: Die Variable erster_durchlauf, welcher True zugeteil war und die Liste lst aus der while-Loop genommen damit
sie nicht immer neu auf True gesetzt werden.
Jedoch sehe ich Jetz die Monde gar nicht mehr.
Debugging:
print(f"Mond position: x={m.x}, y={m.y}")
Mond position: x=-3678848.536564351, y=149.96010395153914
Mond position: x=-3605072.7061186978, y=149.9575681054963
Mond position: x=-3533489.1059499006, y=149.95489764255777
Mond position: x=-3464011.54928975, y=149.95208674443847
Mond position: x=-3396558.0379139986, y=149.94912939266536
Mond position: x=-3331050.5200884365, y=149.94601936302303
Mond position: x=-3267414.6646758434, y=149.94275021985868
Mond position: x=-3205579.650182312, y=149.939315310237
-> Stark negativ
-> G_J zu stark
-> G_J verkleinert aber unübersichtlich
-> Umlaufbahn Parameter zu zeichnen-Funktion hinzugefügt welcher Standartmässig auf True ist und ihn bei den Jupitermonden abgestellt.
Planeten machen Anfangs noch eine Spirale.

Monde von Saturn hinzugefügt.
Monde von Uranus hinzugefügt.
Monde von Neptun hinzugefügt.

Problem:
Nach dem Anklicken von Saturn und dem verlassen der Saturn-Schleife, werden die Monde der anderen Planeten nicht angezeigt.
Nur nach verlassen deren Schleife und erneutem anklicken sind sie sichtbar.
Das Problem begrenzt sich nicht nur auf Saturn sondern alle Planeten deren Monde mit einer for-Schleife gezeichnet werden.

Lösung:
Die Monde mit einer Funktion übersichtlich kreiert und für jeden Planet (mit vielen Monden) eine eigene Variabel hinzugefügt
welche angibt ob das Zeichnen der Monde bereits gestarted wurde.

Funktion hinzugefügt, welche die Position der Monde updatet anstatt dies in jeder Schleife zu wiederhohlen.
Funktion hinzugefügt, welche die Position der Planeten mit vielen Monden updated um den Code nicht in jeder Schleife wiederhohlen zu müssen.
Code übersichtlicher gemacht.

Funktion hinzugefügt welche den Screen updated. Bisher immer den ganzen Code wiederhohlt.

Mondumlaufbahn zu beginn zu geordnet.
Start angepasst aber immernoch zu geordnet.
Anderung rückgängig gemacht.
Funktion eingefügt welche die Planetenkreation voralufen lässt und somit die regelmässige Spirale umgeht.
Diese lässt Aufgrund der vielen berechnungen das Programm kurz stocken wenn man Jupiter oder Saturn anklickt.

Textbox Funktion so angepasst, dass sie mehrere Zeilen auf einmal rendern kann welche sie als Strings in einer Liste bekommt.
Textboxen ergänzt.

Anzahl Monde an bessere Quelle angepasst, da die Anzahl in verschiedenen Quellen inkonsisten ist. (https://nssdc.gsfc.nasa.gov/planetary/factsheet/) 

Funktion info hinzugefügt welche die Infos über einen Planet in einer Textbox wiedergibt.
anz_mode dictonary hinzugefügt und den "monde" Parameter aus der info-Funktion entfernt. (anz_monde anstatt monde um aliase mit monde liste zu vermeiden)
info-Funktion in die planet_update funktion integriert.
Temperatur dictionary hinzugefügt.
Tempearatur zur info-Funktion hinzugefügt.
Umlaufdauer dict hinzugefügt.
Umlaufdauer zur info-Funktion hizugefügt.
Durchmesser dict hinzugefügt.
Durchmesser zur info-Funktion hinzugefügt.
Distanz zur Sonne dict hinzugefügt.
Distanz zur Sonne zur info-Funktion hinzugefügt.


Fehler in der Textbox korrigiert welcher die Masse der Erde (5.97 * 10^24) als 5.96999999999999 * 10^24 darstellte. 
Der Fehler erfolgte aufgrund der Floatarchimetik in Python. (Gelöst mit ChatGPT (Formatierung :.2e))
Masseinheit zur Masse hinzugefügt.

Die Funktion monde_kreieren mit einer Subfunktion monde_append stark vereinfacht. 

Planetenicons mit mehr Pixeln hinzugefügt um den verpixelten Effekt in der Detailansicht zu vermeiden:
Problem: Nicht richtig zentriert (wahrscheinlich aufgrund der grösseren originalen Grösse).
Lösung: Zeichnen Funktion der Klasse Planeten angepasst und Icons in der richtigen grösse (128 anstatt 512 Pixel) hizugefügt. 

quit_check Funktion hinzugefügt welche überprüft, ob das Fenster geschlossen werden soll oder die Detailansicht verlassen werden soll.
Problem: Esc in der Detailansicht funktioniert nicht mehr.
Lösung: Running als globale Variable definiert. 
-> Code stark vereinfacht. 

Esc Icon hinzugefügt.
<a href="https://www.flaticon.com/free-icons/ui" title="ui icons">Ui icons created by UIUX Mall - Flaticon</a>
Esc rect hinzugefügt:
https://www.pygame.org/docs/ref/rect.html