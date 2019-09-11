# Javascript - Obfuscation 2
## *Going down 3 floors...*
*10 points*

Visiting the [page's](http://challenge01.root-me.org/web-client/ch12/ch12.html) challenge reveals a blank page, with no errors in console. so I visit the page source.

I am greeted by a comment message from the creator of the challenge, **Hel0ck,** saying that if we need help to message on the IRC.

Again we see a variable called `pass` and that unescape function. Only this time, there's a bit of unescaping within unescaping.

```js
unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");
```