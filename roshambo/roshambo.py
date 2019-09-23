# coding=utf-8
"""
石头剪刀布小游戏.

:作者:
    0o唯有杜康o0 -- 来源于公众号【师兄带你学Python】
:游戏规则:
    1. 玩家通过交互界面输入R(石头)、P(剪刀)、S(布)
    2. 电脑玩家随机输出R(石头)、P(剪刀)、S(布)
    3. 裁判判定赢家
"""
import random

# 石头剪刀布英文对应关系
JSON_ROCK_PAPER_SCISSORS = {
    "R": "石头",
    "P": "剪刀",
    "S": "布",
}


class Player(object):
    """
    石头剪刀布 玩家类
    """
    # 玩家名称
    name = "玩家"
    # 玩家出手提示消息
    msg_on_player_do_it = "%s: " % name
    # 输入玩家名称提示消息
    msg_on_input_player_name = "请输入玩家名称: "

    def __init__(self):
        # 该玩家的出手记录
        self.list_player_input = list()

    def input_name(self):
        self.name = input(self.msg_on_input_player_name)
        self.msg_on_player_do_it = "%s: " % self.name

    def do_it(self):
        """
        玩家出手
        """
        player_input = input(self.msg_on_player_do_it).upper()
        while player_input not in list(JSON_ROCK_PAPER_SCISSORS.keys()):
            print("输入不合法,请重新输入")
            player_input = input(self.msg_on_player_do_it).upper()
        self.list_player_input.append(player_input)

    def get_player_input(self, shift=0):
        """
        获取玩家的出手结果

        :参数:
            * shift    出手记录中的偏移(shift=0代表返回最后一次出手结果,shift=1代表返回倒数第二次出手结果)
        :返回值:
            出手结果简写码('S' | 'P' | 'R')
        """
        index = -1 - shift
        return self.list_player_input[index]


class ComputerPlayer(Player):
    """
    电脑玩家类
    """
    # 玩家名称
    name = "电脑"
    # 玩家出手提示消息
    msg_on_player_do_it = "%s: " % name

    def do_it(self):
        player_input = random.choice(list(JSON_ROCK_PAPER_SCISSORS.keys()))
        msg = "%s%s" % (self.msg_on_player_do_it, player_input)
        print(msg)
        self.list_player_input.append(player_input)


class Referee(object):
    """
    裁判类
    """
    # 连胜数达到多少打印菜彩蛋
    number_win = 5

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.number_player1_win = 0
        self.number_player2_win = 0

    @staticmethod
    def print_game_result(game_result):
        """
        输出效果美化

        :参数:
            * width          美化后保持的输出宽度
            * game_result    比赛结果字典
            :Demo:
            >>> {
            >>>     "record": { "电脑": "石头", "玩家": "布"},
            >>>     "result": "玩家获胜",
            >>>     "surprise": "你可以让电脑买彩票了,这家伙已经连赢5局了"
            >>> }
        :返回值:
            无
        """
        list_output = list()
        for key, value in game_result['record'].items():
            _str = "%s: %s" % (key, value)
            list_output.append(_str)
        print("%s==>%s" % (','.join(list_output), game_result['result']))
        if game_result['surprise']:
            print(game_result['surprise'])

    def calculate_game_result(self):
        """
        计算比赛结果

        :参数:
            * record     玩家出手记录
            :Demo:
            >>> { "电脑": "R", "玩家": "S"}
        :返回值:
            比赛结果
            :Demo:
            >>> {
            >>>     "record": { "电脑": "石头", "玩家": "布"},
            >>>     "result": "玩家获胜"
            >>> }
        """
        surprise = ''
        input_player1 = self.player1.get_player_input()
        input_player2 = self.player2.get_player_input()
        if (input_player1 == 'S' and input_player2 == 'P') or \
                (input_player1 == 'P' and input_player2 == 'R') or \
                (input_player1 == 'R' and input_player2 == 'S'):
            result = "%s获胜" % self.player1.name
            self.number_player1_win += 1
            self.number_player2_win = 0
            if self.number_player1_win >= self.number_win:
                self.number_player1_win = 0
                surprise = "你可以让%s买彩票了,这家伙已经连赢%s局了" % (self.player1.name, self.number_win)
        elif (input_player1 == 'P' and input_player2 == 'S') or \
                (input_player1 == 'R' and input_player2 == 'P') or \
                (input_player1 == 'S' and input_player2 == 'R'):
            result = "%s获胜" % self.player2.name
            self.number_player2_win += 1
            self.number_player1_win = 0
            if self.number_player2_win >= self.number_win:
                self.number_player2_win = 0
                surprise = "你可以让%s买彩票了,这家伙已经连赢%s局了" % (self.player2.name, self.number_win)
        else:
            result = "双方打平"

        data = {
            "record": {
                self.player1.name: JSON_ROCK_PAPER_SCISSORS[input_player1],
                self.player2.name: JSON_ROCK_PAPER_SCISSORS[input_player2]
            },
            "result": result,
            "surprise": surprise
        }
        return data


class Roshambo(object):
    """
    石头剪刀布小游戏.

    :作者:
        0o唯有杜康o0 -- 来源于公众号【师兄带你学Python】
    :游戏规则:
        1. 玩家通过交互界面输入R(石头)、P(剪刀)、S(布)
        2. 电脑玩家随机输出R(石头)、P(剪刀)、S(布)
        3. 裁判判定赢家
    """
    def start(self):
        print("#" * 60)
        print(self.__doc__)
        print("#" * 60)
        player = Player()
        player.input_name()
        computer_player = ComputerPlayer()
        referee = Referee(player1=player, player2=computer_player)
        while True:
            player.do_it()
            computer_player.do_it()
            game_result = referee.calculate_game_result()
            referee.print_game_result(game_result)


if __name__ == '__main__':
    roshambo = Roshambo()
    roshambo.start()
