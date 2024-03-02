from random import randint
from time import sleep
from home_team import home_lineup as HL, home_pitching_staff as HPS
from away_team import away_lineup as AL, away_pitching_staff as APS
from mlb_scoreboard import Scoreboard as SB
from at_bat import At_Bat as AB
from inning import Inning


class MLB_Showdown:

    def __init__(self):
        self.scoreboard = SB(self)
        self.inning = Inning(self)
        self.outs = 0
        self.HL = HL
        self.HPS = HPS
        self.AL = AL
        self.APS = APS

    def away_inning():
        sb.display_scoreboard()
        while i.outs < 3:
                batter = AL.pop(0)
                pitcher = HPS[0]
                ab = AB(pitcher, batter, mlb_game) 
                ab.check_advantage()
                ab.swing_result()
                AL.append(batter)
                sleep(1)
        sb.update_away_score()
        ab.home_inning_pitched()
        sb.update_inning()
        sleep(2.5)
            

    def home_inning():
        sb.display_scoreboard()
        while i.outs < 3:
                batter = HL.pop(0)
                pitcher = APS[0]
                ab = AB(pitcher, batter, mlb_game)
                ab.check_advantage()
                ab.swing_result()
                HL.append(batter)
                sleep(1)
        sb.update_home_score()
        ab.away_inning_pitched()
        sb.update_inning()
        sleep(2.5)

    def home_extra_inning():
        sb.display_scoreboard()
        while i.outs < 3:
            if sb.home_score > sb.away_score:
                break
            else:
                batter = HL.pop(0)
                pitcher = APS[0]
                ab = AB(pitcher, batter, mlb_game)
                ab.check_advantage()
                ab.swing_result()
                HL.append(batter)
                sb.check_game_over()
                sleep(1)
        sb.update_extra_home_score()
        ab.away_inning_pitched()
        sb.update_inning()
        sleep(2.5)



return(f"Inning: BOT {self.inning}, Home: {self.home_score}, \
Away: {self.away_score}")