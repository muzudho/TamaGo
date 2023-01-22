from board.constant import PASS, RESIGN, OB_SIZE, GTP_X_COORDINATE

class Coordinate:
    """座標変換処理クラス
    """
    def __init__(self, board_size):
        """座標変換処理の初期化。

        Args:
            board_size (int): 碁盤の大きさ。
        """
        self.board_size = board_size
        self.board_size_with_ob = board_size + OB_SIZE * 2

    def convert_from_gtp_format(self, pos):
        """GTP形式の座標からプログラム内部表現の座標に変換する。

        Args:
            pos (str): Go Text Protocol形式の座標。

        Returns:
            int: プログラム内部表現の座標。
        """
        if pos.upper() == "PASS":
            return PASS
        elif pos.upper() == "RESIGN":
            return RESIGN
        else:
            alphabet = pos.upper()[0]
            x = 0
            for i in range(self.board_size):
                if GTP_X_COORDINATE[i + 1] is alphabet:
                    x = i
            y = self.board_size - int(pos[1:])
            
            pos = x + OB_SIZE + (y + OB_SIZE) * self.board_size_with_ob

            return pos

    def convert_to_gtp_format(self, pos):
        """プログラム内部の座標からGTP形式に変換する。

        Args:
            pos (int): プログラム内部表現の座標。

        Returns:
            str: Go Text Protocol形式の座標。
        """
        if pos == PASS:
            return "PASS"
        elif pos == RESIGN:
            return "RESIGN"
        else:
            x = pos % self.board_size_with_ob - OB_SIZE + 1
            y = self.board_size - (pos // self.board_size_with_ob - OB_SIZE)
            return (GTP_X_COORDINATE[x] + str(y))
