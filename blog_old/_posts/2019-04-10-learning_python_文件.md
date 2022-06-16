---
layout: post
title: learning_python_文件
date: 2019-04-10 21:40:09 +0800
tags: [python, 文件]
categories: [知识总结]
author: 痛点就是起点
published: true
---

> 本文为痛点就是起点原创文章，可以随意转载，但需注明出处。

### 文件
#### 文件打开和关闭
```python
# 方式一
file = open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
file.close()   # 文件不用后需关闭，否则会造成内存泄漏问题

# 方式二
with open(...) as file:
    pass
```

#### 文件读写模式

| Character | Meaning |
| ------ | ------ |
| 'r' | open for reading (default) |
| 'w'  | open for writing, truncating the file first |
| 'x' | create a new file and open it for writing |
| 'a' | open for writing, appending to the end of the file if it exists |
| 'b' | binary mode |
| 't' | text mode (default) |
| '+' | open a disk file for updating (reading and writing) |
| 'U' | universal newline mode (deprecated) |

* 笔者内化结果：
    * `rb`，读字节，文件不存在报错。
    * `wb`，写字节，每次调用会覆盖原文件，文件不存在会新建。
    * `ab`，追加写字节，写入信息会追加到文件末尾，文件不存在会新建。
    * `rb+`，读、写字节，文件不存在会报错。
    * `wb+`，读、写字节，每次调用会覆盖原文件，文件不存在会新建。
    * `ab+`，读、追加写字节，写入信息会追加到文件末尾，文件不存在会新建。
    * `r`，读字符，文件不存会报错。
    * `w`，写字符，每次调用会覆盖原文件，文件不存在会新建。
    * `a`，追加写字符，写入信息会追加到文件末尾，文件不存在会新建。
    * `r+`，读、 写字符，文件不存在会报错。
    * `w+`，读、写字符，每次调用会覆盖原文件，文件不存在会新建。
    * `a+`，读、追加写字符，写入信息会追加到文件末尾，文件不存在会新建。

#### 读文件

```python
read(self, n: int = -1) # -> AnyStr

readable(self) # -> bool:

readline(self, limit: int = -1) # -> AnyStr:

readlines(self, hint: int = -1) # -> List[AnyStr]
```

#### 写文件

```python
writable(self) # -> bool

write(self, s: AnyStr) # -> int

writelines(self, lines: List[AnyStr]) # -> None
```