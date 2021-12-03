
def read_inputs():
    with open("input1.txt", 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data

if __name__ == "__main__":
    # get inputs
    measurements = read_inputs()

    count = 0

    for i in range(len(measurements) -1):
        if measurements[i+1] > measurements[i]:
            count = count + 1

    print(count)