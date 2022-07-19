"""
Hackerrank Link: https://hr.gs/bbddc
"""

#!/bin/python3

import os

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def get_cost_to_point(start_point, end_point, snakes):
    num_of_rolls = 0
    while True:
        if start_point >= end_point:
            break
        start_point += 6
        while True:
            tmp = [(start_point == s[0] and s[0] != end_point) for s in snakes]
            if True in tmp:
                start_point -= 1
            else:
                break
        num_of_rolls += 1
    return num_of_rolls


def get_cost_to_point_using_snake(start_point, end_point, snakes):
    if start_point <= end_point:
        return get_cost_to_point(start_point, end_point, snakes)
    orig_start_point = start_point
    lowest_roll = 100
    for s in snakes:
        start_point = orig_start_point
        num_of_rolls = 0
        if s[0] >= start_point:
            num_of_rolls = get_cost_to_point(start_point, s[0], snakes)
            start_point = s[1]
            if s[1] < end_point:
                num_of_rolls += get_cost_to_point(s[1], end_point, snakes)
            else:
                num_of_rolls = 101
            if num_of_rolls < lowest_roll:
                lowest_roll = num_of_rolls
    return lowest_roll


def get_reward(start_point, ladder, snakes):
    cost_to_ladder_start = get_cost_to_point(start_point, ladder[0], snakes)
    ladder_reward = (ladder[1] - ladder[0]) / 6.0
    reward = ladder_reward - cost_to_ladder_start
    return reward


def get_the_next_ladder(ladders, start_point, snakes):
    # end_point = start_point
    chosen_ladders = []
    best_ladder_reward = 0
    best_ladder_ind = -1
    best_ladder_rolls = 0
    for ind, lad in enumerate(ladders):
        current_reward = 0
        if lad[1] > start_point:
            # Number of rolls to reach the end point on dice rolls
            num_of_direct_rolls = get_cost_to_point(start_point, lad[1], snakes)
            # Number of rolls to reach the end point on dice rolls + ladder
            num_of_rolls_with_ladder = get_cost_to_point_using_snake(start_point, lad[0], snakes)
            if num_of_direct_rolls > num_of_rolls_with_ladder:
                chosen_ladders.append(lad)
                current_reward = get_reward(start_point, lad, snakes)
                if current_reward > best_ladder_reward:
                    best_ladder_reward = current_reward
                    best_ladder_ind = ind
                    best_ladder_rolls = num_of_rolls_with_ladder
    return best_ladder_ind, best_ladder_rolls


def quickestWayUp(ladders, snakes):
    start_point = 1
    chosen_ladders = []
    total_rolls = 0
    while True:
        next_ladder_ind, curr_rolls = get_the_next_ladder(ladders, start_point, snakes)
        total_rolls += curr_rolls
        if next_ladder_ind == -1:
            break
        chosen_ladders.append(ladders[next_ladder_ind])
        start_point = ladders[next_ladder_ind][1]
        if (100 - start_point) <= 6:
            break
        ladders.pop(next_ladder_ind)
    total_rolls += get_cost_to_point_using_snake(start_point, 100, snakes)
    # start_point = 1
    # for lad in chosen_ladders:
    #     total_rolls += get_cost_to_point_using_snake(start_point, lad[0], snakes)
    #     start_point = lad[1]
    return total_rolls


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # uncomment statements with input() to take user input
    # t = int(input().strip())
    t = 1

    for t_itr in range(t):
        # n = int(input().strip())
        n = 3

        ladders = []

        # for _ in range(n):
        #     ladders.append(list(map(int, input().rstrip().split())))
        ladders = [[32, 62], [42, 68], [12, 98]]

        # m = int(input().strip())
        m = 7

        snakes = []

        # for _ in range(m):
        #     snakes.append(list(map(int, input().rstrip().split())))
        snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]

        result = quickestWayUp(ladders, snakes)
        print(f"Best way up: {result}")
        # fptr.write(str(result) + '\n')

    # fptr.close()
