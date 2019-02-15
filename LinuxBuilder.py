#!/usr/bin/python
import os

cmd = os.system("apt-get install -y dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux exploitdb fierce firewalk masscan nmap recon-ng smtp-user-enum urlcrazy wol-e hping3")
cmd = os.system("apt-get install -y cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config hexorbase")
cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer pixiewps reaver")
cmd = os.system("apt-get install -y bbqsql blindelephant burpsuite dirb dirbuster wfuzz wpscan zaproxy")
cmd = os.system("apt-get install -y responder wireshark")
cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp  httptunnel")
cmd = os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote  metagoofil nipper-ng pipal")
cmd = os.system("apt-get install -y armitage jboss-autopwn linux-exploit-suggester shellnoob beef-xss")
cmd = os.system("apt-get install -y binwalk p0f pdf-parser")
cmd = os.system("apt-get install -y dhcpig")
cmd = os.system("apt-get install -y cewl john johnny wordlists")
cmd = os.system("apt-get install -y radare2")
cmd = os.system("mkdir ~/scripts")
cmd = os.system("git clone https://github.com/rebootuser/LinEnum.git ~/scripts/linenum")
cmd = os.system("git clone https://github.com/DominicBreuker/pspy.git ~/scripts/pspy")
cmd = os.system("git clone https://github.com/danielmiessler/SecLists.git /opt/seclists")
