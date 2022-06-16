# -*- coding: utf-8 -*-
# @Time: 2019/7/22 10:41
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: generate_readme.py
# @Software: PyCharm
import os
import re
from utils.is_post_file import  is_post_file


def get_posts_title():
    """
    获取文章的日期和标题
    :return:
    """
    posts_path = "../_posts/"
    for file_name in reversed(os.listdir(posts_path)):
        if is_post_file(file_name):
            with open(posts_path + file_name, "r", encoding = "utf-8") as post_file:
                post_date = None
                post_title = None
                for i in range(10):
                    """
                    读取前 10 行
                    readlines() 不能指定读取的行数
                    """
                    post_file_line = post_file.readline()
                    if post_file_line.find("date") != -1:
                        post_date = post_file_line[6:-7].split(" ")[0]
                    if post_file_line.find("title") != -1:
                        post_title = post_file_line[7:-1]

            post_info_to_readme = "* {} --- [{}]({}/{})"\
                .format(post_date, post_title, "https://yhw-miracle.github.io/blog", post_title)
            print(post_info_to_readme)
            write_readme(post_info_to_readme)


def write_readme(post_info):
    """
    将文章信息写入到 readme.md 文件里
    :param post_info:
    :return:
    """
    readme_path = "../readme.md"
    with open(readme_path, "a", encoding = "utf-8") as readme_file:
        readme_file.writelines(post_info + "\n")


if __name__ == '__main__':
    get_posts_title()
