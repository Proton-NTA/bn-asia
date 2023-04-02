# Bayes-Netz mit pgmpy

Dieses Repository stellt ein Konsolenprogramm zur Berechnung der Verteilung von Variablen in einem Bayes-Netz mit optionaler Evidenz bereit.

## Installation

Für die Installation wird [Conda](https://docs.conda.io/projects/conda/en/stable/) empfohlen um alle Abhängigkeiten über die *environment.yml* direkt zu importieren.
Wie die *environment.yml* Datei für das Erstellen einer Umgebung verwendet wird, ist unter diesem Link zu finden:

[Erstellen einer Umgebung über eine *environment.yml* Datei](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

Anschließend klonen Sie das Repository in die Umgebung oder laden die *main.py* herunter, hier benötigen Sie zur Verwendung des Asia-Netzwerkes noch die *asia.bif*.

Weitere Netzwerke finden Sie [hier](https://www.bnlearn.com/bnrepository/discrete-small.html#asia).

## Verwendung

### Start

Starten Sie das Programm über den Pythonintepreter welcher die vorausgesetzten Module installiert hat.

`[home]/anaconda3/envs/bn-asia/bin/python3 main.py [bif-file]`

Der Parameter `[bif-file]` ist optional, hier kann der Pfad zu einem anderen Netzwerk angegeben werden. Default: `asia.bif`

### Eingaben

#### Variable

Nachdem das Netzwerk eingelesen wurde, werden die Variablen, welche im Netzwerk vorhanden sind, ausgegeben.
Anschließend folgt die Frage, für welche Variablen die Verteilung berechnet werden soll.
Hier kann eine Liste an Variablen in beliebiger Form angegeben werden.
Falls eine Variable eingegeben wird, welche nicht im Netzwerk vorhanden ist, wird man darauf hingewiesen.
*(Die Eingabe wird über einen regulären Ausdruck der Form `(\w+)` nach Variablen durchsucht)*

#### Evidenz

Anschließend wird man nach einer optionalen Evidenz gefragt.
Hier kann eine Liste der Form `[key]=[value]` angegeben werden oder mit `Enter` eine leere Eingabe bestätigt werden.
Das Format der Liste ist bis auf die Verwendung von `=` zur Zuweisung der Werte frei.
*(Die Eingabe wird über einen regulären Ausdruck der Form `(\w+)\s*=\s*(\w+)` nach Werten durchsucht)*

Falls die Eingabe fehlerhaft ist, wird man entsprechend darauf hingewiesen.

### Ergebnis

Zuletzt wird die Verteilung berechnet und als Tabelle auf der Konsole ausgegeben.

# Copyright

Die *asia.bif* wurde von der Webseite [bnlearn.com](https://www.bnlearn.com/bnrepository/discrete-small.html#asia) (© 2023 Marco Scutari) geladen, keine Änderungen vorgenommen.