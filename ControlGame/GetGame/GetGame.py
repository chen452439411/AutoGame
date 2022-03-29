# 进入对局
from airtest.core.api import *
from ControlGame.common import *


class GetGame(object):

    # 生成游戏对局对象
    # ad = 0 看广告 ad = 1 不看广告
    def __init__(self, ad_home=1):
        self.ad_home = ad_home

    def ad_gold(self):
        if self.ad_home == 0:
            # 看广告操作
            pass
        else:
            print('不看广告【ad】值为%s' % (self.ad_home))

    def is_homelibao(self):
        """True:有礼包并且关闭 False:无礼包"""
        if exists(Template(path(__file__, "gk_libao_X.png"))):
            print("发现港口礼包页面")
            touch(Template(path(__file__, "gk_libao_X.png")))
            print("已关闭港口礼包页面")
            return True
        else:
            print("没有检测到港口礼包页面")
            return False

    def is_inhome(self):
        """True:已经在首页了 False:没有在首页"""
        self.is_homelibao()
        if exists(Template(path(__file__, "home1.png"))):
            print("检测已经回到港口")
            return True
        else:
            print("没有检测已经回到港口")
            return False

    def main(self):
        self.is_homelibao()
        self.ad_gold()
        touch(Template(path(__file__, "home1.png")))
        touch(Template(path(__file__, "home2.png")))
        touch(Template(path(__file__, "home3.png")))
        touch(Template(path(__file__, "home4.png")))
