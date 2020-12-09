def sum_counts(file):
    count, count1 = 0, 0

    for group in file.read().split('\n\n'):
        pos_arg = map(set, group.split())
        count += len(set(group.replace('\n', '')))
        count1 += len(set.intersection(*pos_arg))
    return count, count1


if __name__ == '__main__':
    with open('input_day6', 'r') as passport_questions:
        count_pt1, count_pt2 = sum_counts(passport_questions)
        print('P1: {}'.format(count_pt1))
        print('P2: {}'.format(count_pt2))
