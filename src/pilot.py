def read_inputs(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    data = []
    for line in lines:
        l = line.split(" ")
        data.append([l[0], int(l[1])])

    return data


def pilot(input):
    horiz_pos = 0
    depth = 0

    for cmd in input:
        entry = cmd[0]
        if "forward" == entry:
            horiz_pos = horiz_pos + cmd[1]
        if "down" == entry:
            depth = depth + cmd[1]
        if "up" == entry:
            depth = depth - cmd[1]

    return horiz_pos, depth


if __name__ == "__main__":
    input_file = "/Users/brad/github/advent2021/input2.txt"
    input = read_inputs(input_file)
    print(input)
    horiz_pos, depth = pilot(input)
    print(horiz_pos, depth, horiz_pos*depth)