# simple-HTTPS-server.py

There are times when we need to spin up HTTPS server for file sharing and hosting exploits instead of `simpleHTTPserver`.

### Create a self-signed certificate

```bash
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

You will now have a `server.pem` in your directory.

### Examples:

Make sure to put the path of `server.pem` in the script. Then create a new directory called `web`.

Put the script and server.pem in www directory like:

`/home/user/www/server.pem`

`/home/user/www/simple-HTTPS-server.py`

Then `cd` into `web` directory and run the script:

`home/user/www/web $> python3 ../simple-HTTPS-server.py`

![server](/images/server.png)

![access](/images/access.png)

