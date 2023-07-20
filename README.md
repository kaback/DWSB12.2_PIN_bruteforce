# DWSB12.2_PIN_bruteforce
Die PIN eines Zweirichtungszählers vom Typ DWSB12.2 bruteforcen (klappt mglw. auch mit anderen Zählern)

### Man braucht 
* einen Raspi
* eine LED an GPIO17, die man mit Klebeband vor der optischen Schnittstelle des Zählers befestigt.
* eine USB Webcam, mit der man das Verhalten des Zählers direkt nach der Eingabe einer PIN beobachtet 

### Wie findet man damit die PIN?
* Das Script lässt die LED blinken und gibt damit eine PIN in den Zähler ein.
* Das Script macht das für alle PINs zwischen 0000 und 9999. Im Handbuch des Zählers steht, dass die PIN beliebig oft falsch eingegeben werden kann.
* Nach der Eingabe einer PIN wird ein Foto des Zählers gemacht, welches als Dateiname die PIN bekommt, also z.B. 0007.jpg
* Man beobachtet jetzt regelmäßig den Zähler, der nach erfolgreicher Eingabe einer PIN eine andere Anzeige hat.
* Bemerkt man, dass sich die Anzeige verändert hat (dass z.B. jetzt zusätzlich die Leistung angezeigt wird) schaut man auf den Fotos nach, ab welchem Bild das der Fall war. Die PIN liest man direkt im Namen des Fotos ab.
* Ein kompletter Durchlauf von 0000 bis 9999 dauert knappe 2,5 Tage, aber häufig wird die PIN schon früher gefunden, weil sie ja sicher nicht 9999 ist...

### Warum?
Mein Netzbetreiber hat es auch nach 3 Monaten nicht geschafft, mir die PIN mitzuteilen. Mit der oben dargelegten Methode hatte ich meine PIN nach 18 Stunden.

### Versuchsaufbau
Man sieht den Zähler mit der angetüdelten LED und dem Raspi, der mittels seines Netzteilkabels an der Tür einer Unterverteilung verankert wurde. Beobachtet wird der Zähler von einer USB Webcam, die mit Malerkrepp an einem schräg vor dem Zähler aufgestellten Brett befestigt wurde.

![Versuchsaufbau](https://github.com/kaback/DWSB12.2_PIN_bruteforce/blob/main/DWSB.jpg?raw=true)
