def breaking_rules():
    return '''Breaking rules:\n
1- If cue stick slips then the player is allowed a re-break\n
2- If cue stick does not slip then a player must execute a legal
break: the breaker must either (1) pocket a ball,or (2) drive at
least four numbered balls to the rail.If he fails to make a legal
break, it is a foul, and the incoming player has the option of
(1) accepting the table in position and shooting, or (2) having
the balls re-racked and having the option of shooting the opening
break himself or allowing the offending player to re-break.\n
3- If a player scratches on a legal break shot, (1) all balls
pocketed remain pocketed (exception is the 8 ball (4th rule)),
(2) it is a foul, (3) the table is open.\n
4- If 8 ball is pocketed during a break then the breaker may ask
for a re-rack or have the 8-ball spotted and continue shooting.
If the breaker scratches while pocketing the 8-ball on the break,
the incoming player has the option of a re-rack or having the 8-ball
spotted and begin shooting with ball in hand behind the spotter.'''


def open_table():
    return '''Open table:\n
1- The table is open after the break, even if a ball goes in.\n
2- The table remains open if, while the table is open, the player
scratches.'''

def combination_shots():
    return '''Combination Shots:\n
1- When the table is open, any combination is allowed, including solid
with stripes or vice versa. However, if in an open table, the player
uses the 8-ball as the first ball in the combination, then even though
it is not a foul, the incoming player continues shooting without moving
the white ball and with the table still open.\n
2- Are allowed but the 8-ball cannot be contacted first, except when the
table is open'''

def common_fouls():
    return '''Common Fouls:\n
1- Failing to make a legal shot: hitting your object ball first\n
2- Scratching the cue ball or driving it off the table\n
3- Failing to have at least one foot on the ground while shooting\n
4- Driving a numbered ball off the table\n
5- Touching, moving or changing the path of any object ball\n
6- Cue stick touching the cue ball more than once on a shot\n
7- Cue stick touching the cue ball while the cue ball is making contact
with another object ball\n
8- Drag shots\n
9- Shooting while an object ball is still moving/spinning\n
10- Failing to have the cue stick in hand while aligning the shot\n
11- Playing out of turn\n
12- Unsportsmanlike conduct such as distracting the opponent\n
13- If a foul is not stated here then it is not a foul'''

def foul_penalty():
    return '''Foul Penalty:\n
1- If a foul is committed then the opposing player gets the cue ball
in hand'''

def Illegally_Pocketed_Balls():
    return '''Illegally Pocketed Balls:\n
1- All illegally pocketed balls (balls that are pocketed as a result
of a foul) are not to be taken out'''

def Playing_the_8_ball():
    return '''Playing the 8-ball:\n
1-  When shooting at the 8-ball, a scratch or foul is not loss of
game if the 8-ball is not pocketed or jumped from the table.
Incoming player has cue ball in hand. Note: A combination shot
can never be used to legally pocket the 8-ball.'''

def Loss_of_Game():
    return '''Loss of Game:\n
1-Fouls when pocketing the 8-ball, such as scratching while making
the 8-ball (exception: 8-Ball Pocketed On The Break).\n
2- Pockets the 8-ball on the same stroke as the last of his group
of balls.\n
3- Jumps the 8-ball off the table at any time\n
4- Pockets the 8-ball in a pocket other than the one designated.
(Note: If the pocket is obvious then it need not be called; however,
the opponent still has the right to ask)\n
5- Pockets the 8-ball when it is not the legal object ball.'''

def main():
    print('Welcome to the 8-Ball Pool Rulebook for CRY BABIES!\n')
    answer = int(input('''Press 1 for BREAKING RULES\n
Press 2 for OPEN TABLE RULES\n
Press 3 for COMBINATION SHOT RULES\n
Press 4 for COMMON FOULS\n
Press 5 for FOUL PENALTY\n
Press 6 for RULES FOR ILLEGALLY POCKETED BALLS\n
Press 7 for RULES FOR PLAYING THE 8-BALL\n
Press 8 for LOSS OF GAME RULES\n
YOUR CHOICE: '''))
    print()
    if answer == 1:
        print(breaking_rules())
    elif answer == 2:
        print(open_table())
    elif answer == 3:
        print(combination_shots())
    elif answer == 4:
        print(common_fouls())
    elif answer == 5:
        print(foul_penalty())
    elif answer == 6:
        print(Illegally_Pocketed_Balls())
    elif answer == 7:
        print(Playing_the_8_ball())
    else:
        print(Loss_of_Game())

main()




