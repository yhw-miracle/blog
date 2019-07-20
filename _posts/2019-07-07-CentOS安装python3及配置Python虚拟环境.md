---
layout: post
title: CentOs安装python3及配置Python虚拟环境
date: 2019-07-07 10:48:16 +0800
tags: [CentOS, Python3, virtualenv]
categories: 问题解决
author: yhw-miracle
---

> 本文为`yhw-miracle`原创文章，可以随意转载，但需注明出处。

本篇文章介绍`CentOS7`系统源码编译安装`Python3.6.9`，并配置虚拟环境，其他系统和`Python`版本可以类似参考。

- 源码安装`python3.6.9`

1. 下载`Python 3.6.9`源码包；

```bash
$ wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
```

2. 解压`Python-3.6.9.tgz`；

```bash
$ tar zxvf Python-3.6.9.tgz
```

3. 准备编译环境；

```bash
$ yum groupinstall 'Development Tools'
$ yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel
```

4. 解压完，进入文件夹，编译安装，该过程耗时较长，大约耗时`20`到`30`分钟，可以泡杯茶等待；

```bash
$ cd Python-3.6.9/
$ ./configure --prefix=/usr/local/python3 --enable-optimizations # 据说 --enable-optimizations 配置项用于提高 Python 安装后的性能，但是会导致安装慢
$ make
$ make install
```

![success](/images/2019/Jul/39.png)

5. 创建`python3`和`pip3`命令；

```bash
$ ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
$ ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

6. 更新`pip3`；

```bash
$ pip3 install --upgrade pip
```

- 配置虚拟环境

**Q**: 为啥要配置虚拟环境，直接用`Python`解析器也可以开发呀？
**A**: 虚拟环境的作用可以配置多个开发环境，并且彼此不受影响，避免依赖包之间的冲突；另外，虚拟环境也便于管理开发环境，可以随意创建开发环境，方便开发。

1. 安装`virtualenv`和`virtualenvwrapper`包；

```bash
$ pip3 install virtualenv
$ pip3 install virtualenvwrapper
```

2. 配置`virtualenv`环境变量；

```bash
$ vi /root/.basrc
export WORKON_HOME=~/.virtualenvs #指定virtualenvwrapper环境的目录
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 #指定virtualenvwrapper通过哪个python版本来创建虚拟环境
$ source /usr/local/bin/virtualenvwrapper.sh
```

3. 创建`virtualenv`命令；

```bash
$ ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
```

4. 创建虚拟环境；

```bash
$ mkvirtualenv demo -p python3
```

5. 查看虚拟环境；

```bash
$ workon
```

6. 进入虚拟环境；

```bash
$ workon demo
```

7. 退出虚拟环境；

```bash
$ deactivate
```

___

- 文内资源
	- [python3.6.9 源码包](https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
)

- 参考资源
	- [CentOS 系统安装 Python3](https://mp.weixin.qq.com/s/h5eb1nVZCdY6BrsD0hnQnA)
	- [Centos7 安装配置 python3 虚拟环境 virtualenvwrapper](https://www.jianshu.com/p/562ce3c2f3b8)
	- [Pipenv & 虚拟环境](https://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)
