# -*- coding: utf-8 -*-
# @Time: 2019/7/22 13:25
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: create_post.py
# @Software: PyCharm
from datetime import datetime
import re
import os
from utils.is_post_file import is_post_file


def is_valid_post_title(post_title, post_type):
    """
    判断文章标题是否有效
    :param post_title: 文章标题，不能是数字开头，不能含有空格和下划线，不能重复
    :param post_type: 文章类型【post、draft】
    :return: 数字开头或含有空格和横线返回 -1，重复标题返回 -2，有效返回 0
    """
    if post_type == "post":
        post_path = "../_posts/"
    if post_type == "draft":
        post_path = "../_draft/"

    if re.match(r'^\d.+$', post_title) is None and post_title.find(" ") == -1 and post_title.find("-") == -1:
        for file_name in reversed(os.listdir(post_path)):
            if is_post_file(file_name):
                if file_name.split("-")[3][0:-3] == post_title:
                    return -2
            else:
                if file_name[0:-3] == post_title:
                    return -2
        return 0
    else:
        return -1


def create_new_post(post_title, post_type = None, categories = None, tags = None):
    """
    创建新文章
    :param post_title: 文章标题
    :param post_type: 文章类型【post、draft】
    :param categories: 文章标签，不指定为 None
    :param tags: 文章所属分类【问题解决、知识总结、技术案例、生活感悟，技术翻译、他山之石】，不指定为 None
    :return:
    """
    if post_type is None or post_type == "post":
        post_path = "../_posts/"
    if post_type == "draft":
        post_path = "../_draft/"
    
    post_title_status = is_valid_post_title(post_title, post_type)
    if post_title_status == 0:
        now_date = datetime.now()
        post_title_date = "{:04d}-{:02d}-{:02d}-".format(now_date.year, now_date.month, now_date.day)
        post_date = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} +0800"\
            .format(now_date.year,
                    now_date.month,
                    now_date.day,
                    now_date.hour,
                    now_date.minute,
                    now_date.second)
        with open(post_path + post_title_date + post_title + ".md", "w", encoding = "utf-8") as post_file:
            post_file.write("---\n"
                            "layout: post\n"
                            "title: {}\n"
                            "date: {}\n"
                            "tags: []\n"
                            "categories: []\n"
                            "author: 痛点就是起点\n"
                            "published: false\n"
                            "---\n".format(post_title, post_date))
            print("create post {} success!".format(post_title))
    elif post_title_status == -1:
        print("文章标题不能是数字开头，且不能含有空格和横线！")
    elif post_title_status == -2:
        print("文章标题不能重复！")


if __name__ == '__main__':
    create_new_post(post_title = input("输入文章标题，不能是数字开头，不能含有横线和空格："), post_type = input("选择文章类型【post or draft】"))
