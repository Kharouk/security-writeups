# Bandit Writeup.
*Host: bandit.labs.overthewire.org
Port: 2220*

## bandit4

```bash
for files in /home/bandit4/inhere/*; do strings ; done
```
Key: **koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

## bandit5
```bash
find -size 1033c ! -executable
```
Key: **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

## bandit6
```bash
find -group bandit6 -user bandit7 -size 33c 2>/dev/null
```
Finds the files that match that then filters out stderr like 'permission denied'.

Key: **HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**

Refactor:
```bash
find -group bandit6 -user bandit7 -size 33c 2>/dev/null -exec cat {} +
```
^^ just automatically prints the answer.

## bandit7
Key: **cvX2JJa4CFALtqS87jk27qwqGhBM9plV**

## bandit8
```bash
sort data.txt | uniq -u
```
Key: **UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**

## bandit9
```bash
strings data.txt | grep ===
```
Key: **truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**

## bandit10
```bash
cat data.txt | base64 -di
```

Key: **IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

##  bandit11
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
Key: **5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**

## bandit12
TODO:: Revisit and write up.

Key: **8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL**

## bandit13
```bash
ssh -i bandit14key.txt bandit14@bandit.labs.overthewire.org -p 2220
```
^^ save the private key to a txt file, change the permissions to 600 (only I can read/write) then login.

Key: **4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e**

## bandit14
```bash
telnet localhost 30000
```
^^ enter the password from bandit13

Key: **BfMYroe26WYalil77FoDi9qh59eK5xNr**

## bandit15
Was an openssl challenge. Not completely sure how it works. Normal telnet/nc

TODO:: Redo to further understand ssl.
```bash
openssl s_client -connect localhost:30001
```
^^ insert bandit14 password

Key: **cluFn7wTiGryunymYOu4RcffSxQluehd**

## bandit16
First I had to scan the available ports between the range 31000 - 32000
```bash
nmap localhost -p31000-32000
```
^^ two revealed. Connected to one, it just gave back input. Connected to the other and entered the password from bandit 15.
```bash
openssl s_client -connect localhost:31790
```
^^ got a private key for next level.

## bandit17
```bash
ssh -i banditkey17.txt bandit17@bandit.labs.overthewire.org -p 2220
```
```bash
diff passwords.old passwords.new
```
^^ line 42 is different.

Key: **kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd**

## bandit18
SSH into the login then run `cat readme`.
Easy.

Key: **IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x**

## bandit19
Execute the file to cat the password in /etc/bandit_pass

It is an setuid executable, essentially allowing us to be bandit20 when we use the file and a following unix command.

Although our uid may be bandit19, when using the exec our euid becomes bandit20, which allows us to see the password for bandit20.

Key: **GbKksEFF4yrVs6il55v6gwY5aVje5f0j**

## bandit20
I log into the shell and first split the screens because two shells are needed in this level.
```bash
screen -S
```
Then: `ctrl+a 0` to switch to the first screen; then `ctrl+a S` to split then, `ctrl+a tab, ctrl+a 1` to add 2nd screen.
```bash
nc -l -p 1234
```
^^ start listening server on port 1234. Post bandit19 password on the first screen.
```bash
./suconnect 1234
```
 ^^ will see that password and return msg about password (second screen)

Key: **gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr**

^^ nc returns the new password!

## bandit21
Challenge is related to crons. Checked out `/etc/cron.d` and looked at the code for `./cronjob_bandit22`. It seems to be a reboot job that runs a script of the same name `cronjob_bandit22.sh`

The script changes permission on a file within the /tmp/ folder. I decided to check out cat the /tmp/\<code> and got:

Key: **Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI**

## bandit22
Saw that `cronjob_bandit23.sh` is a script in /bin/ ran it and it printed that it copied a password file to a tmp file.

Changed into /bin/ to look at the code. Essentially printing out the password for bandit 22 and pasting it into a tmp file which is just *"I am user bandit 22"* em-dee-fived. The password that is in those tmp files is just for bandit22.

So annoyed I had to look this one up. Looking at the code, `echo I am user $(whoami) | md5sum | cut -d ' ' -f 1` **whoami** is obviously bandit22.

Just changed it to bandit23.

Key: **jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n**

## bandit23

Have to create a script file inside `/var/spool` due to specific bandit24 cron job that executes and then deletes all scripts in there as bandit24. So create a script in there would allow it to be run like `cat /etc/bandit_pass/bandit24 > /tmp/\<random_string>` which would give us the password and save it into tmp file.

Also, have to make it an executable script (otherwise wont run duh, with `chmod +x file.sh`

Key: **UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ**
