class Inning:
    def __init__(self, mlb_game, outs=0, first=0, second=0, third=0, runs=0):
        self.mlb_game = mlb_game
        self.outs = outs
        self.first = first
        self.second = second
        self.third = third
        self.runs = runs

    def update_outs(self):
        self.outs = self.outs + 1

    def double_play():
        self.outs = self.outs + 2
