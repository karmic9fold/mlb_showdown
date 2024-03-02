# main game file
import sys
from flask import Flask, render_template, jsonify
from random import randint
from time import sleep
# from ddtrace import patch_all
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

    def away_inning(self):
        sb = self.scoreboard
        mlb_game = self
        at_bat_results = []
        sb.display_scoreboard()
        while i.outs < 3:
                batter = AL.pop(0)
                pitcher = HPS[0]
                ab = AB(pitcher, batter, mlb_game) 
                ab.check_advantage()
                result = ab.swing_result()
                at_bat_results.append(result)
                AL.append(batter)
                sleep(.1)
        sb.update_away_score()
        ab.home_inning_pitched()
        sb.update_inning()
        sleep(.1)
        return at_bat_results
            
    def home_inning(self):
        sb = self.scoreboard
        mlb_game = self
        sb.display_scoreboard()
        at_bat_results = []
        while i.outs < 3:
                batter = HL.pop(0)
                pitcher = APS[0]
                ab = AB(pitcher, batter, mlb_game)
                ab.check_advantage()
                result = ab.swing_result()
                at_bat_results.append(result)
                HL.append(batter)
                sleep(.1)
        sb.update_home_score()
        ab.away_inning_pitched()
        sb.update_inning()
        sleep(.1)
        return at_bat_results

    def home_extra_inning(self):
        sb = self.scoreboard
        mlb_game = self
        sb.display_scoreboard()
        at_bat_results = []
        while i.outs < 3:
            if sb.home_score > sb.away_score:
                break
            else:
                batter = HL.pop(0)
                pitcher = APS[0]
                ab = AB(pitcher, batter, mlb_game)
                ab.check_advantage()
                result = ab.swing_result()
                at_bat_results.append(result)
                HL.append(batter)
                sb.check_game_over()
                sleep(.1)
        sb.update_extra_home_score()
        ab.away_inning_pitched()
        sb.update_inning()
        sleep(.1)
        return at_bat_results

mlb_game = MLB_Showdown()
i = mlb_game.inning
sb = mlb_game.scoreboard

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template ('game_display.html')

@app.route('/start_game')
def start_game():
    print("The game has started") 
    inning_results = []  # Initialize inning_results list
    final_result = None

    while mlb_game.scoreboard.inning < 3:
        inning_data = {
            'top_half_results': mlb_game.away_inning(),
            'bottom_half_results': mlb_game.home_inning()
        }
        inning_results.append(inning_data)

    while mlb_game.scoreboard.home_score == mlb_game.scoreboard.away_score:
        inning_data = {
            'top_half_results': mlb_game.away_inning(),
            'bottom_half_results': mlb_game.home_inning()
        }
        inning_results.append(inning_data)

    final_result = mlb_game.scoreboard.display_final()
    home_score = mlb_game.scoreboard.home_score
    away_score  = mlb_game.scoreboard.away_score

    print("Inning Results:", inning_results)
    print("Final result:", final_result)

    return jsonify({'inning_results': inning_results, 
                    'final_result': final_result,
                    'home_score': home_score,
                    'away_score': away_score
                    })

# DD_SERVICE="MLBShowdown" 
# DD_ENV="MLBtest"
# DD_LOGS_INJECTION=true

if __name__ == '__main__':
    app.run(debug=True)
