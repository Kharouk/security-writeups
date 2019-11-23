# Notes on Legacy - Cyber Mentor Addition

Began with an nmap search that I saved the output to **nmap/legacy.** The command I used was: 

`nmap -A -T4 -p- 10.10.10.4 -oN nmap/legacy`

- Gave us two ports that are open. Also gave us port 3389 which is closed. 
- The two ports that are open are SMB related, because the server is on Windows (apparently XP with 92% guess from nmap)
- On linux 139 port would be for Samba (basically the same).
- These are file share ports. Accesible by users. Common in internal networks, common in Window environment. 
- Most computers have some sort of shared folder structure
- Nmap's 'OS guess' should not be taken to heart.. 


## Script results.
- NETBIOS name means name of computer: **Legacy**.
- We get a MAC address
- `Used with smb-os-discovery` 
    - What operating system: **Windows XP**
    - computer name again
- "If you ever see *message_signing* as disabled, this is dangerous.", or when you see it as enabled but not required. 
    - This is a note on a pen test report, and could lead to shell access.

## Notes
- When dealing with SMB, use `smbclient`.
    - however in this case it did not work when doing `smbclient -F \\\\10.10.10.4\\`
- Instead using metasploit and `msfconsole`
    - then we `search smb_version` -> use the auxilary scanner with `use auxiliary/scanner/smb/smb_version`
        - auxilary is our pre-exploit, all about that scanning, enumeration, and information scanning.
- Legacy really shows us that SMB exploits are common and very vulnerable. 
    - And to get this vulnerability to be of use, we need OS and smb version. 
    - In metasploit, we set the required RHOSTS to the box's ip.
    - 
## Ports
### 139 

### 445
- Ding ding ding. Metasploit found you.
```bash
Host is running Windows XP SP3 (language:English) (name:LEGACY) (workgroup:HTB ) (signatures:optional)
```
- Still not good cause we didn't get an smb version -__o__- But at least we got Windows XP SP3

So after reading up on the rapid7 smb exploit for windows xp sp3, we can use the exploit that metasploit provides. :)
Running the exploit and setting the target to our known OS, and running exploit. I was in. I had shell access. 

This is called **reverse shell** since the victim is connecting back to one of our ports. **bind shell** is when we run malware that opens up a victim's port and lets us connect to them that way. 

Once I was in, i ran `getuid` to see who am I. But I am system, the highest rank.
    - highest privilege level.  
    - Equivelent to root
    - 

