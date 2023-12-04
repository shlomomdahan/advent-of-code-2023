# import re
#
#
# def read_file(filename):
#     with open(filename, "r") as f:
#         return f.readlines()
#
#
# def check_game_possibilities(lines, red_cubes, green_cubes, blue_cubes):
#
#     sum_of_game_ids = 0
#
#     for line in lines:
#
#         game_id_pattern = r"Game (\d+)"
#         match = re.search(game_id_pattern, line)
#         game_number = match.group(1)
#
#         parts = line.split(';')
#
#         pattern = r"(\d+) (red|blue|green)"
#
#         is_possible = True
#
#         for part in parts:
#             matches = re.findall(pattern, part)
#
#             for number, color in matches:
#                 if color == "red" and int(number) > red_cubes:
#                     is_possible = False
#                 elif color == "green" and int(number) > green_cubes:
#                     is_possible = False
#                 elif color == "blue" and int(number) > blue_cubes:
#                     is_possible = False
#
#         if is_possible:
#             # print ("Game {} is possible".format(game_number))
#             sum_of_game_ids += int(game_number)
#
#     return sum_of_game_ids
#
#
# if __name__ == '__main__':
#     filename = "day2.txt"
#     lines = read_file(filename)
#     sum_of_all_game_ids = check_game_possibilities(lines, 12, 13, 14)
#     print(sum_of_all_game_ids)



#  pat 2

import re


def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def check_game_possibilities(lines, red_cubes, green_cubes, blue_cubes):

    power_set = 0

    for line in lines:

        game_id_pattern = r"Game (\d+)"
        match = re.search(game_id_pattern, line)
        game_number = match.group(1)

        parts = line.split(';')

        pattern = r"(\d+) (red|blue|green)"


        minimum_red = 0
        minimum_green = 0
        minimum_blue = 0

        for part in parts:
            matches = re.findall(pattern, part)

            for number, color in matches:
                if color == "red":
                    if int(number) > minimum_red:
                        minimum_red = int(number)
                elif color == "green":
                    if int(number) > minimum_green:
                        minimum_green = int(number)
                elif color == "blue":
                    if int(number) > minimum_blue:
                        minimum_blue = int(number)

        power_set += minimum_red * minimum_green * minimum_blue

    return power_set


if __name__ == '__main__':
    filename = "day2.txt"
    lines = read_file(filename)
    sum_of_all_game_ids = check_game_possibilities(lines, 12, 13, 14)
    print(sum_of_all_game_ids)