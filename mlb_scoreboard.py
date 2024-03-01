class Scoreboard:
    def __init__(self, mlb_game, home_score=0, away_score=0, inning=.5):
        self.mlb_game = mlb_game
        self.inning = inning
        self.home_score = home_score
        self.away_score = away_score
        self.extra_inning_runs = 0

    def update_away_score(self):
        mlb_game = self.mlb_game
        self.away_score = self.away_score + mlb_game.inning.runs

    def update_home_score(self):
        mlb_game = self.mlb_game
        self.home_score = self.home_score + mlb_game.inning.runs

    def update_extra_home_score(self):
        mlb_game = self.mlb_game
        if self.home_score > self.away_score:
            self.home_score = self.home_score
        else:
            self.home_score = self.home_score + mlb_game.inning.runs

    def update_inning(self):
        mlb_game = self.mlb_game
        self.extra_inning_runs = self.mlb_game.inning.runs
        print(f"END OF {self.inning}!")
        print(f"You scored {self.extra_inning_runs} runs!\n")
        mlb_game.inning.outs = 0
        mlb_game.inning.first = 0
        mlb_game.inning.second = 0
        mlb_game.inning.third = 0
        mlb_game.inning.runs = 0
        self.inning = self.inning + .5

    def advance_inning(self): 
        mlb_game = self.mlb_game
        mlb_game.inning.outs = 0
        mlb_game.inning.first = 0
        mlb_game.inning.second = 0
        mlb_game.inning.third = 0
        mlb_game.inning.runs = 0
        self.inning = self.inning + .5
        print(self.inning)

    def display_scoreboard(self):
        curr_inning = 0
        curr_inning = self.inning + .5
        if self.inning > 8.5 and self.away_score > self.home_score:
            print(self.inning)
            print(f"Inning: Bot {int(self.inning)} \
Home: {self.home_score} Away: {self.away_score}\n")
        elif (self.inning - int(self.inning) == 0):
            print(self.inning)
            print(f"Inning: Bot {int(self.inning)} \
Home: {self.home_score} Away: {self.away_score}\n")
        else:
            print(self.inning)
            print(f"Inning: Top {int(curr_inning)} \
Home: {self.home_score} Away: {self.away_score}\n")

    def display_final(self):
        print(f"FINAL {int(self.inning)} Home: {self.home_score} \
Away: {self.away_score}\n")
        return f"{int(self.inning)} Innings- Home: {self.home_score} \
Away: {self.away_score}\n"

    def check_game_over(self):
        mlb_game = self.mlb_game
        x = self.away_score - self.home_score
        if mlb_game.inning.runs > x:
            self.extra_inning_runs = mlb_game.inning.runs
            self.home_score = self.home_score + self.extra_inning_runs
            print("WALK OFF!")
            return f"WALK OFF"
            self.extra_inning_runs = 0
