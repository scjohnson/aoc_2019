# /usr/bin/env python


def read_data(data_line):
    line = data_line.split(',')
    return [int(x) for x in line]


def calculate(data):
    index = 0
    while True:
        if data[index] == 99:
            return data
        elif data[index] == 1:
            data[data[index+3]] = data[data[index+1]]+data[data[index+2]]
        elif data[index] == 2:
            data[data[index+3]] = data[data[index+1]]*data[data[index+2]]
        else:
            print("ERROR")
            return
        index += 4


def solution_1(file_name):
    f = open(file_name)
    line = f.readline()
    data = read_data(line)
    data[1] = 12
    data[2] = 2
    data = calculate(data)
    return data[0]


def solution_2(file_name):
    f = open(file_name)
    line = f.readline()
    for i in range(0, 100, 1):
        for j in range(0, 100, 1):
            data = read_data(line)
            data[1] = i
            data[2] = j
            data = calculate(data)
            if data[0] == 19690720:
                return i*100+j
    print("FAIL")


if __name__ == "__main__":
    print(calculate(read_data("1,0,0,0,99")))
    print(calculate(read_data("2,3,0,3,99")))
    print(calculate(read_data("2,4,4,5,99,0")))
    print(calculate(read_data("1,1,1,4,99,5,6,0,99")))
    print("Solution 1: ", solution_1("input.txt"))
    print("Solution 2: ", solution_2("input.txt"))
