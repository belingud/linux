# Linux 第二天  markdown  

## 回顾  

```shell

按下电源键 
bios加电自检 
引导grub分区
加载内核 
初始化系统
启动   

找回root 或者你创建系统之初用户的密码  

1.重启系统
2.出来画面 快速esc 
3.选择高级选项  回车  
4.选择 recover mode  这一行  选中 按下 e 进入一个编辑页
5.找到 ro recover nomodest 这一行 然后删除 recover nomodest 替换成 （在结尾）加上 
  quite splash rw init=/bin/bash 
6.ctrl+x 
7.passwd 用户名 
8重启 


centos 登录以后 
vi /etc/sysconfig/network-scripts/ifcfg-eth0 
英文状态 i 
ONBOOT=no 将no 改为yes  
esc   

shit+：
wq！
service network restart 

如果写错了 esc  shift+:  q!  强制退出 这个时候是不保存的  


破解 centos 密码  
重启 看到画面 立马esc  
e  
第二项 再按下 e 
quite 加上 空格 1  
回车
b 回车  
passwd root 
新密码 
重启即可  
```

```shell
ping www.baidu.com  测试网络是否通畅  
ifconfig  
```

/

##  taoge@taoge-virtual-machine:~$  什么意思

```shell
taoge 当前用户名
taoge-virtual-machine 当前的主机名
如果管理员用户登陆了  ~ 就等同于 /root
~  当前用户的家目录   ~ 等同于 /home/taoge 每次新建一个用户  都会在 home下面 有一个 以用户名为命名的目录   就好比是 windows 重点的 C:\Users\你的用户名 
$ 表示普通用户正在输入  
# 表示管理员用户正在输入  
cd 后面什么都不写 会进入当前用户的家目录  
```



## Linux 查看帮助文件   重点  

```shell
命令 --help  
比如: 
ls --help 

2.sudo apt-get install man
man 命令  
比如 man ls 
```





## Linux 目录结构  Linux 严格区分大小写  

> linux 下面 一切皆文件   因为访问 硬件设备 跟访问文件是一样的  也是需要切换到目录 然后再打开 



> 挂载  u盘是不能直接访问的   我们可以看 电脑中的文件  可以将u盘插到电脑到 就可以看到u盘内容 这个过程就叫做挂载  弹出U盘 叫做取消挂载  

```shell
audo apt-get install tree  

tree --help #查看帮助  

.
├── bin # 存放用户常用的命令 比如ls pwd ping				     重点  
├── boot #系统启动的核心文件都在这个目录下  
├── cdrom #光驱
├── dev #devices 设备    存放设备包括硬盘 键鼠 
├── etc #系统的配置文件全部在这里   							 重点  
├── home #普通用户的家目录 									    重点
├── lib #系统的链接库 类似于C:\Windows\System32 .dll 程序都依赖于这些库文件  不要动  了解
├── lib64 # 64位操作系统的链接库 
├── lost+found #系统异常重启或者关机 内存的相关数据会保存在这里   了解
├── media # 插上U盘或者移动设备 会自动挂载到这里 
├── mnt # mount（挂载的意思） Linux（ext4）想挂载windows（ntfs）的目录 不同的文件系统类型 一般挂载到这里    重点         
├── opt    #orcle  hadoop等第三方高大上 装X的软件 安装到这里   了解
├── proc  # 系统的进程信息  状态信息都在这里    了解
├── root # 管理员用户的家目录
├── run  # 进程的相关信息  保存在这里  后期配置服务的时候 会用到这个  mysql redis 进程信息一般存这里
├── sbin # 存放管理员才可以使用的命令  
├── snap #系统的快照信息 了解 
├── srv  #系统服务信息 service    了解
├── sys #系统相关的信息  system 的意思  了解 
├── tmp # 临时目录  所有的用户都有读写权限
├── usr # 我们安装的软件都安装在这个目录下    类似于windows  C:\Program Files 重点  
	-bin 应用程序 比如qq pycharm他们的执行文件
	-sbin #超级管理员才可以执行的文件 
	-local#管理员安装的应用程序目录  /usr/local  #超级重点 
├── var  # 存放越来越大的文件 比如日志				#重点 
└── vmlinuz -> boot/vmlinuz-4.15.0-29-generic #快捷方式 

```

`bin` `sbin` `home` `etc` `root` `mnt` `usr` `var` 重点



## 常见的快捷键 

| 快捷键       | 作用                 | 备注     |
| ------------ | -------------------- | -------- |
| ctrl+c       | 立即终止             | 强制终止 |
| ctrl+a       | 回来当前命令行的开头 |          |
| ctrl+e       | 回到当前命令行的结尾 |          |
| ctrl+u       | 清空这个命令行       |          |
| clear/ctrl+l | 清空整个屏幕         |          |
| tab          | 补全                 |          |

## 常见的错误  

