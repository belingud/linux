# Linux基础第三天 

* 硬连接  
* 权限大boss 
* 用户和用户组的操作 
* grep、awk、sort、uniq、wc  
* vi 编辑器   
* 网络、进程管理  
* 计划任务    

## 复习  

```
halt 重启 
init 6 
reboot 重启 
shutdown 关机 
init 0 也是关机  
cd . .. -
mkdir -p  
rm -rf 
touch 
vim 
cat “” > 

head -n 
tail -n 
tail -f 
more 
less

chmod +x  g u o a + - 
chmod -R 

history  
```

## 硬链接    ln  

> 文档分为 节点区 和 内容区   节点区存放我们的 文件名、权限、所属用户 修改时间等  内容区 仅仅是存放内容
>
> 区分一个文件 并不是靠文件名 而是靠 inode 节点    
>
> Linux下面 一切皆文件  
>
> 两个文件同时指向一个inode   节点  

* 硬连接不允许给目录创建 只允许给文件创建   注意权限 如果是在根目录或者 /root 记得 sudo 
* 硬连接其实就是创了一个新文件  跟源文件是独立的  但是它们两个同时指向一个inode节点 区
* 修改源文件的内容  目标文件的内容也会跟着修改 
* 删除一个 新的文件 或者源文件 并不会对  另外一个有影响

```
已经存在一个 文件taoge.txt 
ln taoge.txt taoge6.txt  #taoge6就是新文件   它跟taoge.txt 指向一个inode 节点   

修改taoge.txt 内容  taoge6.txt 也会跟着改变     
删除taoge.txt 并不影响taoge6.txt
```



## 修改所属的组 

```
chmod g+x  
chmod g=rwx 
chmod a-x 
chmod -R 777 

chown -R 用户名:组名  文件或者目录名 
----------------------------------

chgrp 组名  文件或者目录名字 
-R 递归修改
sudo chgrp -R taoge taoge
```



### 权限大boss   chattr 

```
+ 在原来的基础上增加权限 
- 在原来的基础上减去权限 
i 给文件增加或者去除只读属性 （不能修改权限 不能删除 不能修改链接 不能写入 等等）
a 只能追加数据 不能修改或者删除  

sudo chattr +i 文件名（只能是文件名） #保护文件只能读不能删除修改权限 写入  
取消保护 sudo chattr -i 文件名  

sudo chattr +a 文件名   #只能是 echo ‘’ >> (只能两个> 不能一个)追加写入 不能修改权限 不能删除 服务器日志文件经常用到  

sudo chattr -a 文件名 #取消保护
```



## 用户管理 

1. 一个用户必须有一个主组   （要么是管理用户 要么是普通用户 要么是访客 ）
2. 一个用户可以拥有多个附属组
3. 一个组可以拥有多个用户 
4. 该服务器上面的用户信息 存储在  /etc/passwd  下面  组信息 在 /etc/group 中  密码信息 存在于 /etc/shadow 

### 添加用户   useradd   

```

useradd  dongdong 

1		 2  3    4   5  6 				7
dongdong:x:1001:1001: :/home/dongdong:/bin/bash    /sbin/nologin

1 用户名 
2 密码
3 用户uid 
4 所属组的id gid 
5 备注的信息
6 用户的家目录
7 /bin/bash 具备脚本执行的权限 简单来说 就是 可以切换账号登录  /sbin/nologin 不能登录  


-g 添加用户指定添加到哪个组  
useradd -g 组名 新用户名  #组名必须已经存在的   
-u 指定用户的 uid 
useradd -u 666 guang   
useradd yuanyuan  #这个时候yuanyuan的uid 就是667 
-m 自动在home 目录下面创建一个 以用户名为命名的文件夹  默认创建用户 不在home 下面 创建  
-d 自己指定家目录所在的位置  一般结合m一起使用 
举例:sudo useradd -md /tao2 taotao2  
-s /usr/sbin/nologin   #linux中 运行mysql 服务  需要一个mysql 用户身份去运行服务 但是这个用户不能切换登录  
sudo useradd -u 1903 -g taoge -md /dingding -s /usr/sbin/nologin dingding


如果想让这个用户切换登录 那么我们 vi /etc/passwd   将 /usr/sbin/nologin 改为 /bin/bash 
```



### 用户的删除 userdel

```
userdel 用户名  #如果创建了家目录  这么删除只是删除 /etc/passwd中的记录  但是 家目录还没有删除  
userdel -r 用户名 #删除用户名的同时 将家目录一起干掉   

```



### 修改用户的信息   usermod 

