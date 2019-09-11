# Leviathan Write Up
## Level 0
Double checked a few things. Saw that nmap gave back two ports. 22 and 113. Researched that 113 is known to be exploited, given crackers access to list of users. However do not believe this is the problem that is presented here. I see that the main homedirectory forlevel 0 has a .backup directory with a bookmarks.html inside. I double check port 80, but its closed.

Know that the "mission" is to retrieve the password for leviathan1. This box is apparently more common sense than programming, so I just wonder if I can grep the password (I can).

Code:
`cat bookmarks.html | grep password`

Result:
```bash
leviathan0@leviathan:~/.backup$ cat bookmarks.html | grep password
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

Password for level 1: `rioGegei8m`

## Level 1
Had it almost until the very end. When you log in, you are greeted with a setuid executable called *check*. My first thought was to check what's inside with cat. Obviously, there was a lot of binary. Next I checked to see what's inside with `strings`. Had a few potential options like **love** but that wasn't it. Next, I searched online on how else could I see what's happening inside the program. I am not too familiar with *gdb* so wasn't able to get that working.

I found `ltrace` which was a program that records the calls within another program. It is like JS debugger, where it could also hang, when waiting for an input. Essentially this is what came up:
```bash
leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(0x804853b, 1, 0xffffd764, 0x8048610 <unfinished ...>
printf("password: ")                                                              = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: love
)                                             = 108
getchar(1, 0, 0x65766f6c, 0x646f6700)                                             = 111
getchar(1, 0, 0x65766f6c, 0x646f6700)                                             = 118
strcmp("lov", "sex")                                                              = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                              = 29
+++ exited (status 0) +++
```
Random hexadecimals aside, it looks like the program prints an input, and then gets the three first chars of your input. Password is three letters long. Then the `strcmp("lov", "sex")` appears, which compares string, and it looks like its comparing our input with... the password 'sex'. I see.

So I run `./check` again and put the password in. The program returns the password for the next level.

Password for level 2: `ougahZi8Ta`
