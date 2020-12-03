database_pw = open('input_day2', 'r').readlines()

valid_pw = 0
valid_pw2 = 0

for row in database_pw:
    row = row.split()

    gp_num = row[0].split('-')
    gp_ltr = row[1].replace(':', '')

    min_num, max_num = int(gp_num[0]), int(gp_num[1])
    ltr_req = gp_ltr[0]
    pw_req = row[2]

    ltr_count = pw_req.count(ltr_req)

    if min_num <= ltr_count and ltr_count <= max_num:
        valid_pw += 1

    if pw_req[min_num - 1] == ltr_req or pw_req[max_num - 1] == ltr_req:
        if pw_req[min_num - 1] != pw_req[max_num-1]:
            valid_pw2 += 1

print('Day 2 Part 1: {}'.format(valid_pw))
print('Day 2 Part 2: {}'.format(valid_pw2))
