# simple-HTTPS-server.py

There are times when we need to spin up HTTPS server for file sharing and hosting exploits instead of `simpleHTTPserver`.

### Create a self-signed certificate

```bash
openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
```

You will now have a `server.pem` in your directory.

### Examples:

Make sure to put the path of `server.pem` in the script. Or you can put them in the same directory.

`home/user/www $> python3 simple-HTTPS-server.py`

You can also create a new directory for hosting purpose. In that case:

`home/user/www/web $> python3 ../simple-HTTPS-server.py`