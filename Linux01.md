## 操作系统  

### 分类  

windows   Linux unix andriod ios  Symbian blackberry 

#### 桌面操作系统   docs 

windows  macos  Ubuntu 中标麒麟 原来是红旗  

#### 移动端

andriod ios  Symbian blackberry  windows phone 

### 服务器 

window server 2012 

centos Ubuntu server redhat（RHEL） mac os server  



**以上三类 根据内核来区分  **

> 内核是操作系统的核心 决定了 进程在内存种停留的时间  

* windows 
* Linux内核 
  * redhat  阵营 RHEL centos （社区版Linux）
  * debian 阵营 Ubuntu debian fedora 
* unix 内核  
  * macos 
* GUI 图形界面    graphic user interface
  * gnome 
  * KDE  



### 32位操作系统和 64位的区别  Linux windows 

> 内存的寻址空间   64位支持更大的内存  如果32位 只能使用其中的4G 其余的是浪费的  
>
> 32位支持 2的32次方-1 约等于4G  
>
> 64位 支持2的64次方-1 很大  



## Linux 历史    

* 最先是 unix  最开始 因为一场太空旅行的游戏   贝尔实验室参与研发  纯c开发 后来用于大学科研、军工  
* 芬兰 赫尔辛基 大学  linus  林纳斯   买了一个ibm笔记本  自己写了一个操作系统   这时候linux内核已经写完了  
* linux = linus+unix  企鹅 
* 林纳斯 的伟大在于将Linux开源   
  * 国家才能由自己的操作系统  如果政府自己写操作系统  起码30-50年才能到应用水平  数据库清一色的 sqlserver 而没有现在mysql orcale   就不会有 python php ruby程序员  
  * 免费  我们的嵌入式 才能 更好的发展  
  * 因为开源  社区活跃  集合了全世界优秀的程序员  一起完善Linux 
  * git （代码版本管理工具  团队协作开发必备 ）两周 写完了  用c写     最优秀代码版本管理工具 没有之一 
    * 没有网络 也能进行团队协作 
    * 除了git之外 还有svn 版本管理工具  必须有网络才可以

### Linux的优势  

* Linux 内核纯C编写  底层使用汇编语言 能够扎干计算机每一条指令  速度快 资源利用率高  
* 安全性高  蠕虫病毒 中毒的全是windows  
* 应用领域广  嵌入式 移动手机 服务器  都在使用   
* 可以长时间不用关机 
* 消耗资源少  没有图形界面 内存128M足矣跑起来  
* 多用户多任务  



### Linux安装  

### 虚拟化   CPU 要支持虚拟化

```
 vmvare、virtualbox pd13 这些都是软件 
 
 bios f2 F12 delete esc  开机看到画面立马按 搜索你的电脑型号 如何进入bios  开启虚拟化 
```

### docker容器 也是虚拟化的一种 

> 在虚拟机里安装虚拟机 




### 分区总结:

linux一切从根出发  

/boot  逻辑分区  200M 启动系统的 核心目录   

swap 交换分区  逻辑分区   内存很贵 把硬盘中最快的部分 拿出来 当内存使用  内存的2倍  

/home 普通用户的家目录   逻辑分区

/ 根目录 主分区



## 网络 桥接和nat的区别  

桥接 :   虚拟机和我们物理机一样 都是从 交换机获取ip地址  

比如 物理机的ip地址网段是 10.0.127  那么 虚拟机 也是10.0.127 网段的  

net  ： 表示 虚拟机从 物理机上获取ip地址  物理机在这里充当了 路由器的功能  

物理机的网段是  10.0.127  那么虚拟机就可能是  192.168.1  

```
192.168   
172.16  
10.0  这些网段  给局域网预留的

127.0.0.1  表示本机自己 
```



## 常用的端口号  

* http 80 
* https 443 
* ftp 21
* ssh 22 
* 远程桌面 3389 
* smtp 邮件发送服务器 25 
* pop3 110 
* mysql 3306 



## 常用操作  

sudo passwd root  激活我们的root 用户 

sudo su root  切换到root 用户 

ifconfig  查看我们的ip地址  

从root 切换到 你的用户 su taoge 

sudo apt-get install openssh-server       安装 ssh服务    y 同意的意思  

service ssh start 

ctrl+alt+f1~f6 从图形界面切换到命令行    

ctrl+alt+f7 从命令行切换到图形界面  

lsb_release -a  #查看系统的版本

sudo halt  重启系统  

sudo poweroff

sudo shutdown 关机

sudo shutdown -h  17:00  定时关机  

sudo shutdown -c 取消定时关机  

pwd 查看 当前位于哪个目录下   

~ 就是该用户的家目录  

cd ~  切换到 当前用户的家目录  



### 快照和克隆  



#### 快照: 

​	记录虚拟机某时间点的状态  如果8:00 系统宕机  但是我们保存了 6:00 的状态 这个时候可以切换回6:00的状态  

克隆: 

​	复制一模一样的虚拟机 

## sudo  

安装操作系统的过程中 创建了一个用户 这个用户 他是介于 普通用户到root用户之间   权限比普通用户大但是 比管理员权限小    

安装服务或者其它的时候 需要提升权限   这个时候我们在前面要加上 sudo    

centos 我们是不需要的   



## 安装软件 

```
   Ubuntu 安装软件:   
    sudo apt-get install  软件名    安装软件 
    sudo apt-get -f install  软件名 修复安装  
    sudo apt-get remove 软件名   卸载软件 
    sudo apt-get update  获取新的软件包列表   哪些包可以更新 
    sudo apt-get upgrade 升级所有可更新的安装包  
    sudo apt-get clean 清理没用的安装包  
     sudo apt-get autoclean  
	
	
	sudo apt-get update
    sudo apt-get install man gcc  make  lsof ssh openssl tree vim dnsutils iputils-ping 
    sudo apt-get install net-tools psmisc sysstat curl telnet traceroute wget libbz2-dev libpcre3 
    sudo apt-get install libpcre3-dev  libreadline-dev libsqlite3-dev libssl-dev llvm 
    sudo apt-get install zlib1g-dev git mysql-server mysql-client zip  p7zip
```
