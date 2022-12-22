from aocd.models import Puzzle

d2 = Puzzle(year=2022, day=5)

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def input():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def part_one():
    parsing_layout = True
    layout_lines = []

    for line in input():
        if len(line) == 0:
            parsing_layout = False
            break

        if parsing_layout:
            layout_lines.append(line)

    indices = layout_lines[len(layout_lines)-1]
    buckets = list(map(lambda x: int(x), filter(lambda x: len(x) != 0, indices.split(' '))))

    stacks = list(map(lambda _: [], indices))

    for layout in layout_lines[:len(layout_lines)-1]:
        parts = chunkIt(layout, len(buckets))
        def so(p):
            return p.strip().replace("[", "").replace("]", "")

        cols = list(map(lambda p: so(p), parts))
        
        i = 0
        for c in cols:
            if stacks[i] is None:
                stacks[i] = []
            if len(c) > 0:
                stacks[i].append(c)
            i += 1
    
    for line in d2.input_data.split('\n'):
        if not line.startswith("move"):
            continue
        p = line.split(' ')
        indices = [int(p) for p in [p[1], p[3], p[5]]]
        
        count = indices[0]
        fr = indices[1]
        to = indices[2]
        
        for i in range(0, count):
            o = stacks[fr-1].pop()
            stacks[to-1].insert(0, o)

    for c in stacks:
        print('...', c)

    return "".join([s[0] for s in stacks if len(s) > 0])

print(part_one())