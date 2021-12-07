with open('input/day6.txt', 'r', encoding='utf8') as file:
    groups = [group.strip().splitlines() for group in file.read().split('\n\n')]

print(sum(len(set(''.join(group))) for group in groups))
print(sum(1 if all(letter in person for person in group) else 0 for letter in 'abcdefghijklmnopqrstuvwxyz' for group in groups))
