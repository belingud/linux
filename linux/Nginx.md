# Nginx

## 1. nginx可以做什么？

1. 可针对静态资源高速高并发访问及缓存。
2. 可使用反向代理加速，并且可进行数据缓存。
3. 具有简单负载均衡、节点健康检查和容错功能。
4. 支持远程FastCGI服务的缓存加速。
5. 支持FastCGI、Uwsgi、SCGI、Memcached Servers的加速和缓存。
6. 支持SSL、TLS、SNI。
7. 具有模块化的架构：过滤器包括gzip压缩、ranges支持、chunked响应、XSLT、SSI及图像缩放等功能。在SSI过滤器中，一个包含多个SSI的页面，如果经由FastCGI或反向代理处理，可被并行处理。

### 1.1 作为WEB服务的话支持 

1. 支持基于名字、端口及IP的多虚拟主机站点。
2. 支持Keep-alive和pipelined连接。
3. 可进行简单、方便、灵活的配置和管理。
4. 支持修改Nginx配置，并且在代码上线时，可平滑重启，不中断业务访问。
5. 可自定义访问日志格式，临时缓冲写日志操作，快速日志轮询及通过rsyslog处理日志。
6. 可利用信号控制Nginx进程。
7. 支持3xx-5xx HTTP状态码重定向。
8. 支持rewrite模块，支持URI重写及正则表达式匹配。
9. 支持基于客户端IP地址和HTTP基本认证的访问控制。
10. 支持PUT、DELETE、MKCOL、COPY及MOVE等较特殊的HTTP请求方法。
11. 支持FLV流和MP4流技术产品应用。
12. 支持HTTP响应速率限制。
13. 支持同一IP地址的并发连接或请求数限制。
14. 支持邮件服务代理。

### 1.2 应用场景

（1）作为Web服务软件

（2）反向代理或负载均衡服务

（3）前端业务数据缓存服务

```
        location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
        {
            expires      30d;
        }

        location ~ .*\.(js|css)?$
        {
            expires      12h;
        }
              				
```

### 1.3  优点

1. 支持高并发：能支持几万并发连接（特别是静态小文件业务环境）。
2. 资源消耗少：在3万并发连接下，开启10个Nginx线程消耗的内存不到200MB。
3. 可以做HTTP反向代理及加速缓存，即负载均衡功能，内置对RS节点服务器健康检查功能，这相当于专业的Haproxy软件或LVS的功能。
4. 具备Squid等专业缓存软件等的缓存功能。
5. 支持异步网络I/O事件模型epoll（Linux 2.6+）。



## 2. apache的特点

1. Apache 2.2版本非常稳定强大，据官方说，Apache 2.4版本性能更强。
2. Prefork模式取消了进程创建开销，性能很高。
3. 处理动态业务数据时，因关联到后端的引擎和数据库，瓶颈不在Apache上。
4. 高并发时消耗系统资源相对多一些。
5. 基于传统的select模型，高并发能力有限。select 模型 也就是 同步 epoll  异步       
6. 支持扩展库，可通过DSO、apxs方法编译安装额外的插件功能，不需要重新编译Apache。
7. 功能多，更稳定，更安全，插件也多。
8. 市场份额在逐年递减。

### 2.1. 网络模式 

同步网络模式   select  

每个请求的状态始终在维护着 （消耗好多资源）

异步网络模式   epoll  处理服务器端的并发   请求人数越多 服务器肯定吃紧 系统资源也会紧张  I/O效率也会很慢   

不定期将你的请求 筛选出来  直接告诉你    不用挨个select   

epoll  

每个请求  我不再维护你的状态 如果有请求  就找我  找到了 给你服务 找不到拉倒    



## 3. lighttpd的特点

1. 基于异步网络I/O模型，性能、并发都与Nginx相近。
2. 扩展库是SO模式，比Nginx灵活。
3. 目前国内的使用率比较低，安全性没有Apache和Nginx好。
4. 通过插件（mod_secdownload）可实现文件URL地址加密（优点）。
5. 社区不活跃，市场份额较低。



 ## 5. 如何选择web服务器？

1. 静态业务：若是高并发场景，尽量采用Nginx或Lighttpd，二者首选Nginx。
2. 动态业务：理论上采用Nginx和Apache均可，建议选择Nginx，为了避免相同业务的服务软件多样化，增加额外维护成本。动态业务可以由Nginx兼做前端代理，再根据页面元素的类型或目录，转发到后端相应的服务器进行处理。
3. 既有静态业务又有动态业务：采用Nginx。

此外，如果并发不是很大，又对Apache很熟悉，采用Apache也是可以的，Apache 2.4版本也很强大，并发连接数也有所增加。总的来说，在满足需求的前提下，首先选择自己最擅长的软件，若发现了更好的软件，可在掌握新软件之后逐步替换。虽然动态和静态业务都倾向于选择Nginx，但是大前提是自己要熟练掌握Nginx。切记，在工作中不要盲目选择软件，这可能最终会导致自己无法控制局面，从而给企业带来灾难性的损失。

## 6. Ubuntu下nginx安装和虚拟站点配置方式

如果在Ubuntu16.04下使用apt安装nginx，安装完毕后其工作目录设置如下：

