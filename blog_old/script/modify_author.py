# -*- coding: utf-8 -*-
# @Time: 2019/7/22 8:37
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: modify_author.py
# @Software: PyCharm
import re
import os


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


def list_all_files(folder):
    """
    遍历指定目录下的所有文件的文件名
    :param folder: 指定目录
    :return: 所有文件的文件名，以列表的形式返回
    """
    return os.listdir(folder)


if __name__ == '__main__':
    posts_folder = "../_posts/"
    for file_name in list_all_files(posts_folder):
        if is_post_file(file_name):
            with open(posts_folder + file_name, "r+", encoding = "utf-8") as file:
                file_content = file.read()
                file_content_replace = file_content.replace("yhw-miracle", "痛点就是起点")
                file.seek(0, 0)
                file.write(file_content_replace)

            # with open(posts_folder + file_name, "w", encoding = "utf-8") as file:
            #     # 重新打开文件，文件光标会文件起始位置
            #     file.write(file_content_replace)
