from ControlGame.GetGame import GetGame
from ControlGame.ExitGame import ExitGame
from ControlGame.PlayGame.PlayCN004_1 import Play_CN004_1
from ControlGame.PlayGame.PlayCN004_2 import Play_CN004_2
from ControlGame.PlayGame.PlayCN004_3 import Play_CN004_3

from ControlGame.config_game import PLAYNAME
from ControlGame.common import *
from airtest.core.api import *
import logging
import threading


# auto_setup(__file__, devices=["Android:///"], logdir="/Users/chenjiarui/PycharmProjects/AutoGame/log/%s" % (log_time()))
# auto_setup(__file__, devices=["Android:///"])

# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)


#auto_setup(__file__,devices=["Android://127.0.0.1:5037/emulator-5554"])
class RunGame(object):
    def __init__(self, play_name, phone, ad_home=1, ad_exit=1):

        auto_setup(__file__)
        connect_device("Android://%s" % (phone))
        #connect_device("")
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)

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

connect_device("Android://127.0.0.1:5037/127.0.0.1:7555")
RunGame('CN004_3', '127.0.0.1:5037/127.0.0.1:7555').main()
# def threading_test(name, phone):
#     RunGame(name, phone).main()
#
#
# obj1 = threading.Thread(target=threading_test, args=("CN004_2","Android://127.0.0.1:5037/127.0.0.1:7555"))
# obj2 = threading.Thread(target=threading_test, args=("CN004_2","Android://127.0.0.1:5037/emulator-5554"))
#
# obj1.start()
# obj2.start()