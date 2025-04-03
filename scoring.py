def new_highscore(score, old_highscore):
    print(f'You set a new HighScore of {score}!')
    print(f'old highscore was {old_highscore}') 

    f = open("highscore.txt", "w")
    f.write(f'{score}')

def set_score(score):
    f = open("highscore.txt", "r")
    highscore = f.read()
    f.close()

    if highscore.isdigit():
        if score > int(highscore):
            new_highscore(score, int(highscore))
        else:
            print(highscore)
    else:
        new_highscore(score, 0)