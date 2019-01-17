#!/bin/sh
python3 /home/pi/bluetooth-scan/scan.py
sshpass -p "Aokakes0316" scp -r reserchers aokakes@aokakes.sakura.ne.jp:/home/aokakes/www/w318
