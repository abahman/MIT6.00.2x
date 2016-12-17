import random

def oneTrial():
    '''
        Simulates one trial of drawing 3 balls out of a bucket containing
        3 red and 3 green balls. Balls are not replaced once
        drawn. Returns True if all three balls are the same color,
        False otherwise.
        '''
    balls = ['r']*4 + ['g']*4
    chosen_balls = random.sample(balls,3)
    if chosen_balls[0] == chosen_balls[1] == chosen_balls[2]:
        return True
    return False

def drawing_without_replacement_sim(numTrials):
    '''
        Runs numTrials trials of a Monte Carlo simulation
        of drawing 3 balls out of a bucket containing
        3 red and 3 green balls. Balls are not replaced once
        drawn. Returns the a decimal - the fraction of times 3
        balls of the same color were drawn.
        '''
    num_true = 0
    for trial in range(numTrials):
        if oneTrial() == True:
            num_true += 1
    return float(num_true)/(numTrials)

print (drawing_without_replacement_sim(50000))
