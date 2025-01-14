#!/usr/bin/python3
# coding:UTF-8

# -------------------------------------------------------------------------------------
#         PYTHON3 SCRIPT FILE FOR THE REMOTE ANALYSIS OF COMPUTER NETWORKS
#         BY TERENCE BROADBENT MSc DIGITAL FORENSICS & CYBERCRIME ANALYSIS
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : TREADSTONE                                                             
# Details : Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

print("[*] Initialising, please wait...")

import os
import sys
import os.path

os.system("apt-get install python3-pip -y > log.txt 2>&1")

os.system("pip3 install pyfiglet  >> log.txt 2>&1")
os.system("pip3 install termcolor >> log.txt 2>&1")
os.system("pip3 install shutil    >> log.txt 2>&1")

import time
import shutil
import pyfiglet 
from termcolor import colored

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : TREADSTONE                                                             
# Details : Check running as root.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.geteuid() != 0:
   print("[*] Please run this python3 script as root...")
   exit(1)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : TREADSTONE                                                             
# Details : Display rogue-agent product banner.
# Modified: N/A
# -------------------------------------------------------------------------------------

os.system("clear")

banner = pyfiglet.figlet_format("ROGUE  AGENT")
banner = banner.rstrip("\n")

print(colored(banner,"red", attrs=['bold']))
print(colored("\t\tT R E A D S T O N E  E D I T I O N\n\n", "yellow", attrs=['bold']))

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : TREADSTONE                                                             
# Details : Create program directories.
# Modified: N/A
# -------------------------------------------------------------------------------------

print("[*] Creating directories, please wait...")
dirList = ["LARX", "OUTCOME", "BLACKBRIAR", "TREADSTONE", "ROGUEAGENT"]
for x in range(0, len(dirList)):
   if not os.path.exists(dirList[x]):
      print("	[+] Creating directory " + dirList[x] + "...")
      os.system("mkdir " + dirList[x])      

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : TREADSTONE                                                             
# Details : Install system requirements.
# Modified: N/A
# -------------------------------------------------------------------------------------

print("[*] Installing system requirements I, please wait...")

list1 = ["libemail-outlook-message-perl", "libemail-sender-perl", "default-jdk", "gdb", "ghex", "snmp", "proxychains4", "bloodhound", "sqlite3", "hashcat", "python3-ldap", "gobuster", "crackmapexec", "exiftool", "rlwrap", "xdotool", "sshpass", "seclists", "redis","feroxbuster"]

for x in range(0, len(list1)):
   print("\t[+] Installing " + list1[x] + "...")
   os.system("apt-get install " + list1[x] + " -y >> log.txt 2>&1")   

print("\t[+] Installing krb5...")
os.environ["DEBIAN_FRONTEND"] = "noninteractive"
os.system("apt-get install krb5-user -y >> log.txt 2>&1")
os.environ["DEBIAN_FRONTEND"] = "interactive"

print("[*] Installing system requirements II, please wait...")

list2 = ["2to3", "pwn", "bloodhound", "kerbrute", "smtp-user-enum", "python3-nmap==1.5.1", "simplejson==3.17.5"]

for x in range(0, len(list2)):
   print("\t[+] Installing " + list2[x] + "...")
   os.system("pip3 install " + list2[x] + " >> log.txt 2>&1")   

print("[*] Installing system requirements III, please wait...")

list3 = ["'neo4j-driver==1.7.0' --force-reinstall","'neo4j==1.7.0' --force-reinstall", "aclpwn", "ldap3"]

for x in range(0, len(list3)):
   print("\t[+] Installing " + list3[x] + "...")
   os.system("python3 -m pip install " + list3[x] + " >> log.txt 2>&1")
   
print("\t[+] Installing evil-winrm...")
os.system("gem install evil-winrm >> log.txt 2>&1")

print("\t[+] Installing windapsearch...")
os.system("git clone https://github.com/ropnop/windapsearch.git >> log.txt 2>&1")
os.system("mv windapsearch/windapsearch.py /usr/share/doc/python3-impacket/examples/windapsearch.py >> log.txt 2>&1")
if os.path.exists("windapsearch"):
   shutil.rmtree("windapsearch")   

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : TREADSTONE                                                             
# Details : Activate database and configure proxychains.
# Modified: N/A
# -------------------------------------------------------------------------------------

os.system("mv exploits.py ./TREADSTONE/install_exploits.py")
os.system("mv RA.db ./ROGUEAGENT/RA.db")
os.system("sed -i 's/#quiet_mode/quiet_mode/' /etc/proxychains.conf")
os.system("sed -i 's/proxy_dns/#proxy_dns/' /etc/proxychains.conf")
os.system("updatedb")

print("[*] All done!!...")
#EoF
