
def read_inputs():
    with open("input1.txt", 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data


def calculate_depth_changes(measurements):
    count = 0

    for i in range(len(measurements) - 1):
        if measurements[i + 1] > measurements[i]:
            count = count + 1

    print(count)

if __name__ == "__main__":
    measurements = read_inputs()
    calculate_depth_changes(measurements)
