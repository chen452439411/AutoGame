# 退出对局
from airtest.core.api import *
from ControlGame.GetGame import GetGame
from ControlGame.common import *


class ExitGame(object):
    def __init__(self, ad_exit=1):
        # ad = 0 看广告 ad = 1 不看广告
        self.ad_exit = ad_exit

    def ad_gold(self):
        ad_exit = self.ad_exit
        if ad_exit == 0:
            if_exists(path(__file__, "ad_exit.png"))
            pass
        else:
            print('不看广告【ad_exit】值为%s' % (ad_exit))

    def is_net(self):
        """是否出现网络异常"""
        if_exists(path(__file__, "other1.png"))

    def is_ad(self):
        """是否出现结束广告"""
        if_exists(path(__file__, "other3.png"))

    def is_returnhome(self):
        """是否出现返回港口 True：发现返回港口页面并且已经返回港口 False：未返回港口"""
        if exists(Template(path(__file__, "return_home.png"), record_pos=(0.001, 0.202), resolution=(1664, 1040))):
            print("发现对局结束结算页面")
            if self.ad_exit == 1:
                touch(Template(path(__file__, "return_home.png"), record_pos=(0.001, 0.202), resolution=(1664, 1040)))
            else:
                self.ad_gold()
            return True
        else:
            print("未发现对局结束结算页面")
            return False

    def main(self):
        """True：已返回home False：还在对局中"""

        def exit1():
            """True：已经返回首页 False：还在对局当中"""
            if GetGame.GetGame().is_inhome():
                stata = True
            elif self.is_returnhome():
                stata = True
            else:
                stata = False
            print(stata, 'exit1')
            return stata

        if exit1():
            stata = True
            print(stata, 'main')
            return stata
        else:
            self.is_net()
            self.is_ad()
            stata = exit1()
            return stata
