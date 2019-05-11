* 网络管理  
* 进程管理  
* 计划任务    
* 打包压缩解压缩  
* 软件安装  
* 环境安装   


## centos 安装图形界面 

```
yum -y groupinstall Desktop 
yum -y groupinstall "Chinese-support" 
init 5 

命令界面 切换到 图形界面  ctrl+alt+F7  反之就是 Ctrl+alt+F1~F6
```


### 根据内容查找  

```
sudo find ./ -name "*.py" | xargs grep kangbazi   

xargs命令  用来给其它命令 传递参数 


taoge@taoge-virtual-machine:~$ echo '11226688' | xargs echo  默认 xargs 是以空白进行切割 
11226688
taoge@taoge-virtual-machine:~$ echo '11&22&66&88' | xargs -d '&' echo 
11 22 66 88
```



## 网络管理  

1. ifconfig 

```
ens33     Link encap:以太网  硬件地址 00:0c:29:39:b2:e9  
          inet 地址:10.0.127.214  广播:10.0.127.255  掩码:255.255.255.0
          inet6 地址: fe80::a6ab:1bd8:f4fc:f3a9/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:301627 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:120228 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:29948113 (29.9 MB)  发送字节:12625775 (12.6 MB)
          
    inet 地址 ：ip地址  
     inet6 ipv6地址  
     Link 连通 状态
     UP  网卡开启  
     BROADCAST 发送广播包
     RUNNING  连上 
     MULTICAST 支持组播
     mask:子网掩码 
  
  
  ifconfig 网卡名 up   
  ifconfig 网卡名 down 
  
  
  service networking restart  
  /etc/init.d/networking restart 
  只要是 /etc/init.d 里边有的服务名 就可以用service 来启动  
```

### ping

```
ping www.baidu.com   ctrl+c 终止 
ping -c 10 www.qfedu.com 指定ping10次 
-b 测试与网关的连通性   
```



### tracert   windows系统

```
tracert www.so.com  #查看你的电脑到达so.com  经过了哪些ip  也就是  下一跳   
```



### 常见的协议  

```
TCP/IP协议   传输控制协议/网间协议    
	http https socket ftp ssh  都是基于tcp/ip协议
UDP协议  用户报文协议  
```





### netstat 查看网络连接状况

```
-n 端口号
-t tcp协议 表示 你通过tcp协议过来的  比如 http  
-u udp 协议
-p 显示进程 
-a 所有  

sudo netstat -nt 显示所有的 TCP连接   
sudo netstat -nu 显示所有的udp连接 
sudo netstat -ntpa 显示所有TCP端口号以及进程号   
```



## ps 进程管理  相当于 windows ctrl+shift+esc 任务管理器

> process status  当前系统的进程状态  我们 可以用 kill 杀死  也可以killall  

```
ps  
   -e 显示所有的进程 ps -e | more 20 每页显示20个  
   -u 指定用户的进程 例子: ps -u root | more -10 每页显示10个 
   -x 一般结合a 来使用   ps -ax 显示完整的信息   a在这里表示所有的进程   
   -r 正在运行的进程 								   S可中断的休眠状态 R 就绪  T暂停
   用户名		进程号 cpu占用率  虚拟内存  RSS(常驻内存) 进程的状态 进程开始时间     命令 
   root       1103  0.0  0.3  65512  3832  ?        Ss   08:48   0:00 /usr/sbin/sshd -D
   root       2545  0.0  0.4  94928  4520  ?        Ss   08:49   0:00 sshd: taoge [priv]
   						 内存占用率		进程的控制终端？ 表示非终端（远程进入）
   						 0：00表示进程已经执行了的时间 
   						 
   kill 2  进程号  #杀死指定的进程 
   kill -9 2 进程号  #强制杀死  
   killall -TERM 进程的名字   
   killall -TERM mysql #杀死所有关于mysql 的进程  
   
   
   ps -aux | grep sshd  #重点  使用它可以查看 ssh 服务是否启动了  或者说正在内存中的程序有没有sshd
```



## top  Linux经典的性能分析工具   能够看到 资源的占用情况 

> 类似于windows 的任务管理器

```
top 
	  当前时间 	系统运行时间	登录用户数   系统的负载   系统的平均负载 任务队列的平均长度 1 5 15 
top - 19:36:23 up  1:30,  2 users,  load average: 0.00, 0.01, 0.05 1核 这个值不能超过1 值越大		  																 系统压力压力越大
		进程总数	 正在运行的	  睡眠的			停止的		   僵尸进程
Tasks:  79 total,   1 running,  78 sleeping,   0 stopped,   0 zombie

Cpu(s):  0.0%us,  0.0%sy,  0.0%ni,100.0%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
		总共内存	       用了			  空闲			内核缓存的内存
Mem:   1004136k total,   188052k used,   816084k free,    15496k buffers
	   交换空间  总共2G		                              空间交换区总量
Swap:  2097148k total,        0k used,  2097148k free,    43656k cached


PID 进程号  
PR 优先级  
USER 进程所有者的用户名 



sudo apt-get -y install htop 

top  
```



