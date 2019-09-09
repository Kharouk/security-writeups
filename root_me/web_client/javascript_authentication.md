# Javascript - Authentication
*5 points*

Simple, check-the-files flag. 

Visit this [page](http://challenge01.root-me.org/web-client/ch9/) and you’ll see a login page. Check the page and see what JS files are being imported. Find one titled `login.js`.

Within it, there’s a check to see what user and password is being entered:

```js
function Login(){
	var pseudo=document.login.pseudo.value;
	var username=pseudo.toLowerCase();
	var password=document.login.password.value;
	password=password.toLowerCase();
	if (pseudo=="4dm1n" && password=="sh.org") {
	    alert("Password accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou an validate the challenge using this password.");
	} else { 
	    alert("Mauvais mot de passe / wrong password"); 
	}
}
```

Enter the pseudo code and the password and an alert comes up. The flag is the password.

#### Flag:
`sh.org`

#security writeups/root-me#
