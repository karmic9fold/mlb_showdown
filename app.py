import sys
from flask import Flask, render_template, jsonify
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

mlb_game = MLB_Showdown()
game_log = []
i = mlb_game.inning
sb = mlb_game.scoreboard

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template ('game_display.html')

@app.route('/start_game')
def start_game():   
    while sb.inning < 3:
        MLB_Showdown.away_inning()
        game_log.append(str(sb.display_scoreboard()))

        if sb.inning > 2.5:
            if sb.home_score > sb.away_score:
                break
            else:
                MLB_Showdown.home_extra_inning()
                game_log.append(str(sb.display_scoreboard()))
        else:
            MLB_Showdown.home_inning()
            game_log.append(str(sb.display_scoreboard()))

    while sb.home_score == sb.away_score:
        MLB_Showdown.away_inning()
        game_log.append(str(sb.display_scoreboard()))
        MLB_Showdown.home_extra_inning()
        game_log.append(str(sb.display_scoreboard()))

        if sb.home_score != sb.away_score:
            break

    final_result = sb.display_final()

    return jsonify({'game_log': game_log, 'final_result': final_result})

if __name__ == '__main__':
    app.run(debug=True) 
