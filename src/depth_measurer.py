
def read_inputs(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data


def calculate_depth_changes(measurements):
    count = 0

    for i in range(len(measurements) - 1):
        if measurements[i + 1] > measurements[i]:
            count = count + 1

    return count

if __name__ == "__main__":
    input_file = "/Users/brad/github/advent2021/input1.txt"
    measurements = read_inputs(input_file)
    count = calculate_depth_changes(measurements)
    print(count)
