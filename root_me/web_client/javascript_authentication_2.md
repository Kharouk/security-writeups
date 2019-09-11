# Javascript - Authentication
*10 points*

Again, a simple, check-the-files flag.

This time there's a bit more javascript to dissect, but nothing too difficult.

Visit the [page](http://challenge01.root-me.org/web-client/ch11/) and you'll be greeted with a login button that sends two alerts; username and password.

I didn't know the answer right away, so I skipped through and got a message saying I'm a "naughty hacker". 😘

I inspected the page, and saw the `login.js` file. Looking at the function `connextion()`, I saw that it was checking the username and password I was inputting against a string within an array. The string, `"GOD:HIDDEN"`, is then split between the `:`. The function checks to see if the username matches with the first part (GOD) and the password matches with the second part (HIDDEN). If so, we get another alert saying we passed, and we can use the password as our key.

Done!

#### Flag:
`HIDDEN`