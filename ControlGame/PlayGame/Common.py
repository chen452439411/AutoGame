from airtest.core.api import *
from ControlGame.common import *


def qianjin():
    """前进操作"""
    try:
        touch(wait(Template(path(__file__, 'qianjin.png'), record_pos=(-0.325, 0.099), resolution=(1664, 1040)),
                   timeout=60))
    except Exception as e:
        print(e, 'qianjin未执行')


def qifei():
    """飞机起飞"""
    if_exists(path(__file__, "qifei.png"))


def close_view():
    """关闭视野"""
    if_exists(path(__file__, "close_view.png"))
