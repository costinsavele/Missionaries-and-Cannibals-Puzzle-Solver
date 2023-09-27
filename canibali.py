
def cross_river():
    missionaries_left = 3
    cannibals_left = 3
    boat_capacity = 2
    boat_position = 'left'
    
    while missionaries_left > 0 or cannibals_left > 0:
        if boat_position == 'left':
            if missionaries_left >= 2 and (cannibals_left < 2 or missionaries_left - 2 >= cannibals_left - 2):
                missionaries_left -= 2
                boat_position = 'right'
                print('Two missionaries cross the river to the right bank')
            elif cannibals_left >= 2 and (missionaries_left == 0 or missionaries_left >= cannibals_left):
                cannibals_left -= 2
                boat_position = 'right'
                print('Two cannibals cross the river to the right bank')
            elif missionaries_left >= 1 and cannibals_left >= 1 and (missionaries_left - 1 >= cannibals_left - 1):
                missionaries_left -= 1
                cannibals_left -= 1
                boat_position = 'right'
                print('One missionary and one cannibal cross the river to the right bank')
            else:
                print('No valid move from left bank')
                break
        else:
            if missionaries_left == 3:
                break
            if boat_capacity == 2:
                if missionaries_left < 2 or (cannibals_left >= 2 and cannibals_left <= missionaries_left - 2):
                    cannibals_left += 2
                    boat_position = 'left'
                    print('Two cannibals cross the river to the left bank')
                elif cannibals_left < 2 or (missionaries_left >= 2 and missionaries_left <= cannibals_left - 2):
                    missionaries_left += 2
                    boat_position = 'left'
                    print('Two missionaries cross the river to the left bank')
            else:
                if missionaries_left == 2 and cannibals_left == 1:
                    cannibals_left += 1
                    boat_position = 'left'
                    print('One cannibal returns to left bank')
                elif missionaries_left == 1 and cannibals_left == 2:
                    missionaries_left += 1
                    boat_position = 'left'
                    print('One missionary returns to left bank')
                else:
                    break

    print('All missionaries and cannibals have safely crossed the river to the other bank!')

    cross_river()