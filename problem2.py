import sys

"""
forward 3
down 4
forward 3
up 4
down 4
"""

def part1(input):
    position = {
        'horizontal': 0,
        'vertical': 0
    }
    for line in input:
        direction, distance = line.split(' ')
        if direction == 'up':
            position['vertical'] -= int(distance)
        if direction == 'down':
            position['vertical'] += int(distance)
        if direction == 'forward':
            position['horizontal'] += int(distance)
        
    return position['horizontal'] * position['vertical']

def part2(input):
    position = {
        'horizontal': 0,
        'aim': 0,
        'depth': 0
    }
    for line in input:
        direction, distance = line.split(' ')
        if direction == 'up':
            position['aim'] -= int(distance)
        if direction == 'down':
            position['aim'] += int(distance)
        if direction == 'forward':
            position['horizontal'] += int(distance)
            position['depth'] += position['aim'] * int(distance)
        
    return position['horizontal'] * position['depth']

# main
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = sys.argv[1]
        input_text = [line.strip() for line in open(input)]
        print(part1(input_text))
        print(part2(input_text))
    else:
        print("Usage: ./firstproblem.py <input1>")