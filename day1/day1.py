import re


# def openFile(filename):
#     file = open(filename, "r")
#     return file
#
# def sumAllValues(file):
#
#     sum = 0
#
#     for line in file:
#         listOfNumbers = []
#         for value in line:
#             if value.isdigit():
#                 listOfNumbers.append(value)
#
#         if len(listOfNumbers) == 0:
#             continue
#         elif len(listOfNumbers) == 1:
#             sum += int(listOfNumbers[0])*10 + int(listOfNumbers[0])
#         else:
#             sum += int(listOfNumbers[0])*10 + int(listOfNumbers[-1])
#
#
#     return sum


# file = openFile("day1.txt")
# sum = sumAllValues(file)
# print(sum)

# ________________________________

# part 2

def readFile(filename):
    with open(filename, "r") as f:
        return f.readlines()


def extractNumbers(lines):

    pattern = r"(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
    txtToNum = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    sum = 0
    for line in lines:
        digits = re.findall(fr"{pattern}", line)
        print(digits)

        if len(digits) == 0:
            continue
        else:
            # Convert text to numbers if needed
            converted_digits = [txtToNum[d] if d in txtToNum else int(d) for d in digits]
            firstDigit = converted_digits[0]
            lastDigit = converted_digits[-1]
            sum += firstDigit*10 + lastDigit

    return sum


if __name__ == "__main__":
    lines = readFile("day1/day1.txt")
    sum = extractNumbers(lines)
    print(sum)
