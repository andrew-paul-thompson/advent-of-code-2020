from functools import reduce
from operator import mul

with open('input/day3.txt', 'r', encoding='utf8') as file:
    tree_map = [line.strip() for line in file.readlines()]

def calculate_tree_encounters_for_slope(slope_x, slope_y):
    pos_x, pos_y = 0, 0
    tree_encounters = 0
    while pos_y < len(tree_map):
        if tree_map[pos_y][pos_x] == '#':
            tree_encounters += 1
        pos_x = (pos_x + slope_x) % len(tree_map[0])
        pos_y += slope_y
    return tree_encounters

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
answers = [calculate_tree_encounters_for_slope(*slope) for slope in slopes]
print(answers[1])
print(reduce(mul, answers))