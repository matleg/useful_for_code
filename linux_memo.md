
## softwares

arp-scan \
bleachbit \
cryptsetup \
fdupes \
gedit \
git-all \
gparted \
hardinfo \
htop \
luckybackup \
meld \
ncdu \
p7zip-full \
samba \
ssh \
vim \
vlc \
whois 

## samba

[partages]
comment = partages
path = "/media/pi/cle57"
writeable = yes
guest ok = yes
create mask = 0644
directory mask = 0755
force user = pi

sudo /etc/init.d/samba start,restart,stop




## linux

Public directory (c)  in private directory (b)

mkdir a/b/c
chmod 711 a/b
sudo chown root a/b
touch a/b/c/this.txt




## auto start vncserver


install tightvncserver on server (e.g. raspberry) and gvncviewer on client
create file /home/pi/.config/autostart/tightvnc.desktop
#!/bin/sh
[Desktop Entry]
Type=Application
Name=tightvncserver
Exec=vncserver :1
StartupNotify=false

starting command is : vncserver -geometry 1600x900 :1 (connexions on port 1)

command to connect:
"vncviewer <adresseipOuHost>:1 &"
or
"gvncviewer <adresseipOuHost>:1 &"
no username!!!

if does not work: sudo apt-get purge xxxxxxx; sudo apt-get install xxxxxxx
xxxxxxx=tightvncserver
        tightvnc-java
        
also try to install x11vnc for auto start





## scan IP addresses on network

install arp-scan
sudo arp-scan -l (for  --localnet)

or:
nmap -T4 -sP 192.168.1.0-254 (T4: profile agressive, -sP: scan ports
0-254: all addresses)




## fix IP addresses on network

add in file /ect/hosts of client and server
the adresses, example :
192.168.1.1	    rpi1
192.168.1.2	    rpi2
192.168.1.3 	main_pc
192.168.1.4     osmc



## configuration keyboard raspberry

sudo dpkg-reconfigure keyboard-configuration

sudo vim /etc/default/keyboard
XKBLAYOUT=gb
XKBLAYOUT=fr





## dd

to find SD card
```bash
sudo fdisk -l
```

to create SD card
```bash
sudo dd bs=4M if=2017-11-29-raspbian-stretch.img of=/dev/mmcblk0p status=progress conv=fsync
```

(if: input file, of:output file, bs: block size)

to restore
```bash
sudo dd if=~/chemin/vers/le/fichier/de/backup.img of=/dev/mmcblk0  bs=512
```

bits zeros: if=/dev/zero
random: if=/dev/urandom



## simple http server

python -m SimpleHTTPServer 9988
http://adresseip:9988/




## simple git server

install git instaweb
script to execute at each start with, e.g.:
crontab -e
@reboot /home/pi/startup_script.sh

```bash
#!/bin/bash
cd my_git_repo.git
git instaweb --httpd=webrick
cd /home/pi
```




## auto start gitlab CE server

sudo systemctl enable gitlab-runsvdir.service
sudo systemctl disable gitlab-runsvdir.service





## wifi auto reconnection raspberry

script to execute in  /etc/rc.local (at each start)

```bash
#!/bin/bash

while true ; do
        if ifconfig wlan0 | grep -q "inet addr:" ; then
                sleep 300
        else
                ifup --force wlan0
                sleep 20
        fi
done
```

(for example : /home/pi/network_monitor.sh & )





## bash source

./script
-> executes the script. When done, changes made to the environment are discarded.

. script
-> sources the script. As if commands had been typed in directly. Environment changes are kept.

source script
-> sources the script
source and . are synonymous in Bash.




## rsync slashes memo

rsync source destination/                          !=        rsync source/ destination/ 
(creation of source in destination)                !=       (copy of content from source into destination)
  
rsync source destination/     =       rsync source/ destination/source/
rsync source destination/     =       rsync source destination    (slash in destination has no influence)
 




## umask memo

/etc/profile sets 022, removing write perms to group + others.
Set a more restrictive umask: i.e. no exec perms for others:
umask 027
Paranoid: neither group nor others have any perms:
umask 077




## rsync options

-a (not used), equivalent to: -rlptgoD (no -H,-A,-X : hard links, ACLs (implies -p), extended attributes)
preserves permissions (owners, groups), times, symbolic links, and devices

-l, --links                 copy symlinks as symlinks
-L, --copy-links            transform symlink into referent file/dir
-p -o -g permissions, owner, group
-E preserve executability
-t preserve modification times




## info about a command

bash: type
csh : which

type cat  -> /bin/cat
type echo  -> builtin shell



## commands execution

c1 ; c2  -> c1 then c2
c1 && c2  -> c2 if no error in c1
c1 || c2  -> c2 if error in c1

start command at time & date :
at 13:14 9/23/18 command         ctrl+D

