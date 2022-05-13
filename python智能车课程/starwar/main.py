import pygame

from source import tools,setup
from source.states import main_menu,load,level,level2
from source.compounent import other_things


def main():
    # 状态字典，依次读入状态
    state_dic = {'main_menu': main_menu.Mainmenu(),
                 'load': load.Load(),
                 'level': level.Leval(),
                 'level2': level2.Leval2()}
    game=tools.GAME(state_dic,'main_menu')
    game.run()


if __name__=='__main__':
    main()