```
usermod  
		-g 组id  将用户所属主组修改到指定的 组
		-u uid   修改用户的id 
		-G 		 附属组的名称 
		-a 		 将用户添加到附属组 
		sudo usermod -a -G taoge liangliang  将liangliang添加到 taoge附属组中  
		-d 目录名  修改用户的家目录  
		sudo usermod -d /新目录 用户名
		-l 修改登录名 
		sudo usermod -1 新用户名 指定的用户名
```



### 修改密码  passwd  

```
passwd  #只是写一个passwd 说明修改的是 root 用户  
```



### su 和sudo 

```
su #只写su 说明切换到  root  


sudo  系统安装的时候 创建的用户 它属于sudo组 sudo组比普通用户权限大 比超级管理员权限小  如果操作一个动作 需要root 权限  sudo组里的用户 可以在前面加上 sudo  用来 提升权限  
```

### 其它命令 

```
id   #查看用户的 uid gid 等详细信息  
groups #查看用户属于哪些组  主组 附属组都能看到 

liangliang@taoge-virtual-machine:/home/taoge$ whoami
liangliang
liangliang@taoge-virtual-machine:/home/taoge$ groups 
#当前liangliang 主组是 tao 附属组是 taoge
tao taoge


```



## 组管理 

```
groupadd 组名
groupdel 组名 #删除  如果这个组被用户当作主组来使用 那么不能删除 非得删除 必须得先删除用户 
groupmod -n 新组名 原组名  
```



## 管道符  |  前面的输出 作为后面的输入  

```
cat /etc/passwd | head -n 2  
```



## 日志清洗 命令  非常重要 

### grep 非常类似于我们的正则表达式 

```shell
cat /etc/passwd | grep 'tao'  

-c 显示符合要求的行数 
例:grep -c 'tao' /etc/passwd 
-v 跟-c 相反 打印不符合要求的行  
gerp -v 'tao' /etc/passwd   

-n 打印出行的同时 连同行号一起输出  
grep -nv 'tao' /etc/passwd 

-i 忽略大小写 

grep '^#' test.py 匹配#开头的行
grep ‘[0-9]’ 文件名 #匹配文本中包含数字的行  
grep 'o\{2\}' /etc/passwd #匹配包含2个 o 的  特殊字符要 \ 转义  
```

## wc 

```shell
-l   统计符合要求的有多少行
-c   统计有多少个单词 

cat /etc/passwd | wc -l
```



### awk  流式编辑器 针对文本的行 一行行的去操作 

``` shell
-F 指定分割符  $0 代表所有的列 $7 代表第7列  
cat /etc/passwd | awk -F ":" '{print $1"~"$7}'  
awk /root/ /etc/passwd  #匹配 包含root 的 行 
awk -F ':' '$1 ~/root/' /etc/passwd #第一列是 root 的   
awk -F ':' '$3==0' /etc/passwd #判断第三列值为0 的 
awk -F ':' '$7!="/usr/sbin/nologin"' /etc/passwd # 判断哪些用户是可以登陆 或者具备脚本执行权限
awk -F ':' '$7=="/bin/bash"' /etc/passwd 

awk -F ':' '$3 < $4' /etc/passwd #判断第三列小于第4列的  
awk -F ':' '$3>100 || $7 != "/bin/bash"' /etc/passwd #逻辑或 或者  
awk -F ':' '$3>100 && $7 != "/bin/bash"' /etc/passwd #逻辑与 并且 
awk -F ':' '{(total=total+$3)};END{print total}' /etc/passwd # 对所有行的第三列进行求和 
```



# sort 排序 默认按照首字母进行排序

```shell
cat /etc/passwd | sort  #首字母排序  
-t #指定分隔符  
-k #第几列  
-n #以纯数值进行排序
-r #逆向排序 
cat /etc/passwd | sort -n -t ':' -k 3 #对 /etc/passwd  取出第三列 然后按照数值排序
cat /etc/passwd | sort -n -t ':' -k 3 -r #针对上面的 进行倒序 排列
```





### uniq （unique ）去重  一般是跟sort 命令 一起使用 

```
-c 在每行前面 显示出现的次数  
-d 只输出重复的行  多行只是输出一行 
-D  只输出重复的行  有多少行输出多少行
-i 忽略大小写 

taoge@taoge-virtual-machine:/tmp$ sort fruit.py | uniq -c 
      2 banana
      2 caomei
      1 huanggua
      1 juhuacha
      1 orange
taoge@taoge-virtual-machine:/tmp$ sort fruit.py | uniq -d
banana
caomei
taoge@taoge-virtual-machine:/tmp$ sort fruit.py | uniq -D
banana
banana
caomei
caomei


```



