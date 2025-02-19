## softwares

```sh
sudo apt install arp-scan bash-completion bleachbit cargo cryptsetup dnsutils elinks fdupes gedit git-all gparted hardinfo htop iotop luckybackup lsof make meld ncdu net-tools p7zip-full samba ssh testdisk vim vlc whois
```

## Crisis tools

```sh
sudo apt install procps util-linux sysstat iproute2 numactl tcpdump nicstat ethtool linux-tools-common linux-tools-$(uname -r) bpfcc-tools bpftrace trace-cmd
```

## samba

```sh
[partages]
comment = partages
path = "/media/pi/cle57"
writeable = yes
guest ok = yes
create mask = 0644
directory mask = 0755
force user = pi

sudo /etc/init.d/samba start
sudo /etc/init.d/samba restart
sudo /etc/init.d/samba stop

```

## linux

Public directory (c) in private directory (b)

```sh
mkdir a/b/c
chmod 711 a/b
sudo chown root a/b
touch a/b/c/this.txt
```

## auto start vncserver

install tightvncserver on server (e.g. raspberry) and gvncviewer on client

create file /home/pi/.config/autostart/tightvnc.desktop

```
#!/bin/sh
[Desktop Entry]
Type=Application
Name=tightvncserver
Exec=vncserver :1
StartupNotify=false
```

Start command is :

```bash
vncserver -geometry 1600x900 :1 (connexions on port 1)
```

command to connect:

```bash
"vncviewer <adresseipOuHost>:1 &"
```

or

```bash
"gvncviewer <adresseipOuHost>:1 &"
#no username!!!
```

if does not work:

```bash
sudo apt purge tightvncserver
sudo apt install tightvncserver
sudo apt purge tightvnc-java
sudo apt install tightvnc-java
```

also try for auto start :

```
sudo apt install x11vnc
```

## scan IP addresses on network

```bash
# install arp-scan
sudo arp-scan -l (for  --localnet)

# or:
nmap -T4 -sP 192.168.1.0-254
# T4: profile agressive
# -sP: scan ports
# 0-254: all addresses
```

## configuration keyboard raspberry

```bash
sudo dpkg-reconfigure keyboard-configuration

sudo vim /etc/default/keyboard
XKBLAYOUT=gb
XKBLAYOUT=fr
```

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

# bits zeros: if=/dev/zero
# random: if=/dev/urandom
```

## simple http server

```bash
python -m SimpleHTTPServer 9988
```

<http://adresseip:9988/>

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

```bash
sudo systemctl enable gitlab-runsvdir.service
sudo systemctl disable gitlab-runsvdir.service
```

## wifi auto reconnection raspberry

script to execute in /etc/rc.local (at each start)

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

rsync source destination/ != rsync source/ destination/  
(creation of source in destination) != (copy of content from source into destination)

rsync source destination/ = rsync source/ destination/source/  
rsync source destination/ = rsync source destination (slash in destination has no influence)

## umask memo

/etc/profile sets 022, removing write perms to group + others.
Set a more restrictive umask: i.e. no exec perms for others:
umask 027
Paranoid: neither group nor others have any perms:
umask 077

## rsync options

-a (not used), equivalent to: -rlptgoD (no -H,-A,-X : hard links, ACLs (implies -p), extended attributes)
preserves permissions (owners, groups), times, symbolic links, and devices

-l, --links copy symlinks as symlinks

-L, --copy-links transform symlink into referent file/dir

-p -o -g permissions, owner, group

-E preserve executability

-t preserve modification times

## info about a command

bash: type
csh : which

type cat -> /bin/cat
type echo -> builtin shell

## commands execution

c1 ; c2 -> c1 then c2

c1 && c2 -> c2 if no error in c1

c1 || c2 -> c2 if error in c1

start command at time & date :

at 13:14 9/23/18 command ctrl+D

list jobs:

atq

## sticky bit - SUID/GUID

sticky bit:

chmod 1777 directory or chmod o+t directory

1: allow users to delete only files they own

SUID/GUID:

rights allowing to execute a command with command's rights and not with user's rights. the command is usually
a system tool:

/usr/bin/passwd : \_rwsr_xr_x -> bob can take roots' rights to execute the command

chmod 4777 command or chmod u+s command

chmod 2777 command or chmod g+s command

## various linux shell sys admin

? replaces 1 character -> ls guide_unix.??x

inode : unique file number on the partition

simple quote ' ' : avoids characters expansion: '$USER' -> $USER

double quote " " : allows $ to keep its meaning "$USER" -> mat

possible to mount a disk at IP address?

/ipadress/path/to/disk/......

/ipadresstodisk/.........


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

## regex to find a string _without_ a substring in it

```sh
^mynameistata((?!toto).)*$

