from aocd.models import Puzzle
import string

d2 = Puzzle(year=2022, day=3)

def part_one():
    def p(x):
        if x in string.ascii_uppercase:
            return string.ascii_uppercase.index(x) + 26
        return string.ascii_lowercase.index(x)
    
    def solve(line):
        a = line[:len(line)//2]
        b = line[len(line)//2:]
        
        # 1. intersection of chars of a and b
        i = set([(p(i) + 1) for i in a if i in b])
        return sum(i)
    
    accum = 0
    for line in d2.input_data.split('\n'):
        accum += solve(line)

    return accum

print(part_one())