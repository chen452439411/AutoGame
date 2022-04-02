# -*- encoding=utf8 -*-
__author__ = "chenjiarui"

from ControlGame.PlayGame.Common import *
from ControlGame.common import *


def play1():
    if_exists(path(__file__, "feiji_1.png"))
    qifei()


def play2():
    if_exists(path(__file__, "feiji_2.png"))
    qifei()


def play3():
    if_exists(path(__file__, "feiji_3.png"))
    qifei()


def play4():
    if_exists(path(__file__, "zsj_1.png"))
    qifei()


def play5():
    if_exists(path(__file__, "feiji_5.png"))
    qifei()


def main():
    close_view()
    qianjin()
    play1()
    play2()
    play3()
    play4()
    play5()
