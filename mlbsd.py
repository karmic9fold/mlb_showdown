import sys
from flask import Flask, render_template
from mlb_showdown import MLB_Showdown as MLB

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template ('game_display.html')

@app.route('/start_game')
def start_game():
    game = MLB()
    i = game.inning
    sb = game.scoreboard
    game_log = [] 

    while sb.inning < 9:
        MLB.away_inning()
        game_log.append(str(sb))

        if sb.inning > 8.5:
            if sb.home_score > sb.away_score:
                break
            else:
                MLB.home_extra_inning()
                game_log.append(str(sb))
        else:
            MLB.home_inning()
            game_log.append(str(sb))

    while sb.home_score == sb.away_score:
        MLB.away.inning()
        game_log.append(str(sb))
        MLB.home_extra_inning()
        game_log.append(str(sb))

        if sb.home_score != sb.away_score:
            break

    game_log.append(sb.display_final())

    return jsonify(game_log)

if __name__ == '__main__':
    app.run(debug=True) 
