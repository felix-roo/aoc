from aocd.models import Puzzle

d2 = Puzzle(year=2022, day=2)

# a = rock
# b = paper
# c = scissors

# x = rock
# y = paper
# z = scissors

# point system:
# rock = 1
# paper = 2
# scissors = 3
# lose = 0, draw = 3, win = 6

# total_score = sum of all scores for each round
# round_score = shape + outcome

Rock = 1
Paper = 2
Scissors = 3

def mtp(input):
    opts = {
        'A': Rock,
        'B': Paper,
        'C': Scissors,
        'X': Rock,
        'Y': Paper,
        'Z': Scissors,
    }
    if input not in opts:
        print('no such option ', input)
        exit(-1)
    return (opts[input])

Lose = 0
Draw = 3
Win = 6

def cw(theirs, mine):
    relationships = {
        Rock: Scissors,
        Scissors: Paper,
        Paper: Rock,
    }
    if theirs == mine:
        return Draw
    
    defeated_by = relationships[theirs]
    if mine == defeated_by:
        return Lose
    
    return Win

ts = 0

for line in d2.input_data.split('\n'):
    inputs = line.split(' ')
    (t, m) = inputs
    result = cw(mtp(t), mtp(m)) + mtp(m)
    ts += result

print('total score:', ts)