# Optimum HackTheBox Writeup

- Started with a nmap to scan the ports. Used `-A -T4` flags, which revealed that HTTP port is running (web server), and that the box is a Microsoft Server (91%)
- Port 80 is exposing the box's `HttpFileServer` version 2.3. Going onto it there is a login asking for credentials. Few basic admin/password combinations didn't work.
- Searched for HTTPFILESERVER exploit and found one for that version. Ran the exploit on msfconsole and was able to get shell access. 
- Checking `getuid` I am someone named Kostas. Not root. Their desktop had a user.txt file with a key. **User Owned.**

