Host: bandit.labs.overthewire.org
Port: 2220

========= bandit4 ==========

```bash
for files in /home/bandit4/inhere/*; do strings ; done
```
Key: **koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

========= bandit5 ==========
```
find -size 1033c ! -executable
```
Key: **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

=========== bandit6 ========
find -group bandit6 -user bandit7 -size 33c 2>/dev/null
^^ finds the files that match that then filters out stderr like 'permission denied' 
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
find -group bandit6 -user bandit7 -size 33c 2>/dev/null -exec cat {} +
^^ just automatically prints the answer

========= bandit7 =========
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

========= bandit8 =========
sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

========= bandit9 =========
strings data.txt | grep ===
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

======== bandit10 =========
cat data.txt | base64 -di
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

======== bandit11 =========
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

=========bandit12=========
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

==========bandit13========
ssh -i bandit14key.txt bandit14@bandit.labs.overthewire.org -p 2220
^^ save the private key to a txt file, change the permissions to 600 (only I can read/write) then login
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

========bandit14==========
telnet localhost 30000
^^ enter the password
BfMYroe26WYalil77FoDi9qh59eK5xNr

========bandit15==========
^^ was an openssl challenge. Not completely sure how it works. Normal telnet/nc 
openssl s_client -connect localhost:30001
^^ insert bandit14 password
cluFn7wTiGryunymYOu4RcffSxQluehd

========bandit16==========
^^ first I had to scan the available ports between the range 31000 - 32000
nmap localhost -p31000-32000
^^ two revealed. Connected to one, it just gave back input. Connected to the other and entered bandit15 pass
openssl s_client -connect localhost:31790
^^ got private key.

========bandit17==========
ssh -i banditkey17.txt bandit17@bandit.labs.overthewire.org -p 2220
diff passwords.old passwords.new 
^^ line 42 is different
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

========bandit18==========
^^ ssh command + `cat readme`
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

========bandit19==========
^^ execute the file to cat the password in /etc/bandit_pass
^^ it is an setuid executable, essentially allowing us to be bandit20 when we use the file and a following unix command
^^ although our uid may be bandit19, when using the exec our euid becomes bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j

========bandit20==========
^^ I log into the shell and first split the screens bc two shells are needed
screen -S ^^ then: 'ctrl+a 0` to switch to first scrn then `ctrl+a S` to split then `ctrl+a tab, ctrl+a 1` to add 2nd scrn
nc -l -p 1234 ^^ start listening server on port 1234. Post bandit19 password (first screen)
./suconnect 1234 ^^ will see that password and return msg about password (second screen)
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr ^^ nc returns the new password!

=======bandit21===========
^^ Challenge is related to crons. Checked out /etc/cron.d and looked at the code for cronjob_bandit22
^^ It seems to be a reboot job that runs a script of the same name ./cronjob_bandit22
^^ It changes permission on a file within the /tmp/ folder. I decided to check out cat the /tmp/<code> and got:
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

=======bandit22==========
^^ saw that cronjob_bandit23.sh is a script in /bin/ ran it and it printed that it copied a password file to a tmp file
^^ changed into /bin/ to look at the code. Essentially printing out the password for bandit 22 and pasting it into a tmp file which is just "I am user bandit 22" em-dee-fived. The password that is in those tmp files is just for bandit22.
^^so annoyed I had to look this one up. Looking at the code, `echo I am user $(whoami) | md5sum | cut -d ' ' -f 1` whoami is obvs bandit22. Just change it to bandit23.
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

======bandit23==========
^^ Have to create a script file inside /var/spool due to specific bandit24 cron job that executes then deletes all scripts in there as bandit24. So create a script in there would allow it to be run like cat /etc/bandit_pass/bandit24 which would give us password and save it into tmp file.
^^ also, have to make it an executable script (otherwise wont run duh, with `chmod +x file.sh`
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 
