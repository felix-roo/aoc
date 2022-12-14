from aocd.models import Puzzle

d1 = Puzzle(year=2022, day=1)

def part_one():
    calorie_accum = 0
    largest_accum_calorie = 0

    for line in d1.input_data.split('\n'):
        if line == '':
            calorie_accum = 0
            continue
        
        calorie_accum += int(line)
        largest_accum_calorie = max(calorie_accum, largest_accum_calorie)
    
    return largest_accum_calorie

def part_two():
    calorie_accum = 0
    ca = []

    for line in d1.input_data.split('\n'):
        if line == '':
            ca.append(calorie_accum)
            calorie_accum = 0
            continue

        calorie_accum += int(line)
    
    ca = sorted(ca)
    
    return ca.pop() + ca.pop() + ca.pop()

print(part_one())
print(part_two())