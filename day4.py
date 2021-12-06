import re

def is_valid1(card_data):
    return all(field in card_data.keys() for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid2(card_data):
    valid = True
    valid = valid and card_data['byr'].isnumeric() and 1920 <= int(card_data['byr']) <= 2002
    valid = valid and card_data['iyr'].isnumeric() and 2010 <= int(card_data['iyr']) <= 2020
    valid = valid and card_data['eyr'].isnumeric() and 2020 <= int(card_data['eyr']) <= 2030
    if card_data['hgt'][:-2].isnumeric():
        hgt = int(card_data['hgt'][:-2])
        if card_data['hgt'][-2:] == 'cm':
            valid = valid and 150 <= hgt <= 193
        elif card_data['hgt'][-2:] == 'in':
            valid = valid and 59 <= hgt <= 76
        else:
            valid = False
    else:
        valid = False
    valid = valid and card_data['hcl'][0] == '#' and len(card_data['hcl']) == 7 and all(c in '0123456789abcdef' for c in card_data['hcl'][1:])
    valid = valid and card_data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = valid and len(card_data['pid']) == 9 and card_data['pid'].isnumeric()
    return valid

with open('input/day4.txt', 'r', encoding='utf8') as file:
    cards = [s.strip() for s in file.read().split('\n\n')]

valid_count1 = 0
valid_count2 = 0
for card in cards:
    card_data = dict([pair.split(':') for pair in re.split('[\n ]', card)])
    if is_valid1(card_data):
        valid_count1 += 1
        if is_valid2(card_data):
            valid_count2 += 1
print(valid_count1)
print(valid_count2)