# -*- coding: utf-8 -*-
# @Time: 2019/7/22 14:30
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: is_post_file.py
# @Software: PyCharm
import re


def is_post_file(file_name):
    """
    判断是否为文章源文件
    :param file_name: 文件名
    :return: True or False
    """
    result = re.match(r'^\d{4}-\d{2}-\d{2}-.+\.md$', file_name)
    if result is not None:
        return True
    else:
        return False
