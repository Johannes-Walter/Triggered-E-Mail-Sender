# Triggered-E-Mail-Sender
## Programm
An einem Raspberry Pi wird ein Knopf angeschlossen, damit per Knopfdruck eine E-Mail mit der Druckdauer erzeugt und abgesendet wird.  
Weiterhin gibt es noch ein tägliches Update, welches über die in den vergangenen 24h und den passierten Drückereien berichtet.

## Aufbau
Zum Betrieb ist ein Rasperry Pi (auf einem Raspberry Pi 3 getestet), eine Internetverbindung, ein Knopf, ein Widerstand und etwas Kabel notwendig.
Nach den Standarteinstellungen sollte der Knopf und der Widerstand zwischen Pin 1 und Pin 10 geschaltet werden, so wie es in [diesem Tutorial](https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/) erklärt wird.
Die Datei "settings.json" bietet ein paar Einstellmöglichkeiten, zum Beispiel eine Änderung des Anschlusspins oder die E-Mail-Daten der Sender- und Empfängeraccounts.
Um das lesen des Knopfes und das Senden der E-Mail beginnt, muss jetzt nur noch "button_counter.py" ausgeführt werden.

Damit das tägliche Update funktioniert, muss ein Cronjob eingerichtet werden, welcher automatisch zu festgelegten Zeiten das Programm "button_counter_daily_update.py" Ausführt.
Ein Tutorial, welches erklärt wie das geht, ist [hier zu finden](https://wiki.ubuntuusers.de/Cron/).