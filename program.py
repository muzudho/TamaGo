"""プログラムの情報。
"""
PROGRAM_NAME="TamaGo"
PROTOCOL_VERSION="2"

# Version 0.0.0 : ランダムプレイヤの実装。
# Version 0.1.0 : SGFファイルの読み込み処理の実装。load_sgfコマンドの対応。
#                 配石パターンのデータ構造の追加。眼の判定、上下左右の空点判定等改善。
#                 着手履歴、Zobrist Hash、超劫の判定の実装。
# Version 0.2.0 : ニューラルネットワークの教師あり学習の実装。
#                 Policy Networkを使用した着手生成ロジックの実装。
# Version 0.2.1 : Residual Blockの構造を修正。学習の再実行。
# Version 0.3.0 : モンテカルロ木探索の実装。
# Version 0.3.1 : モンテカルロ木探索のValue更新処理のバグ修正。komi, get_komiコマンドのサポート。
# Version 0.4.0 : Sequential Halving Applied to Trees (SHOT) の実装。
# Version 0.5.0 : 探索時間の制御、time_left、time_settingsコマンドのサポート。
# Version 0.6.0 : Gumbel AlphaZero方式の強化学習の実装。ネットワークの構造改善。
# Version 0.6.1 : --batch-sizeオプションの追加。
VERSION="0.6.1"
