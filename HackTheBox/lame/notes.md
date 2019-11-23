# Write up for Lame (No walkthrough..)

## 11/23/19:
- taking this in multiple days probs since I want no outside help.
- Started with a classic nmap sweep: `nmap -A -T4 -p- 10.10.10.3 -o nmap/lame`
    - Mixed both the cyber mentor way and the ippsec of saving it. It takes a while though I might find a better solution..
- Normal scan whilst the main one is loading:
    - Found port 21 open (ftp)
    - Found port 22 open (ssh)
    - 139 and 445 open for microsoft (smb)
- Based on the above knowledge and report, I am assuming that we will be trying to get in using an smb exploit that will reveal ssh credentials that we can then ssh into and possible get user/root
- Once the main nmap finished, there was extra info:
    - FTP (21) - vsftpd 2.3.2
    - distccd (3632) - ?
    - Couldn't get exact OS details, something called OpenWrt White Russian 0.9, could also possibly be a printer or a router?
- Based on what I know, I'll try using metasploit for smb\_version
    - Could not be identified (Unix - (Samba 3.0.20-Debian)
    - A quick google search revealed nothing, maybe this isn't a smb exploit. 
- Checking on that detailed FTP report from nmap, I decided to search up the version (vsftpd 2.3.4) in exploit-db.
    - Apparently a backdoor was added in this version of vsftpd..
- Running the exploit on msfconsole... I was able to connect to the FTP port, but it was asking for a password. At this point I think I'm skipping ahead. Maybe I should try to figure out that ssh first?
    - "USER: 331 Please specify the password"
    - Not sure if I can enter the password in the msfconsole. 
- Since this box is very CVE (Common Vulnerabilities Exposure), I knew I'm on the right track with finding vulnerabilities.
- So I've never encountered **distccd** before, and researching it it looks like it's a Daemon. Supports ip based authentication from anyone, so apparently anyone can connect to it. It will distribute C code across several machines on a network.. Runs on port 3632 or through a tunnel command such as ssh (should not be listening for connections)
    - And of course, metasploit does have an exploit. 
    - `use exploit/unix/misc/distcc_exec`
    - Connected! Command shell session 1. 
        - It was a reverse TCP connection. 
        - There was a command that echoed "lBeP2uEArTRJeeTX"
        - Looks like I am inside a shell, landing inside /tmp/ territory
        - I was able to go into /root/ folder, where I found a root.txt file. I tried opening it but I was denied. However, I did realise I was inside the root folder which should've denied me anyways. When checking the hidden files in the directory, I saw the '.ssh/' directory and I knew that maybe I can get the known_hosts and authorized_keys info to maybe be able to ssh in that other open port.

There was also a "vnc.log" that I need to make sense of:
```

New 'X' desktop is lame:0

Starting applications specified in /root/.vnc/xstartup
Log file is /root/.vnc/lame:0.log
```

I then went to explore the other directories; next stop, home. I went into /home/makis and found a user.txt file with a key, did I draw blood?Yep! Owned the user.

- So now I'm trying to crack root user. I did a bit more research on "lame", and found out it was a program used to create compressed audio files.. Not sure if it matters here. But I discovered I couldn't run lame anyways (didn't really have a shell) so I ran `shell` and got my sh going. Still could not run `lame` so I ran /bin/bash. Now I got my terminal in a familiar way: `daemon@lame:/tmp$ `, running lame now says its not installed and I need to ask admin to install it.. 
- Spent the last hour trying to figure out the FTP port. It is using a version that is vulnerable (2.3.4) but I keep trying to break it (using a backdoor, enumerating, etc) and it's just not letting up. Will change up tactics back to the SSH and the SMB ports.
    - Could it be that since the nmap returned saying that it allowed for "anonymous" connection, (Anonymous FTP Login allowed), that we can use anonymous@anonymous?
    - Yep, logged iin! And it was a rabbit hole, nothing inside the FTP server.  
- Next I decided to investigate the SMB and SSH ports. SSH port might be a bit of a waste of time since it usually requires brute force and vulnerabilities might not be very common (unless I write my own).
- Checking on that smb version again, I google and there IS an exploit for it, (Samba 3.0.20-Debian). Metasploit obviously has one called `exploit/multi/samba/usermap_script` -> And I get the shell as root!!! Which is the exact same shell as I received when breaking the DistCC protocol, only I'm given root. That is LAME. 
- So many turns leading nowhere in this one, but it was fun being able to solve this one on my own. First ever box! Will remember it fondly. Good way of practicing whilst studying for my CompTIA's Network+ certificate.
- Found root key in `/root/root.txt`



## Post Box Notes
- Looking online, it seems very few experts used the `distccd` method, which makes me happy knowing I was able to solve user flag through that route! 
- Learning about rabbit holes. the FTP was just a sidetrack aimed to distract. If it's taking too long and you think it should have definitely worked, it's probably a hole.

## SSHing
known\_hosts:
|1|gS7DWzAxRvtufzEYnaW40GOvYu0=|5afWvF6s4R5Yaog0mimuOyNfXiI= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAstqnuFMBOZvO3WTEjP4TUdjgWkIVNdTq6kboEDjteOfc65TlI7sRvQBwqAhQjeeyyIk8T55gMDkOD0akSlSXvLDcmcdYfxeIF0ZSuT+nkRhij7XSSA/Oc5QSk3sJ/SInfb78e3anbRHpmkJcVgETJ5WhKObUNf1AKZW++4Xlc63M4KI5cjvMMIPEVOyR3AKmI78Fo3HJjYucg87JjLeC66I7+dlEYX6zT8i1XYwa/L1vZ3qSJISGVu8kRPikMv/cNSvki4j+qDYyZ2E5497W87+Ed46/8P42LNGoOV8OcX/ro6pAcbEPUdUEfkJrqi2YXbhvwIJ0gFMb6wfe5cnQew==

authorized\_keys:
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApmGJFZNl0ibMNALQx7M6sGGoi4KNmj6PVxpbpG70lShHQqldJkcteZZdPFSbW76IUiPR0Oh+WBV0x1c6iPL/0zUYFHyFKAz1e6/5teoweG1jr2qOffdomVhvXXvSjGaSFwwOYB8R0QxsOWWTQTYSeBa66X6e777GVkHCDLYgZSo8wWr5JXln/Tw7XotowHr8FEGvw2zW1krU3Zo9Bzp0e0ac2U+qUGIzIu/WwgztLZs5/D9IyhtRWocyQPE+kcP+Jz2mt4y1uA73KqoXfdw5oGUkxdFo9f1nu2OwkjOc+Wv8Vw7bwkf+1RgiOMgiJ5cCs4WocyVxsXovcNnbALTp3w== msfadmin@metasploitable


