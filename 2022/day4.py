from aocd.models import Puzzle

d2 = Puzzle(year=2022, day=4)

def part_one():
    def solve(line):
        (a, b) = line.split(',')
        (a1, a2) = map(lambda v: int(v), a.split('-'))
        (b1, b2) = map(lambda v: int(v), b.split('-'))
        if a1 >= b1 and a2 <= b2:
            return True
        if b1 >= a1 and b2 <= a2:
            return True
        return False
    
    accum = 0
    for line in d2.input_data.split('\n'):
        overlaps = solve(line)
        if overlaps:
            accum += 1
    return accum

print(part_one())