# matches:
# mynameistatatititutu
# but not:
# mynameistatatitototu
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

```bash
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

```bash
grep -E ",'[0-9]{4}-[0-9]{2}-[0-9]{2}'," my_file   # -E : extended regex

grep -P ",'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'," my_file    # -P : Perl regex

# timestamps
sed -ri "s/'((0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/[12][0-9]{3} [012][0-9]:[0-5][0-9]:[0-5][0-9])'/to_timestamp\('\1','DD\/MM\/YYYY HH24:MI:SS'\)/g" my_file
```

## regex greedy pattern

```bash
# from https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions

eeeAiiZuuuuAoooZeeee

A.*Z yields 1 match: AiiZuuuuAoooZ (see on rubular.com)
A.*?Z yields 2 matches: AiiZ and AoooZ

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

## Create user & add it to sudo group & delete old one

```bash
sudo adduser mat
sudo usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi mat
sudo deluser -remove-home pi
```

## Backup SD card raspberry remotely

(from <https://www.it-react.com/index.php/2020/02/02/backup-your-raspberry-pi-remotely/> & <https://www.thedigitalpictureframe.com/guide-back-up-sd-card-raspberry-pi-while-running/>)

```
ssh mat@rasp "sudo dd if=/dev/mmcblk0 bs=1M status=progress | gzip -" | dd of=~/$(date +%Y%m%d\_%H%M%S)\_pi_backup.gz
#  gzip - : With no FILE, or when FILE is -, read standard input.
```

Modify visudo tu run dd command :

```bash
sudo visudo

# add this line
ALL = NOPASSWD: /usr/bin/dd
```

## Restore SD card (not remotely of course)

```bash
gunzip -dc pi_backup.gz | sudo dd of=/dev/mmcblk0 bs=1M
#  -c, --stdout      write on standard output, keep original files unchanged
#  -d, --decompress  decompress
```

## Connect automatically rasp to wifi

```bash
vi /boot/wpa_supplicant.conf

# add
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=FR

network={
        scan_ssid=1
        ssid="ssid"
        psk="password"
        key_mgmt=WPA-PSK
}
```

## List open ports

```bash
sudo netstat -ltup
sudo netstat -tulpn | grep LISTEN
sudo lsof -i -P -n | grep LISTEN
sudo ss -tulpn | grep LISTEN
sudo nmap -sTU -O localhost

sudo lsof -i:22 ## see a specific port such as 22 ##
```

## Get all pages & files of website

```bash
wget -r -l0 my_website

# -r : recursion
# -l0 : infinite recursion depth

```

## fail2ban - yunohost

```bash
service fail2ban restart
watch fail2ban-client status yunohost
watch fail2ban-client status sshd
fail2ban-client status
tail -f /var/log/nginx/website-access.log
tail -f /var/log/nginx/access.log
vi /etc/fail2ban/jail.d/defaults-debian.conf
vi /etc/fail2ban/jail.d/yunohost-jails.conf
```

```sh
[yunohost]
enabled  = true
port     = http,https
protocol = tcp
filter   = yunohost
logpath  = /var/log/nginx/*error.log
           /var/log/nginx/*access.log
maxretry = 3
bantime = 3600
findtime = 300
```

```bash
# unban ip
fail2ban-client set yunohost unbanip 192.168.1.254

# follow logs
tail -f /var/log/fail2ban.log
```

## list files in dir -> to html

from:
<https://stackoverflow.com/questions/3785055/how-can-i-create-a-simple-index-html-file-which-lists-all-files-directories>

```sh
# Generate an HTML directory index one level deep:
tree -H '.' -L 1 --noreport --charset utf-8 -o index.html

# Only include specific file types that match a glob pattern, e.g. *.zip files:
tree -H '.' -L 1 --noreport --charset utf-8 -P "*.zip" -o index.html

```

## compare distant and local file

<https://unix.stackexchange.com/questions/144476/run-a-diff-between-local-and-remote-files>

```sh
ssh user@remote_host "cat remote_file.txt" | diff - local_file.txt
```


## recalbox ssh connect without password

```sh
cd /recalbox/share/system/.ssh/
vi authorized_keys
```

##

##

##