list jobs:
atq



## sticky bit - SUID/GUID

sticky bit:
chmod 1777 directory    or    chmod o+t directory
1: allow users to delete only files they own


SUID/GUID:
rights allowing to execute a command with command's rights and not with user's rights. the command is usually
a system tool:
/usr/bin/passwd : _rwsr_xr_x  -> bob can take roots' rights to execute the command

chmod 4777 command   or   chmod u+s command
chmod 2777 command   or   chmod g+s command





## various linux shell sys admin


? replaces 1 character  -> ls guide_unix.??x

inode : unique file number on the partition

simple quote ' ' : avoids characters expansion:  '$USER' -> $USER
double quote " " : allows $ to keep its meaning "$USER" -> mat

possible to mount a disk at IP address?
/ipadress/path/to/disk/......
/ipadresstodisk/.........




## script execution

. /path/to/script.sh                 !=               ./path/to/script.sh
execute in current shell                          opens new shell




## linux VS windows

\r ASCII CR  -> end of line, without jump
\n ASCII LF  -> next line (linux)
\r\n EOL : CRLF  -> windows




## linux /etc/init.d VS /etc/rc.local

use:
/etc/init.d/command OPTION

OPTION can be: start, stop, reload, restart, force-reload

/etc/rc#.d (# is a number for specific initialization level - from 0 to 6)


/etc/rc.local : files run after all other init level scripts have run (e.g. mount, samba, etc.)





## power button raspberry

shorting pins 5 and 6 (GPIO3 and GND) together will wake the Pi up from a halt state

        - create listen-for-shutdown.py:

```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
```
		- sudo mv listen-for-shutdown.py /usr/local/bin/
		- sudo chmod +x /usr/local/bin/listen-for-shutdown.py

		- create listen-for-shutdown.sh:

```bash
#! /bin/sh
case "$1" in
  start)
    /usr/local/bin/listen-for-shutdown.py &
    ;;
  stop)
    pkill -f /usr/local/bin/listen-for-shutdown.py
    ;;
  *)
    echo "Usage: /etc/init.d/listen-for-shutdown.sh {start|stop}"
    exit 1
    ;;
esac
exit 0
```

```bash

sudo mv listen-for-shutdown.sh /etc/init.d/
sudo chmod +x /etc/init.d/listen-for-shutdown.sh
sudo update-rc.d listen-for-shutdown.sh defaults    
#(register the script to run on boot with defaults runlevels)
```


		
## Copy File Permissions to Another File

```bash
chmod --reference=reference_file file

chown --reference=reference_file file
```




## really delete data on disk
(from Korben)

```bash
#!/bin/bash
for n in `seq 7`; do dd if=/dev/urandom of=/dev/diskN ; done
```


## regex capture group


what is between () is captured and can be reused as a variable ($1)

e.g.: search
\$\{([a-zA-Z]+)\}

replace:
"$$$1"

changes all : ${variable} to "$variable" : variable is captured by ([a-zA-Z]+)


with sed:

```bash
sed -irn 's/$my_variable(_toto)/$my_variable_\1/g' my_file 
```

-r regex extended
-n quiet
-i inplace


Example:

```
$ echo "123.456.78" |sed 's/\([0-9]*\)\.\([0-9]*\)\.\([0-9]*\)/\1/'
123
$ echo "123.456.78" |sed 's/\([0-9]*\)\.\([0-9]*\)\.\([0-9]*\)/\2/'
456
$ echo "123.456.78" |sed 's/\([0-9]*\)\.\([0-9]*\)\.\([0-9]*\)/\3/'
78
$ echo "123.456.78" |sed 's/\([0-9]*\)\.\([0-9]*\)\.\([0-9]*\)/\1 : \2 : \3/'
123 : 456 : 78
```


## regex capture date

```
grep -E ",'[0-9]{4}-[0-9]{2}-[0-9]{2}'," my_file   # -E : extended regex

grep -P ",'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'," my_file    # -P : Perl regex

# timestamps
sed -ri "s/'((0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/[12][0-9]{3} [012][0-9]:[0-5][0-9]:[0-5][0-9])'/to_timestamp\('\1','DD\/MM\/YYYY HH24:MI:SS'\)/g" my_file
```



## xargs command examples

```bash
find . -name "*.jpg" -type f -print | xargs tar -cvzf pictures.tar.gz
cat dl_links.txt | xargs wget
echo 'one two three' | xargs mkdir
#ls
#one two three
faster with xargs : 
find ./foo -type f -name "*.txt" -exec rm {} \; 
find ./foo -type f -name "*.txt" | xargs rm
```

use {} with –i to replace arguments:

```bash
ls /etc/*.conf | xargs -i cp {} /home/matleg/confs
```



## 



## 

## 
## 
## 


## 
## 
## 

## 
## 
## 



