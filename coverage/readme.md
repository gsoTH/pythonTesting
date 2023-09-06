# coverage: Tool zur Analyse der Abdeckungsgrade
Mit `coverage` können wir [Abdeckungsgrade](http://kleuker.iui.hs-osnabrueck.de/CSI/Methoden/kombiquUeberdeckung.html) analysieren, also überprüfen, welche Teile unseres Codes aufgerufen werden. Wir berechnen insbesondere die [Anweisungsüberdeckung C0](https://de.wikipedia.org/wiki/Kontrollflussorientierte_Testverfahren#C0._Anweisungs%C3%BCberdeckungstest_(Statement_Coverage)) und die [Zweigüberdeckung C1](https://de.wikipedia.org/wiki/Kontrollflussorientierte_Testverfahren#C1._Zweig%C3%BCberdeckungstest_(Branch_Coverage)).

Im Zusammenspiel mit UnitTests nutzen wir diese Informationen um die [Testabdeckung](https://www.testautomatisierung.org/lexikon/code-coverage/) unseres Codes zu messen.

## Installation
`pip install coverage`


## Aufruf:
- `coverage help` 
> Wenn Sie keine Admin-Rechte besitzen, also z.B. auf Schulrechnern, werden Erweiterungen in Ihr Verzeichnis installiert. In diesem Fall müssen Sie bei Aufruf den Befehl `python -m ` voransetzen. Hier also: `python -m  coverage help` 

- `coverage run <modul>` Führt ein Python-Skrip aus analysiert die Anweisungsabdeckung C0. 
- `coverage run --branch <modul>` Führt ein Python-Skrip aus analysiert die Zweigüberdeckung C1.
- `coverage report` Ergebnis von `run` anzeigen
- `coverage html` Ergebnis von `run` als Webseite inkl. farbigen markierungen des getesteten Codes.


## Testabdeckung ermitteln mit pytest
Anweisungsüberdeckung analysieren, indem wir das Ergebnis von pytest an coverage übergeben:
- ``coverage run -m pytest``

Wir können zusätzlich die Zweigüberdeckung analysieren lassen:
- ``coverage run --branch -m pytest``

Abschließend kann man sich das Ergebnis ansehen mit:
-``coverage report`` oder:
- `coverage html` (empfohlen)