```shell
1.命令写错了  
2.命令出现了多余空格
3.如果你没有安装对应的软件  而你使用了 就会提示命令没有安装 比如 vi /ets/hosts
```



## 常用命令 

### ls

```shell
ls -a  列出所有的包括.开头的隐藏文件
   -l  详细的列表 
   -A  除了隐藏文件之外（. .. ）开头的 目录及文件
   --color 不同的颜色显示目录 文件 及链接 
   -i  显示的是文件的 节点号  
   
ls -al 经常使用  等同于 ll 
```



```shell
1      2      3  4    5     6     7           8
d rwxr-xr-x   2 root root  4096 4月  15 12:56 snap
d rwxr-xr-x   2 root root  4096 7月  31  2018 srv
d r-xr-xr-x  13 root root     0 4月  16 11:39 sys
- rw-r--r--   1 root root     0 4月  16 11:40 taoge.txt
d rwxrwxrwt  14 root root  4096 4月  16 11:37 tmp
d rwxr-xr-x  11 root root  4096 7月  31  2018 usr
d rwxr-xr-x  14 root root  4096 7月  31  2018 var
l rwxrwxrwx   1 root root    30 4月  15 12:08 vmlinuz -> boot/vml

1： d - l   d 代表目录   - 代表文件  l 链接 （快捷方式）
2:  rwxr-xr-x 权限  r read读  w write 写 x execute 执行 
3.  文件的inode 节点  
4.  文件所属的用户 
5.  文件所属的组 
6. 文件的大小 字节为单位 
7. 文件上一次的修改时间  不是 创建时间   
8.文件或者目录名
```



```shell
1       2      3
rwx    r-x    r-x   755    
r--    r--    r--   444

1代表 文件目录拥有者的权限  
2代表 所属组的权限  
3代表 其他用户的权限 
- 代表没有权限

100 4  r
010 2  w
001 1  x

rw- r-- r--  644 
```



### 历史命令  

```shell
history  列出带行号的每条命令  
!行号   自动执行第几个历史命令   

上下左右箭头  
上箭头  你的上一条命令  
```

## 软链接  

```shell
ln -s 源文件  快捷方式的名字 
例: ln -s /root r 
lrwxrwxrwx   1 root  root      4 4月  16 14:40 r -> root

```

## 目录管理  os.path.join(os.path.dir(os.path.dir(__filename__),'image')

1.绝对路径和相对路径   cd 

```shell
windows 是盘符 c d e f linux以切从根出发 /
绝对路径就是从/ 到当前的目录 比如 /home/taoge 
相对路径 以当前目录为基准 上级目录或者子目录  
	.代表当前路径    cd . 还是当前目录
	..代表上级目录   cd .. 回到上级目录  cd ../../ 回到上级的上级目录 
	~ 回到当前用户的家目录
	- 源目录  cd /home/taoge 然后 cd /etc   cd - 就回到  /home/taoge 
pwd 显示当前位于哪个目录 	
```

2.创建目录 

```shell
mkdir 目录名 创建目录 
mkdir -p 目录1/目录2/目录3/目录4 
mkdir -p 3/{4，5}/{6，7，8} 

├── 3
│   ├── 4
│   │   ├── 6
│   │   ├── 7
│   │   └── 8
│   └── 5
│       ├── 6
│       ├── 7
│       └── 8

```

3.删除目录 

```shell
rmdir 目录 #目录为空 不能有子目录  
rmdir -p 目录名 #递归删除空目录  目录种有子目录 也不行  
上面需要目录必须为空   

rm -rf 目录或者文件名字  
	r 递归删除
	f 代表强制  
```



## 文件操作  

1.文件的创建  touch

```shell
sudo touch 1.txt 2.txt 3.rmvb 4.avi 5.flv #批量创建空文件如果文件存在  那么自动忽略  
vi 得记得保存   
echo '错过我过了这个村，我在下一个村等你’ > 6.txt #如果有 6.txt 覆盖其中的内容 没有创建6.txt 并写入 
echo '错过我过了这个村，我在下一个村等你’ >> 6.txt # 没有6.txt 先创建  并把内容追加文件的末尾 
```

2.文件的移动   mv  move

```shell
在当前目录下 移动文件   
mv 源文件  目标文件 #比如 mv 1.txt 11.txt #那么1.txt就不存在了 换成了 11.txt 其实相当于重命名 
mv 源文件  新目录/  #将文件移动到新目录下 文件名还是原来的 
mv 源文件  新目录/新名称  #将文件移动到新目录的过程中 同时名字也进行了修改 
mv ../taotao.txt ./tao.txt  #将上一级目录的文件 移动到当前目录下 并且改名 
```

3.文件的拷贝 cp 

```shell
cp tao.txt  tao.txt.backup #备份一个文件 修改服务器上面的文件 一定要记住备份  
cp -r 源目录  目标目录  比如 cp -r taotao tao  #目录中会多一个 tao的目录 
```

4.文件的删除 rm 

