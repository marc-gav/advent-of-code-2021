import sys

def part1(input1):
    values = []
    # read input line by line
    for line in open(input1):
        values.append(int(line))

    res = sum([v2 - v1 > 0 for v1, v2 in zip(values, values[1:])])
    print(res)

def part2(input):
    values = []
    # read input line by line
    for line in open(input):
        values.append(int(line))
    
    # sum batches of 3
    batches = [v1 + v2 + v3 for v1, v2, v3 in zip(values, values[1:], values[2:])]

    res = sum([v2 - v1 > 0 for v1, v2 in zip(batches, batches[1:])])
    print(res)

# main
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input1 = sys.argv[1]
        part1(input1)
        part2(input1)
    else:
        print("Usage: ./firstproblem.py <input1>")