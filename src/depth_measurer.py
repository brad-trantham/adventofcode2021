
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

def calculate_window_changes(measurements):
    windows = {}
    count = 0

    window = 0
    for i in range(len(measurements)-2):
        sum = 0
        sum = sum + measurements[i]
        sum = sum + measurements[i+1]
        sum = sum + measurements[i+2]
        windows[window] = sum
        window = window + 1

    #print(windows)
    for i in range(len(windows)-1):
        if windows[i+1] > windows[i]:
            count = count + 1

    return count


if __name__ == "__main__":
    input_file = "/Users/brad/github/advent2021/input1.txt"
    measurements = read_inputs(input_file)
    count = calculate_window_changes(measurements)
    print(count)
