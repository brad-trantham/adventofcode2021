
def read_inputs(input_file):
    with open(input_file, 'r') as f:
        data = f.read().splitlines()
    return data

def analyze_diagnostic(data):
    gamma = 0
    for d in data:


if __name__ == "__main__":
    input_file = "C:\\github\\adventofcode2021\\input3a_small.txt"
    input = read_inputs(input_file)
    print(input)