##　磁盘管理　

> 先分区 再格式化再 挂载  
>
> 第一块硬盘  sda  第二块 sdb 第三块 sdc 
>
> windows 文件系统类型  NTFS  FAT32 
>
> Linux文件系统类型  Ext4 

* df
* du
* fdisk





### df 查看磁盘的使用情况

```
df 
	-h 最佳阅读体验阅读
	-k 以k为单位
	-m 以M为单位
```

### du 查看文件或者目录空间的使用情况 

```
du -a  显示目录的大小 （包含子目录和其中的文件的大小） 
   -s 只显示目录的大小 不显示子目录和文件
   -c 显示目录 及子目录及文件  并统计总的大小 
   -h 以最佳阅读体验阅读 这里显示每个文件占用了多大的空间 
   
du -s -h ~ #只查看家目录的大小 
```

### fdisk 分区工具 先创建主分区 再创建扩展分区 

```
fdisk -l #列出所有的磁盘 并且 查看分区情况   
fdisk -h #查看帮助文件 
	  -n 新建一个分区
	  -d 删除一个分区 
	  -w 保存 
	  -q 退出  

fdisk -l   #第二块硬盘是/dev/sdb  

对空的硬盘进行分区  
fdisk /dev/sdb  
	  m 查看帮助
      n 新建一个分区
	  d 删除一个分区 
	  w 保存 
	  q 退出 

分区:
n -> p(主分区)->选择分区号(1)->选择扇区号（会有提示 2048）->+8G ->w 保存 （如果不保存直接退出即可）
fdisk /dev/sdb   #删除分区 
      -d  选择分区号（1到4之间）->w   

fdisk -l #可以看到已经分好的一个区 这个时候还不能用  接下来要格式化  以 /dev/sdb1 为例子 
格式化:
sudo mke2fs -t ext4 /dev/sdb1 #对分好的区进行格式化  -t 代表指定文件系统类型  这个时候还不能用 接下来要进行挂载 

挂载: mount 

sudo mkdir -p /python1903 #创建一个新的目录 或者 用已经存在的目录 
sudo mount -t ext4 /dev/sdb1 /python1903/ #临时挂载  
这个时候 df -h  #可以看到  /dev/sdb 说明可以用了 
取消挂载:
umount /python1903 

永久挂载  
sudo vim /etc/fstab										  
/dev/sdb1       /python1903     ext4    defaults        0 0
新的分区		 挂载到哪里		 文件系统类型  默认选项 	   是否备份 0 不备份1备份  是否开机检查磁盘 0 不检查 1 检查  

mount -a 表示 让挂载 立即生效  
```



##  其它   了解 尽量熟练应用  

1.uname    Ubuntu

```
uname -r  显示内核版本号  

uname -a  系统的详细信息  
uname -v 操作系统的版本 
```

2.hostname

```
hostname 查看主机名显示主机名字

sudo hostname 新名字  
sudo vim /etc/hostname #永久设置主机名
```

3. who  显示当前登录的用户 

```
taoge    + tty7  终端         2019-04-18 13:57 03:43        1939 (:0)
taoge    + pts/4        2019-04-18 15:03   .         20925 (10.0.127.220)
	      ssh 
```

4. w  查看登录的用户 并且查看他们的一些行为  

```
 23:45:13 up  5:39,  2 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1     -                18:07    4:10m  0.13s  0.13s -bash
root     pts/0    10.0.127.220     18:07    0.00s  0.54s  0.27s w   #这个用户做了什么操作  
```

5.last 

```
last -10 显示最近登录的信息 并且只显示10条   
```

6.查看内存  

```
free -h 查看内存的使用情况 
```



## Linux 启动  

* 电源键  
* bios加电自检  
* 读取引导分区 
* 加载linux 内核  
* 加载init进程  完成系统的初始化  init 6重启 init 0关机   centos 里边 init 5 （从命令行切换到图形界面）



* 设置启动级别  vi /etc/init/rc-sysinit.conf

  ​			env DEFAULT_RUNLEVEL=2

  

* 启动内核  
* 执行不同级别的脚本程序  
* vim /etc/init.d/rc.local  读取里边的内容 看哪些需要开机自动启动  
* 用户登录  



### date 查看当前时间 

### cal 当月日历 

###　cal 2019 全年日历  





## 计划任务    超级重点 

> 周期性的去执行    
>
> 有两种方式 
>
> 1.配置文件
>
> 2.命令  

