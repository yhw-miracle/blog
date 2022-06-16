---
layout: post
title: learning_python_模块和包
date: 2019-04-12 21:42:34 +0800
tags: [python, 模块, 包]
categories: [知识总结]
author: 痛点就是起点
published: true
---

> 本文为痛点就是起点原创文章，可以随意转载，但需注明出处。

### 模块和包
* 导入模块的方式

```python
import {模块名}   # 全部导入
from {模块名} import {资源名称}   # 局部导入
# 资源名称包括：类名、函数和全局变量
```

* 局部导入资源访问控制

```python
from {模块名称} import *
```
___
```python
__all__ = ["{资源名称}", "{资源名称}"]

```

* 屏蔽文件的执行代码

```python
if __name__ = "__main__":
	pass
```

* 模块资源运行工作原理：第一次导入资源文件生成`.pyc`缓存文件。 

* 包是项目结构中的目录，用于文件分层管理。