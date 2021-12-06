with open('input/day2.txt', 'r', encoding='utf8') as file:
    policies_and_passwords = file.readlines()

valid_count1 = 0
valid_count2 = 0
for policy_and_password in policies_and_passwords:
    policy, password = policy_and_password.strip().split(': ')
    policy_range, policy_letter = policy.split(' ')
    policy_lo, policy_hi = map(int, policy_range.split('-'))
    if policy_lo <= password.count(policy_letter) <= policy_hi:
        valid_count1 += 1
    if (password[policy_lo-1] == policy_letter) ^ (password[policy_hi-1] == policy_letter):
        valid_count2 += 1
print(valid_count1)
print(valid_count2)