1.配置文件   vim /etc/crontab  

```
# m    h   dom   mon dow    user  command
分     时   日    月  周      用户   命令
0-59 0-23 1-31 1-12 0-6 

 例子: 20 16 18 4 4 taoge echo '去年一滴相思泪,今年放流到嘴边' > /tmp/taoge.txt 
```

2.命令 

```
# m h  dom mon dow   command
分 时 日 月 周    命令  

crontab -e 创建计划任务  
crontab -l 列出所有的计划任务    仅仅是列出 crontab -e创建的计划任务  配置文件并没有列出  
crontab -r 清空所有的计划任务 
crontab -i 删除之前 先确认  


 service cron restart #重启定时任务服务 
 
 
```



3.常用的定时任务 

| 分   | 时         | 日   | 月   | 周   | 命令      | 注释                          |
| ---- | ---------- | ---- | ---- | ---- | --------- | ----------------------------- |
| 0    | 0          | *    | *    | *    | mysqldump | 每天的0点备份数据库           |
| 0    | 2          | *    | *    | 0    | rsync     | 每个星期天的凌晨两点 文件同步 |
| 0    | 0          | 15   | *    | *    | 计算工资  | 每个月的15号0点计算工资       |
| 0    | */2        | *    | *    | *    | ./        | 每2个小时执行一次脚本         |
| 0    | 8,12,18,22 | *    | *    | *    | 打卡      | 每天的8点12点 18点 22点打卡   |
| 0    | 8-23       | *    | *    | 1-5  | study     | 每周1到5 8点到23点在教室学习  |
|      |            |      |      |      |           |                               |
|      |            |      |      |      |           |                               |



##  软件的安装  

windows  zip rar 7zip iso 

Linux  gz bz2 xz  zip 

1.压缩和解压缩     

```
gz    apt-get install  gzip 
	gzip 文件1 文件2 支持批量压缩   源文件不存在了  替换成了 .gz的文件  
	不支持 压缩目录
	gzip -d a.gz b.gz  #源文件 也不存在了  换成 a   b 

	

bz2 apt-get install  bzip2
	bzip2 文件1 文件2 支持批量压缩   源文件不存在了  替换成了 .bz2的文件  
	bzip2 -d 1.txt.bz2 2.jpg.bz2 2.txt.bz2 3.avi.bz2 3.rmvb.bz2 4.avi.bz2 支持批量解压缩  删除源文件  取掉 .bz2 
	不能压缩目录 
	
zip及unzip   

  apt-get install zip unzip
  
  zip 新名字.zip 文件1 文件2  目录1 目录2   #支持压缩文件 以及压缩目录   源文件还存在
  unzip 名字.zip #解压缩  源文件还存在  
  

tar: 
	因为我们的gz bz2 都不支持压缩目录 所以我们使用tar 先打包    
	tar -c  打包  
		-x 解包  
		-v 显示处理的进度  
		-f 指定文件名     
		-z 压缩成 gz 格式
		-j 压缩成 bz2 格式
		-J 压缩成xz 格式的   
		
   打包例子: 
   tar -cvf 新名字.tar 文件1 文件2 文件n  目录1 目录n
   解包
   tar -xvf xiaogege.tar
   
   -----------------------以上并没有压缩-------------------
   
```



2.打包压缩机解包并解压缩  

```

   gz的压缩与解压缩  
   打包并压缩
   tar -zcvf gege.tar.gz 111.txt 5.flv 6.jpg 7.txt taotao/
   解包并解压缩  
    tar -zxvf gege.tar.gz 
   
   bz2的压缩与解压缩 
   
    tar -jcvf gege.tar.bz2 111.txt 5.flv 6.jpg 7.txt taotao/
    tar -jxvf gege.tar.bz2
   
   xz的压缩与解压缩  
  	tar -Jcvf gege.tar.xz 111.txt 5.flv 6.jpg 7.txt taotao/
    tar -Jxvf gege.tar.xz
```





### 软件安装  

* apt-get       自动去下载依赖包  自动安装  
  * apt-get -y  install   包名
  * apt-get -y  remove  包名
  * apt-get -y  update 获取新的软件包列表
  * apt-get -y  upgrade 更新可以更新的软件 
  * apt-get source 包名  获取包的源码  
* dpkg 安装   debian package 安装  下载deb 的软件 比如搜狗 输入法  类似于 windows .exe  
  * 优点 下载下来这个包 直接安装即可 
  * 缺点 有依赖  严格地安装顺序   比如安装2 必须先安装1     
* 源码编译安装 
  * 优点 很符合机器 的习惯  
  * 缺点:编译安装 很麻烦   

- 修改源

```
cp /etc/apt/source.list /etc/apt/source.list.bak
vim /etc/apt/source.list
```

