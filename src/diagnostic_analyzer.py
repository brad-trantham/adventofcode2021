
def read_inputs(input_file):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
        data = [int(d,2) for d in data]
    return data


def analyze_diagnostic(data):
    gamma = 0

    # bits in the answer
    bits = [0, 0, 0, 0, 0]

    # count of 1 values in each position
    ones_cnt = [0, 0, 0, 0, 0]

    # count the ones in each positiion
    for i in range(len(data)):
          if data[i] & 0b10000 == 16:
              ones_cnt[0] = ones_cnt[0] + 1
              print("1 in pos0 for",bin(data[i]))
          if data[i] & 0b01000 == 8:
              ones_cnt[1] = ones_cnt[1] + 1
          if data[i] & 0b00100 == 4:
              ones_cnt[2] = ones_cnt[2] + 1
          if data[i] & 0b00010 == 2:
              ones_cnt[3] = ones_cnt[3] + 1
          if data[i] & 0b00001 == 1:
              ones_cnt[4] = ones_cnt[4] + 1

    # flip the bits where more than half were 1
    threshold = len(data)/2
    for i in range(len(bits)):
        if ones_cnt[i] > threshold:
            bits[i] = 1

    bitstring = ""
    for b in bits:
        bitstring = bitstring + str(b)
    print(bitstring)

    gamma = int(bitstring,2)
    epsilon = gamma ^ 0b11111
    print(gamma, epsilon)
    return gamma * epsilon


if __name__ == "__main__":
    input_file = "/Users/brad/github/advent2021/input3a_small.txt"
    input = read_inputs(input_file)
    print(input)
    power = analyze_diagnostic(input)
    print(power)