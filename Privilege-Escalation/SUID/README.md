# Linux SUID 提权
标签（空格分隔）： linux
- **自动化 SUID 检测脚本** - [suidcheck](https://github.com/nongcloud/oscp-Learn/Privilege-Escalation/SUID/suidcheck.sh)

- 查找 SUID 可执行文件
```
#查找具有root权限的SUID的文件

find / -perm -u=s -type f 2>/dev/null
find / -user root -perm -4000-print2>/dev/null
find / -user root -perm -4000-exec ls -ldb {} \;
```
已知的可用来提权的`linux`可执行文件列表
| 命令   | 命令     | 命令       | 命令      | 命令         | 命令        | 命令    | 命令      |
|--------|----------|------------|-----------|--------------|-------------|---------|-----------|
| [ash](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/ash.md) | [base64](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/base64.md)  |[bash](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/bash.md)  |[busybox](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/busybox.md) |[cat](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/cat.md)  | [chmod](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/chmod.md)  |[chown](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/chown.md)   |[chroot](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/chroot.md)|
|[cp](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/cp-move.md)| [csh](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/csh.md) | [curl](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/curl.md)  |  [cut](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/cut.md)  |[dash](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/dash.md)  | [date](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/date.md)   |[dd](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/dd.md)  |[diff](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/diff.md)  |
|[docker](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/docker.md)   | [env](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/env.md)       |[file](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/file.md)      | [find](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/find.md)    | [grep](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/grep.md)   | [ip](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/ip.md)      |[more](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/less-more.md) | [mv](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/cp-move.md) | 
|[openssl](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/openssl.md)|  [perl](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/python-perl-ruby-lua-etc.md)   | [php](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/php.md)| [python](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/python-perl-ruby-lua-etc.md)  | [rsync](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/rsync.md) | [rvim](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/rvim.md)| [time](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/time-timeout.md) | [timeout](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/time-timeout.md)|
|[vim](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/vim.md) |[其他脚本文件](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/SUID/Details/other-script-file.md)   |

