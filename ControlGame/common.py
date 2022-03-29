import os
import datetime
from airtest.core.api import *


def path(file, file_name):
    """输出绝对路径"""
    current_dir = os.path.dirname(file)
    parent_path = os.path.dirname(current_dir)
    return current_dir + "/" + file_name


def log_time():
    """输出时间"""
    now_time = datetime.datetime.now()
    time = datetime.datetime.strftime(now_time, '%Y-%m-%d-%H:%M:%S')
    return time


def if_exists(photo):
    """封装先exists再touch的操作"""
    try:
        if exists(Template(photo)):
            touch(Template(photo))
            print(photo, '已执行')
        else:
            print(photo, '未发现，未执行')
    except Exception as e:
        print(e, photo, '未执行')
