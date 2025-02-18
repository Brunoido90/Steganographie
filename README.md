Dieses Projekt ist eine Python-Anwendung, die Steganographie verwendet, um Text in Bildern zu verstecken und ihn später wieder zu extrahieren. Steganographie ist eine Technik, bei der Informationen in einem Trägermedium (in diesem Fall ein Bild) verborgen werden, ohne dass dies offensichtlich ist. Das Programm verwendet die niedrigstwertigen Bits (LSB) der Pixel, um den Text zu verstecken.

Funktionsweise
Text in Bild verstecken:

Der eingegebene Text wird in eine Binärsequenz umgewandelt.

Jedes Bit der Binärsequenz wird in das niedrigstwertige Bit (LSB) eines Pixels eingebettet.

Das modifizierte Bild wird als neue Datei gespeichert.

Text aus Bild extrahieren:

Die LSBs der Pixel werden ausgelesen, um die Binärsequenz zu rekonstruieren.

Die Binärsequenz wird zurück in Text umgewandelt.

Technische Details
Verwendete Bibliotheken
Tkinter: Für die grafische Benutzeroberfläche (GUI).

PIL (Pillow): Für die Bildverarbeitung.

NumPy: Für die effiziente Manipulation der Pixel.

Wichtige Funktionen
text_to_binary(text):

Wandelt Text in eine Binärsequenz um (jedes Zeichen wird in 8-Bit-ASCII-Code konvertiert).

binary_to_text(binary):

Wandelt eine Binärsequenz zurück in Text.

hide_code():

Versteckt den eingegebenen Text in einem Bild, indem die LSBs der Pixel modifiziert werden.

extract_code():

Extrahiert den versteckten Text aus einem Bild, indem die LSBs der Pixel ausgelesen werden.

Benutzeroberfläche (GUI)
Die GUI besteht aus folgenden Elementen:

"Bild auswählen":

Ermöglicht das Auswählen eines Bildes, in dem der Text versteckt oder extrahiert werden soll.

Textfeld:

Hier kann der Benutzer den Text eingeben, der versteckt werden soll, oder der extrahierte Text wird angezeigt.

"Code einbetten":

Versteckt den eingegebenen Text im ausgewählten Bild und speichert das modifizierte Bild.

"Code extrahieren":

Extrahiert den versteckten Text aus dem ausgewählten Bild und zeigt ihn im Textfeld an.

Verwendung
Text verstecken:

Wählen Sie ein Bild aus.

Geben Sie den Text in das Textfeld ein.

Klicken Sie auf "Code einbetten" und speichern Sie das modifizierte Bild.

Text extrahieren:

Wählen Sie ein Bild aus, das zuvor mit Text versteckt wurde.

Klicken Sie auf "Code extrahieren", um den versteckten Text anzuzeigen.

Beispiel
Eingabe:
Bild: example.png

Text: Hello, World!

Ausgabe:
Modifiziertes Bild: example_stego.png

Extrahierter Text: Hello, World!

Installation
Voraussetzungen:

Python 3.x

Installieren Sie die erforderlichen Bibliotheken:

bash
Copy
pip install pillow numpy
Ausführen des Programms:

Speichern Sie den Code in einer Datei, z. B. stego_app.py.


README.md
markdown
Copy
# Steganographie-App

Eine Python-Anwendung, um Text in Bildern zu verstecken und ihn später wieder zu extrahieren.

## Funktionen
- Text in Bildern verstecken.
- Versteckten Text aus Bildern extrahieren.
- Benutzerfreundliche GUI mit Tkinter.

## Installation
1. Stellen Sie sicher, dass Python 3.x installiert ist.
2. Installieren Sie die erforderlichen Bibliotheken:
   ```bash
   pip install pillow numpy
Klonen Sie das Repository:

bash
Copy
git clone https://github.com/yourusername/steganography-app.git
Führen Sie das Programm aus:

bash
Copy
python stego_app.py
Verwendung
Wählen Sie ein Bild aus.

Geben Sie den Text ein, den Sie verstecken möchten.

Klicken Sie auf "Code einbetten" und speichern Sie das modifizierte Bild.

Um den Text zu extrahieren, wählen Sie das modifizierte Bild aus und klicken Sie auf "Code extrahieren".
