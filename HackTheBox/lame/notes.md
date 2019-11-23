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
-
