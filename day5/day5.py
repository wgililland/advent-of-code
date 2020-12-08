seat_data = open('input_day5', 'r').read().splitlines()

seats = [int(seat.replace('F', '0').replace(
    'B', '1').replace('L', '0').replace('R', '1'), 2) for seat in seat_data]

seat_missing = set(range(min(seats), max(seats))) - set(seats)
print('The highest seat ID is: {}'.format(max(seats)))
print('My seat ID is: {}'.format(list(seat_missing)[0]))

'''
Alternate solutions for Part 2:

seat_missing = set(range(min(seats), max(seats))).difference(seats)

seat_missing = [seat_miss for seat_miss in range(
    min(seats), max(seats)) if seat_miss not in list(seats)]
'''
