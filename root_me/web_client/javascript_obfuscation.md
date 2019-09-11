# Javascript - Obfuscation 1
*10 points*

Visiting this [page](http://challenge01.root-me.org/web-client/ch4/ch4.html), another alert appears. I didn't know the password so I just submitted a random string. I failed, and then I begin the hunt for the password. No external js files here, so I inspect the source. There we see the script that checks for the password.

```html
<script type="text/javascript">
    pass = '%63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64';
    h = window.prompt('Entrez le mot de passe / Enter password');
    if(h == unescape(pass)) {
        alert('Password accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou an validate the challenge using this pass.');
    } else {
        alert('Mauvais mot de passe / wrong password');
    }
</script>
```

The variable `pass` seems to be an encrypted string; the `h` variable is our input that has been stored. There is an if block, that checks to see if our input matches with the encrypted string. However, the function `unescape()` is present here, which is seemingly reverting escaped characters within `pass`.

A quick google search reveals that [unescape()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/unescape) returns us a new string where hexadecimal escape sequences are replaced with the chracter that it represents. It is also deprecated, so it's best not to use this function.

Inside Chrome's console, I run:
```js
const pass = '%63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64';
unescape(pass);
```

A string is returned to me. I receive an alert telling me that the string is the correct password, and I can use it to validate the challenge.

#### Flag:
`cpasbiendurpassword`