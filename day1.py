with open('input/day1.txt', 'r', encoding='utf8') as file:
    expense_report = [int(number) for number in file.readlines()]

for i in range(len(expense_report)):
    for j in range(i+1,len(expense_report)):
        if expense_report[i] + expense_report[j] == 2020:
            answer1 = expense_report[i] * expense_report[j]
        for k in range(j+1,len(expense_report)):
            if expense_report[i] + expense_report[j] + expense_report[k] == 2020:
                answer2 = expense_report[i] * expense_report[j] * expense_report[k]

print(answer1)
print(answer2)