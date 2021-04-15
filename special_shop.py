"""
https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/
"""


def solve1(N, A, B):
    min_sum = B * (N ** 2)
    ret_ind = 0
    for i in range(N + 1):
        curr_sum = A * (i ** 2) + B * ((N - i) ** 2)
        if curr_sum < min_sum:
            min_sum = curr_sum
    print(ret_ind, N, min_sum)
    return min_sum 


def solve2(N, A, B):
    """Final best solution

    Args:
        N (int): Total number of flower pots to buy
        A (int): Price of flower pot 1
        B (int): Price of flower pot 2

    Returns:
        int: Minimum price of the flower pots
    """
    print(N, A, B)
    x = (N * B) / (A + B)
    min_sum = A * (int(x) ** 2) + B * ((N - int(x)) ** 2)
    curr_sum = A * (int(x + 1) ** 2) + B * ((N - int(x + 1)) ** 2)
    if curr_sum < min_sum:
        min_sum = curr_sum
    return min_sum


fp = '/media/bhaskar/hdd1/projects/competitive-coding/data/705e7b9a8c0411e8.txt.clean.txt'
ans_fp = '/media/bhaskar/hdd1/projects/competitive-coding/data/705baa6e8c0411e8.txt'
ans_f = open(ans_fp)

with open(fp) as f:
    lines = f.read().split('\n')
    lines2 = ans_f.read().split('\n')
    T = int(lines[0].strip())
    for i in range(T):
        N, A, B = list(map(int, lines[i + 1].split(' ')))
        min_sum = solve3(N, A, B)
        # print(min_sum)
        if min_sum != int(lines2[i].strip()):
            print("Wrong answer")
            print(N, A, B)
            print(min_sum, lines2[i])
            break
    f.close()
ans_f.close()

# print(solve2(100, 100, 88))
