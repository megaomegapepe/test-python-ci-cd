def count_max(data: list[int]):
    max_: int = data[0]
    for number in data:
        if number > max_:
            max_ = number
    return max_


def count_min(numbers: list[int]):
    max_: int = numbers[0]
    for number in numbers:
        if number < max_:
            max_ = number
    return max_


def calculate_sum(numbers: list[int]):
    sum_: int = 0
    for number in numbers:
        sum_ += number
    return sum_


def calculate_multiplication(numbers: list[int]):
    multiplication_ = 1
    for number in numbers:
        multiplication_ *= number
    return multiplication_


if __name__ == '__main__':
    data = []
    with open("input.txt") as file:
        for line in file:
            data.append([int(x) for x in line.split()])

    try:
        integers = data.pop()
    except IndexError:
        print("File is empty")
        exit(0)
    print("Max: " + count_max(integers).__str__())
    print("Min: " + count_min(integers).__str__())
    print("Sum: " + calculate_sum(integers).__str__())
    print("Multiplication: " + calculate_multiplication(integers).__str__())
