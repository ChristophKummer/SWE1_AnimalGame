#AnimalGame

##Installation:
im Terminal=>
```bash
pip install dist/animalgame-0.1.0.tar.gz
```

##Programmstart:
im Terminal=>
```bash
python -m AnimalGame
```

##Programmbeschreibung:
AnimalGame ist ein Programm, in dem Einheiten von verschiedenen Figuren erstellt werden können, die mit einander interagieren können. 
Es sind folgende Figuren erstellbar:
	-Player
	-Farm-Animals:
		-Cow
		-Parrot
		-Chicken
	-Wild-Animals:
		-Wolf

Es sind folgende Interaktionen möglich:
	-Player kann jedes Animal füttern
	-Jedes Animal macht Geräusche beim Fressen
	-Die Figuren haben einen Gesundheitsstatus, der verändert werden kann und beim Sinken unter 0 zum Löschen der Figur führt.
	-Ein Wolf kann Animals töten.
	-Ein Wolf kann sterben, wenn keine Animals vorhanden sind, die er fressen kann.


##Tests:
```bash
pytest
```
	Durch Eingabe des Befehls "pytest" im Terminal werden zwei Test durchgeführt.
	1. Überprüfung ob eine Kuh beim Füttern ein Geräusch macht
		-Erstellung einer Kuh und eines Players
		-Player füttert die Kuh
		-Einlesen der Konsolenausgabe und Check ob mit der Testbedingung übereinstimmt
	2. Überprüfung ob das Angreifen des Wolfes auf eine Kuh die Gesundheit schwächt
		-Erstellung einer Kuh und eines Wolfes
		-Überprüfung ob die Gesundheit geschwächt wurde
