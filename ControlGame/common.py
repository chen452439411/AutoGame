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


def click_absolute_coordinates(coordinates,name = None):
    touch(coordinates)
    print(name,'已点击',coordinates,'坐标')

def click_attack1():
    """点击攻击方式1"""
    coordinates = (1169,527)
    click_absolute_coordinates(coordinates,'attack1')

def click_attack2():
    """点击攻击方式2"""
    coordinates = (1104,642)
    click_absolute_coordinates(coordinates,'attack2')

def click_attack3():
    """点击攻击方式3"""
    coordinates = (1159,723)
    click_absolute_coordinates(coordinates,'attack3')

def click_attack4():
    """点击攻击方式4"""
    coordinates = (1305,732)
    click_absolute_coordinates(coordinates,'attack4')

def click_attack5():
    """点击攻击方式5"""
    coordinates = (1353,630)
    click_absolute_coordinates(coordinates,'attack5')

def click_attack6():
    """点击攻击方式6"""
    coordinates = (1307,532)
    click_absolute_coordinates(coordinates,'attack6')

def click_attack_centre():
    """点击攻击射击键"""
    coordinates = (1231,637)
    click_absolute_coordinates(coordinates,'centre')