```shell
sudo rm 文件名 删除 文件 
rm -i 文件名 #在删除之前 先让用户确认一下 
rm -f 文件名 #强制删除 不提示   
rm -rf 目录 
rm -rf * #删除当前目录下面的所有文件  
rm -rf 3/a* 删除目录3 下面以a开头的所有   
```

5.文件的查看

```shell
cat  文件名 查看文件内容 
vi 文件名   # :q！ 强制退出
tac 文件名 #倒序显示文本行  
head -n 2 1.txt #只查看文本的前两行  
tail -n 2 1.txt #只是查看文本的后两行 

tail -f cat 1.txt #实时查看文本最后面的内容  
watch -d -n 秒数 cat 文件名  #实时显示文件的内容 高亮   ctrl+c 退出

more 文件名    分页显示文件内容   空格 翻页  回车 换行   q退出  
less 文件名  g 回到开头  G到结尾   空格 向后翻页 b 向前翻页      
stat 文件名 查看文件的详细信息   

atime 最近访问时间  
mtime 最近修改时间 
ctime 修改状态时间 


```

6.文件的查找   find   

```shell
find 路径  参数 文件名  
		
	-name 是按照文件名查找
	-iname 也是按照文件名查找 但是这个不区分大小写 
	-mtime 按照修改时间
	-user 所属用户  
	-size [+/- c/k/M/G] + 大于 - 小于
	-perm 权限值 
	-ls 以列表的形式  
	-maxdepth #最大的深度  

find / -name "2.txt“ #查找根目录下 名为 2.txt 的文件  
find . -name "taoge.txt" #在当前目录下面查找  
find /tmp/ -name "2.txt" #指定的目录查找 
find -mtime -3 #查找3天以内的  
find -mtime +3 #查找3天以上的 
find / -maxdepth 1 -mtime -1 -ls #查找目录级别为1 修改时间为1天以内的 并以列表展示 
find /tmp/ -size 11c #查找 /tmp目录下面大小为11字节的  
find /tmp/ -size +10c -size -125c -name "*.txt" #查找 tmp目录下面 大于10字节 小于125字节后缀为.txt的所有文件 
find / -maxdepth 1 -user taoge #查找根目录下 深度为1 所属用户为taoge的 所有  
find / -perm 644 -maxdepth 1 -ls #查找跟目录下面 权限为644 的 深度为1 并且列表展示  
 
```



## 文件的权限  

```shell
r 读 4 
w 写 2
x 执行 1 execute 
- 没有权限 
rwxrw-r--  拥有着可读可写可执行 所属组 可读可写不可执行  其他用户 只读 
764 
666 
经常遇到的  777 755 644 600  

#符号表示  
u 所属的用户 
g 所属的组 
o 其他人 
a all 
+ 增加
- 去除权限   


-rw-r--r--   1 root  root      0 4月  16 11:40 taoge.txt 原来
chmod g+w  taoge.txt 
-rw-rw-r--   1 root  root      0 4月  16 11:40 taoge.txt 修改后 
chmod g-w  taoge.txt 
-rw-r--r--   1 root  root      0 4月  16 11:40 taoge.txt 减w后 
chmod a+x taoge.txt  所属用户 所属组其他用户 全部加上执行的权限 
chmod a=rwx taoge.txt 所有的用户全部变成了 可读可写可执行  
chmod o=r taoge.txt 其它用户只读   

chmod a+x taoge.txt  给文件增加执行的权限    重点  



chmod 755 文件或者目录名字 #更改为所属用户可读可写可执行 所属组可读可执行 其它用户可读可执行   
chmod 777 目录名  #只是修改该目录名 子目录及子子目录它们还是原来的权限  
chmod -R 777 目录名 #改目录及下面所有的子目录及所有文件  通通修改为 777权限   
```



### 修改文件的拥有者   chown  

```shell
chown 用户名:组名 文件或者目录  更改文件或者目录的拥有者 
chown -R 用户名:组名 文件或者目录 递归修改文件或者目录的拥有者  
```



## pycharm 增加快捷方式  

```shell
/home/taoge/桌面/pycharm-2018.2.2/bin/pycharm.png 
/home/taoge/桌面/pycharm-2018.2.2/bin/pycharm.sh

vi /usr/share/applications/pycharm.desktop    

i 进入编辑模式  
粘贴下面的  :

[Desktop Entry]
Name=Pycharm
Type=Application
GenericName=Pycharm3
Comment=Pycharm3:The Python IDE 
Icon=/home/taoge/桌面/pycharm-2018.2.2/bin/pycharm.png
Exec="/home/taoge/桌面/pycharm-2018.2.2/bin/pycharm.sh" %f
Terminal=pycharm
Categories=pycharm;


esc  
：wq!

chmod +x /usr/share/applications/pycharm.desktop  
cp /usr/share/applications/pycharm.desktop /home/taoge/桌面/ 
双击就可以运行了 
```