- nginx站点配置目录：/etc/nginx/
  - 其中主配置为nginx.conf
  - sites-available子目录存放站点配置文件，其中有一个default文件为虚拟站点的配置模板，自己的虚拟站点可以以此为模板进行配置。
  - sites-enabled子目录存放一个对应站点配置文件的软连接。必须在sites-availabel生成站点的配置文件，然后到sites-enabled添加对应的软连接。
- 默认站点根目录 ：  /var/www/html/
- 日志文件目录：/var/log/nginx/
  - error.log记录站点的错误，如果要查看详细的错误信息，可以打开该文件查看

以www.blog.com站点为例说明多个虚拟站点配置的方法：

~~~
#安装nginx
sudo service apache2 stop  #如果有apache，则停止apache
sudo apt install nginx-full -y

#虚拟站点配置
#1.首先切换目录到sites-available目录
cd /etc/nginx/sites-available

#2.复制虚拟站点配置模板，生成自己虚拟站点的配置文件
sudo cp default www.blog.com.conf  

#3 编辑模板
#---------------------以下为配置内容-------------------
server {
        listen 80; #监听端口

	   #站点的根目录
        root /var/www/html/www.blog.com;

        # Add index.php to the list if you are using PHP
        #网站默认首页打开顺序
        index index.html index.htm; 
        
        #站点名称，可以有多个名称，中间用空格隔开
        server_name www.blog.com blog.com; 
}

#------------------到此结束------------------------------
#这个模板比较简单，如果有复杂的要求，请以此为基础进行改进

#4 保存退出
:wq

#5 切换到sites-enabled目录下，创建软连接
cd ../sites-enabled
sudo ln -s /etc/nginx/sites-available/www.blog.com.con   www.blog.com.conf

#6 重启nginx服务
sudo service nginx restart  (start/stop)
或者
sudo /etc/init.d/nginx restart

#7 切换到站点根目录(根据你自己的设定进行)，我假定站点根目录是/var/www/html
cd /var/www/html
sudo chmod -R 755 www.blog.com
#编辑index.html

<html>
<head>
<meta charset='utf-8'>
<title>疯狂程序员的博客</title>
</head>
<body>

<h1>疯狂的程序员</h1>

</body>
</html>
#保存退出
:wq

#8 切换到windows系统下，编辑C:\Windows\System32\drivers\etc\hosts文件，在末尾增加：
#ip为你虚拟机的ip地址
192.168.48.3  www.blog.com   

#9 在windows系统下浏览器里输入 :  www.blog.com
看看是否是你的页面
~~~
## 7.centos下nginx安装和配置

- 添加源：

  ~~~
  sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
  ~~~

- 安装Nginx

  ~~~
  sudo yum install -y nginx
  ~~~

- 启动Nginx并设置开机自动运行

  ~~~
  sudo systemctl start nginx.service
  sudo systemctl enable nginx.service
  ~~~

- 测试，在浏览器中输入localhost，看缺省网站

##8. 负载均衡

当一台服务器的单位时间内的访问量越大时，服务器压力就越大，大到超过自身承受能力时，服务器就会崩溃。为了避免服务器崩溃，让用户有更好的体验，我们通过负载均衡的方式来分担服务器压力。

| 角色      | ip           | 作用        |
| ------- | ------------ | --------- |
| lvs负载均衡 | 10.11.59.220 | 请求分担      |
| web01   | 10.11.59.155 | 轮询的web服务器 |
| web02   | 10.11.59.154 | 轮询的web服务器 |

- 这三台机子要求都安装了nginx环境，web01和web02结构应该是一样的

### 8.1 负载均衡服务的配置

~~~
   #连接池
   upstream www_server_pools {  #www_server_pools自定义的连接池名称
      server 10.11.59.154;    #连接的服务器，可以ip或者是域名
      server 10.11.59.155;
   }   

  server {
        listen       80;
        server_name  www.caoliu.com;

        location / {
           # root   /data/www;
           # index index.php index.html index.htm;
           
            proxy_pass  http://www_server_pools;#http://连接池名称
            proxy_set_header   Host $host;   #把主机的header头发给轮询的服务器
            proxy_set_header   X-Forward-For  $Remote_addr; #获取真实的ip地址
        }  
  }
~~~

### 8.2 upstream模块

是nginx支持负载均衡的模块，nginx_http_upstream_moudle，它所支持的代理方式：

- proxy_pass
- fast_cgi
- memcache_pass

### 8.3 常用的轮询算法

- rr轮询算法：静态调度算法，按照请求的时间顺序逐一分配到不同的服务器，如果服务器down掉，就不再向其转发请求

- wrr 权重算法，静态调度算法

  ~~~
     upstream www_server_pools {
        server 10.11.59.154 weight=1;  
        server 10.11.59.155 weight=3;#这个服务器得到的转发是上面的3倍
     }
  ~~~

- ip_hash  根据客户端ip哈希的结果确定访问那个服务器。

  ~~~
    upstream www_server_pools {
        server 10.11.59.154;
        server 10.11.59.155;
        ip_hash;
     }
  ~~~

- 第三方的算法

  - fair 按照服务器忙闲，优先将请求给工作量小的服务器
  - url_hash  按照url哈希的结果访问不同服务器
