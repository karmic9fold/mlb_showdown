from random import randint

from home_team import home_lineup as HL, home_pitching_staff as HPS
from away_team import away_lineup as AL, away_pitching_staff as APS 
from inning import Inning
from mlb_scoreboard import Scoreboard as SB

def roll_die():
    return randint(1,20)

class At_Bat:
    def __init__(self, current_pitcher, current_batter, mlb_game,
        pitcher_advantage=False, batter_advantage=False):
        self.current_pitcher = current_pitcher
        self.current_batter = current_batter
        self.mlb_game = mlb_game
        self.pitcher_advantage = pitcher_advantage
        self.batter_advantage = batter_advantage
        
    def away_inning_pitched(self):
        self.current_pitcher['innings'] = self.current_pitcher['innings'] - 1
        if self.current_pitcher['innings'] ==0:
            self.mlb_game.APS.pop(0)

    def home_inning_pitched(self):
        self.current_pitcher['innings'] = self.current_pitcher['innings'] - 1
        if self.current_pitcher['innings'] ==0:
            self.mlb_game.HPS.pop(0)

    def check_advantage(self):
        pitch_roll = roll_die()
        pitch = int(pitch_roll) + self.current_pitcher['control']
        """pitch roll value is added to pitchers control."""
        print(f"Add roll {pitch_roll} to {self.current_pitcher['name'].title()} control \
{self.current_pitcher['control']}... {pitch}.")
        print(f"{self.current_batter['name'].title()} On Base: {self.current_batter['on_base']}")
        if int(pitch) > self.current_batter['on_base']:
            print("Pitcher has the advantage!")
            self.pitcher_advantage = True
        elif int(pitch) <= self.current_batter['on_base']:
            print("Batter has the advantage.")
            self.batter_advantage = True

    def swing_result(self):
        i = self.mlb_game.inning
        swing = roll_die()
        print(f"Batter has rolled {swing}.")
        while self.pitcher_advantage is True:
            if int(swing) < (self.current_pitcher['put_out']):
                print(f"{self.current_batter['name'].title()} has been put out.\n")
                self.pitcher_advantage = False
                i.outs = i.outs + 1
            elif int(swing) < (self.current_pitcher['strike_out']):
                print(f"{self.current_batter['name'].title()} has struck out.\n")
                self.pitcher_advantage = False
                i.outs = i.outs + 1
            elif int(swing) < (self.current_pitcher['ground_out']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0: 
                    i.outs = i.outs + 1
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                elif i.first == 1 and i.second == 0 and i.third == 0: #Man 1
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!\n")
                        i.first = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0: #Man 1,2
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!\n")
                        i.first = 0
                        i.second = 0
                        i.third = 1
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0: # Man on 2
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1: #Man 2,3 
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out. Runner looked back to 3rd.\n")
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1: #Man 3
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                    i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1: #Man 1,3
                    if i.outs < 2:
                        i.first = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!\n")
                    else:
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1: #Man 1,2,3
                    if i.outs < 2:
                        i.first = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!\n")
                    else:
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
            
            elif int(swing) < (self.current_pitcher['fly_out']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1: 
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1

            elif int(swing) < (self.current_pitcher['walk']):
                self.pitcher_advantage = False
                print(f"{self.current_batter['name'].title()} has walked.\n")
                if i.first == 0 and i.second == 0 and i.third == 0:
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    i.first = 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    i.first = 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_pitcher['single']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.first = 1
                    i.second = 0
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.first = 1
                    i.second = 0 
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.first = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.second = 1
                    i.third = 0 
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.runs = i.runs + 1
                
            elif int(swing) < (self.current_pitcher['single_plus']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus.\n")
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus.\n")
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    i.third = 1
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus.\n")
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus.\n")
                    i.first = 1
                    i.second = 0
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus.\n")
                    i.first = 1
                    i.second = 0 
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus.\n")
                    i.first = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus.\n")
                    i.second = 1
                    i.third = 0 
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus.\n")
                    i.runs = i.runs + 1
                
            elif int(swing) < (self.current_pitcher['double']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.second = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.first = 0
                    i.second = 1
                    i.third = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.first = 0
                    i.second = 1
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.third = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.second = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.first = 0
                    i.second = 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.first = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1

            elif int(swing) < (self.current_pitcher['triple']):
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
triple.\n")
                    i.third = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.third = 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.second = 0
                    i.third = 1
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.second = 0 
                    i.third = 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.second = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
bases clearing triple!\n")
                    i.first = 0
                    i.second = 0 
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_pitcher['home_run']): 
                self.pitcher_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Home Run!\n")
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.first = 0 
                    i.runs = i.runs + 2
                elif i.first == 1 and i.second ==1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.first = 0
                    i.second = 0
                    i.runs = i.runs + 3
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.second = 0 
                    i.runs = i.runs + 2
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.second = 0
                    i.third = 0
                    i.runs = i.runs + 3
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.third = 0
                    i.runs = i.runs + 2
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.first = 0 
                    i.third = 0 
                    i.runs = i.runs + 3
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
GRAND SLAM!\n")
                    i.first = 0
                    i.second = 0
                    i.third = 0
                    i.runs = i.runs + 4
        while self.batter_advantage is True:
            if int(swing) < (self.current_batter['put_out']):
                print(f"{self.current_batter['name'].title()} has been put out.\n")
                self.batter_advantage = False
                i.outs = i.outs + 1
            elif int(swing) < (self.current_batter['strike_out']):
                print(f"{self.current_batter['name'].title()} has struck out.\n")
                self.batter_advantage = False
                i.outs = i.outs + 1
            elif int(swing) < (self.current_batter['ground_out']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0: #Empty
                    i.outs = i.outs + 1
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                elif i.first == 1 and i.second == 0 and i.third == 0: #Man 1
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!.\n")
                        i.first = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0: #Man 1,2
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play!. Runner advances to 3rd.\n")
                        i.first = 0
                        i.second = 0
                        i.third = 1
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0: # Man on 2
                    print(f"{self.current_batter['name'].title()} has hit \
a ground out. Runner advances to 3rd.\n")
                    i.second = 0
                    i.third = 1
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1: #Man 2,3
                    if i.outs < 2:
                        i.outs = i.outs + 1
                        i.second = 0
                        i.runs = i.runs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
an RBI fielder's choice.\n")
                    else:
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                elif i.first == 0 and i.second == 0 and i.third == 1: #Man 3
                    if i.outs < 2:
                        i.outs = i.outs + 1
                        i.third = 0 
                        i.runs = i.runs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
an RBI fielder's choice.\n")
                    else:
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1: #Man 1,3
                    if i.outs < 1:
                        i.first = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                        i.third = 0 
                        i.runs = i.runs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
into an RBI double play!.\n")
                    elif i.outs < 2:
                        i.first = 0
                        i.second = 1
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a fielder choice. Runner held at 3rd. Out at first.\n")
                    else:
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
                elif i.first == 1 and i.second == 1 and i.third == 1: #Man 1,2,3
                    if i.outs < 1:
                        i.first = 0
                        i.second = 0
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
into an RBI double play!.\n")
                    elif i.outs < 2:
                        i.outs = i.outs + 1
                        i.outs = i.outs + 1
                        i.first = 0 
                        i.second = 0
                        print(f"{self.current_batter['name'].title()} has hit \
into a double play\n")
                    else:
                        i.outs = i.outs + 1
                        print(f"{self.current_batter['name'].title()} has hit \
a ground out.\n")
            elif int(swing) < (self.current_batter['fly_out']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                    i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out. Runner tags to Third.\n")
                        i.second = 0
                        i.third = 1
                        i.outs = i.outs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly. Runner Advances to third.\n")
                        i.second = 0
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly. Runner held on First.\n")
                        i.third = 0 
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1: 
                    if i.outs < 2:
                        print(f"{self.current_batter['name'].title()} has hit a \
Sacrifice Fly. Runner on 2nd advances.\n")
                        i.second =  0
                        i.outs = i.outs + 1
                        i.runs = i.runs + 1
                    else:
                        print(f"{self.current_batter['name'].title()} has hit a \
fly out.\n")
                        i.outs = i.outs + 1
            elif int(swing) < (self.current_batter['walk']):
                self.batter_advantage = False
                print(f"{self.current_batter['name'].title()} has walked.\n")
                if i.first == 0 and i.second == 0 and i.third == 0:
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    i.first = 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    i.first = 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    i.second = 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_batter['single']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.second = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.first = 1
                    i.second = 0
                    i.third = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single.\n")
                    i.third = 0
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.first = 1
                    i.second = 0 
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.first = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.second = 1
                    i.third = 0 
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single.\n")
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_batter['single_plus']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus.\n")
                    i.first = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
single plus. Runner advances from First to Third.\n")
                    i.third = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runner advances from 1st to 3rd.\n")
                    i.second = 0
                    i.third = 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runner scores from 2nd.\n")
                    i.first = 1
                    i.second = 0
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runners score from 2nd and 3rd.\n")
                    i.first = 1
                    i.second = 0 
                    i.third = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runner scores from 3rd.\n")
                    i.first = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runner advances from 1st to 3rd.\n")
                    i.second = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI single plus. Runners score from 2nd and 3rd.\n")
                    i.second = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_batter['double']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.second = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.first = 0
                    i.second = 1
                    i.third = 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
double.\n")
                    i.first = 0
                    i.second = 1
                    i.third = 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.third = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.second = 1
                    i.third = 0
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.first = 0
                    i.second = 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI double.\n")
                    i.first = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_batter['triple']):
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
triple.\n")
                    i.third = 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.third = 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.second = 0
                    i.third = 1
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.second = 0 
                    i.third = 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.second = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit an \
RBI triple.\n")
                    i.first = 0
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
bases clearing triple!\n")
                    i.first = 0
                    i.second = 0 
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
                    i.runs = i.runs + 1
            elif int(swing) < (self.current_batter['home_run']): 
                self.batter_advantage = False
                if i.first == 0 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Home Run!\n")
                    i.runs = i.runs + 1
                elif i.first == 1 and i.second == 0 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.first = 0 
                    i.runs = i.runs + 2
                elif i.first == 1 and i.second == 1 and i.third ==0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.first = 0
                    i.second = 0
                    i.runs = i.runs + 3
                elif i.first == 0 and i.second == 1 and i.third == 0:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.second = 0 
                    i.runs = i.runs + 2
                elif i.first == 0 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.second = 0
                    i.third = 0
                    i.runs = i.runs + 3
                elif i.first == 0 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Two-run Home Run!\n")
                    i.third = 0
                    i.runs = i.runs + 2
                elif i.first == 1 and i.second == 0 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
Three-run Home Run!\n")
                    i.first = 0 
                    i.third = 0 
                    i.runs = i.runs + 3
                elif i.first == 1 and i.second == 1 and i.third == 1:
                    print(f"{self.current_batter['name'].title()} has hit a \
GRAND SLAM!\n")
                    i.first = 0
                    i.second = 0
                    i.third = 0
                    i.runs = i.runs + 4