## 面试题 

```
查找你最常使用的10条命令  

 history | awk '{print $2}' | sort |uniq -c | sort -n -k 1 -r | head -n 10
```





## vi vim 编辑器  （txt 文本文档 和 sublime 编辑器的区别）



###   英文状态   shift 切换中英文![编辑器三种模式](C:\Users\neyo\Desktop\新建文件夹\编辑器三种模式.png)编辑模式  

| 键        | 作用                            |
| --------- | ------------------------------- |
| i         | 在光标的当前位置输入            |
| a         | 在光标的下一个位置输入          |
| o         | 在光标的下一行输入              |
| A         | 在光标所在行的行尾输入          |
| S         | 先把所在行的内容删除 然后输入   |
| s         | 先把光标位置的字符删除 然后输入 |
| I 大写的i | 在光标所在行的行首输入          |
| O         | 光标所在行的上一行              |
|           |                                 |



### 命令模式   编辑模式ESC进入 

| 键      | 作用                   |
| ------- | ---------------------- |
| h       | 光标向左移动一个位置   |
| j       | 光标向下移动一个位置   |
| k       | 光标向上移动一个位置   |
| l       | 光标向右移动一个位置   |
| yy      | 复制一行               |
| p       | 粘贴一行               |
| nyy     | 复制n行                |
| np      | 粘贴n行                |
| dd      | 删除一行               |
| ndd     | 删除n行                |
| u       | 撤回上一次的操作       |
| GG      | 快速回到文章的末尾     |
| gg      | 快速回到整篇文章的开头 |
| .       | 重复上一次的操作       |
| shift+6 | 快速回到 行首          |
| shift+4 | 快速回到行尾           |
| （      | 快速回到块首部         |
| ）      | k快速回到块的尾部      |
|         |                        |



### 底部命令模式 shift+: 

| 键                                                 | 作用                                                         |
| -------------------------------------------------- | ------------------------------------------------------------ |
| :w                                                 | 保存 并没有退出                                              |
| :q                                                 | 退出                                                         |
| :wq！                                              | 强制保存并退出                                               |
| :x                                                 | 保存并退出                                                   |
| :set nu                                            | 设置行号                                                     |
| :set nonu                                          | 取消行号                                                     |
| ：23                                               | 快速将光标定位到第23行                                       |
| /字符串                                            | n从上往下找 shift+n 从下往上找                               |
| ?字符串                                            | n 从下往上找 shift+n 从上往下                                |
| :s/要查找的字符串/替换后的字符串/                  | 替换的是所在的行 只能替换一行的一个关键词                    |
| :s/要查找的字符串/替换后的字符串/g                 | 替换一整行所有的关键词                                       |
| :%s/要查找的字符串/替换后的字符串/                 | 全文替换 每一行只是替换一个关键词                            |
| :%s/要查找的字符串/替换后的字符串/g                | 全文所有的关键词全部被修改                                   |
| :numeber1,number2s/要查找的字符串/替换后的字符串/  | number1，number2 表示第几行  只替换从n1 到n2 之间的关键词 但是只是第一个 |
| :numeber1,number2s/要查找的字符串/替换后的字符串/g | number1，number2 表示第几行  只替换从n1 到n2 之间的关键词 替换所有的关键词 |
| :%s/http:\/\/www.baidu.com/http:\/\/www.so.com     | 特殊字符记得转义                                             |

### 网络管理 

```
ifconfig  查看ip地址  
windows 操作系统  ipconfig 

ens33 表示网卡信息 
ens33     Link encap:以太网  硬件地址 00:0c:29:39:b2:e9  
          inet 地址:10.0.127.214  广播:10.0.127.255  掩码:255.255.255.0
          inet6 地址: fe80::a6ab:1bd8:f4fc:f3a9/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  跃点数:1
          接收数据包:65940 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:3283 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:4607858 (4.6 MB)  发送字节:406615 (406.6 KB)

lo        Link encap:本地环回  
          inet 地址:127.0.0.1  掩码:255.0.0.0
          inet6 地址: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  跃点数:1
          接收数据包:216 错误:0 丢弃:0 过载:0 帧数:0
          发送数据包:216 错误:0 丢弃:0 过载:0 载波:0
          碰撞:0 发送队列长度:1000 
          接收字节:15800 (15.8 KB)  发送字节:15800 (15.8 KB)
          
 ifconfig ens33 
 
 ifconfig ens33 up  开启网卡
  ifconfig ens33 down 关闭网卡
```



















































