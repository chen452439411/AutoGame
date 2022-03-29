from ControlGame.GetGame import GetGame
from ControlGame.ExitGame import ExitGame
from ControlGame.PlayGame.PlayCN004 import Play_CN004
from ControlGame.config_game import PLAYNAME
from ControlGame.common import *
from airtest.core.api import *

# auto_setup(__file__, devices=["Android:///"], logdir="/Users/chenjiarui/PycharmProjects/AutoGame/log/%s" % (log_time()))
auto_setup(__file__, devices=["Android:///"])
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class RunGame(object):
    def __init__(self, play_name, ad_home=1, ad_exit=1):
        self.play_main = PLAYNAME[play_name]['main']
        self.play_num = PLAYNAME[play_name]['num']
        self.ad_home = ad_home
        self.ad_exit = ad_exit

    def play(self):
        eval(self.play_main)

    def main(self):
        for i in range(99999):
            try:
                GetGame.GetGame(self.ad_home).main()
                for ii in range(self.play_num):
                    print("第%s局第%s次循环play开始" % (i, ii))
                    log("第%s局第%s次循环play开始" % (i, ii), desc="main")
                    self.play()
                    if ExitGame.ExitGame(self.ad_exit).main():
                        break
                    else:
                        pass
            except Exception as e:
                print(e, 'Main.main()失败')


RunGame('CN004').main()
