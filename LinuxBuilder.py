#!/usr/bin/python
import os

#array for any tools that need to be installed
kaliTools = ["dmitry", "dnmap", "dnsenum", "dnsmap", "dnsrecon", "dnstracer", "dnswalk", "dotdotpwn", "enum4linux", "exploitdb", "fierce", "firewalk", "masscan", "nmap", "recon-ng", "smtp-user-enum", "urlcrazy", "wol-e", "hping3", "cisco-auditing-tool", "cisco-global-exploiter", "cisco-ocs", "cisco-torch", "copy-router-config", "hexorbase", "aircrack-ng", "asleap", "bluelog", "blueranger", "bluesnarfer", "pixiewps", "reaver", "bbqsql", "blindelephant", "burpsuite", "dirb", "dirbuster", "wfuzz", "wpscan", "zaproxy", "responder", "wireshark", "cryptcat", "cymothoa", "dbd", "dns2tcp",  "httptunnel", "casefile", "cutycapt", "dos2unix", "dradis", "keepnote",  "metagoofil", "nipper-ng", "pipal", "armitage", "jboss-autopwn", "linux-exploit-suggester", "shellnoob", "beef-xss", "binwalk", "p0f", "pdf-parser", "dhcpig", "cewl", "john", "johnny", "wordlists", "radare2"]

#turns the array into a string where the terms are separated by a space
str = " ".join(kaliTools)
os.system("apt install %s" % str)



username = os.environ.get('USER')

scriptDirectory = os.path.exists("/home/%s/scripts" % username)
linenumDirectory =  os.path.exists("/home/%s/scripts/linenum" % username)
pspyDirectory = os.path.exists("/home/%s/scripts/pspy" % username)
seclistDirectory = os.path.exists("/opt/seclists")

if scriptDirectory == False:
    os.system("mkdir /home/%s/scripts/" % username)
if linenumDirectory == False:
    os.system("git clone https://github.com/rebootuser/LinEnum ~/scripts/linenum")
if pspyDirectory == False:
    os.system("git clone https://github.com/DominicBreuker/pspy ~/scripts/pspy")
if seclistDirectory == False:
    os.system("git clone https://github.com/danielmiessler/SecLists /opt/seclists")

os.system("chmod 755 /home/%s/cripts/ -R" % username)
