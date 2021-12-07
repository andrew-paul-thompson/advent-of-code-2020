def get_row(boarding_pass):
    lo = 0
    hi = 127
    for c in boarding_pass[:7]:
        if c == 'F':
            hi -= (hi - lo) // 2 + 1
        else:
            lo += (hi - lo) // 2 + 1
    return lo

def get_column(boarding_pass):
    l = 0
    r = 7
    for c in boarding_pass[-3:]:
        if c == 'L':
            r -= (r - l) // 2 + 1
        else:
            l += (r - l) // 2 + 1
    return l


def get_seat_id(boarding_pass):
    return get_row(boarding_pass) * 8 + get_column(boarding_pass)

with open('input/day5.txt', 'r', encoding='utf8') as file:
    boarding_passes = [s.strip() for s in file.readlines()]

print(get_seat_id(max(boarding_passes,key=get_seat_id)))
seat_ids = sorted([get_seat_id(boarding_pass) for boarding_pass in boarding_passes])
for i in range(2, len(seat_ids)):
    if seat_ids[i-1] == seat_ids[i] - 2:
        print(seat_ids[i] - 1)