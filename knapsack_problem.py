"""
https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/knapsack-with-large-weights-33a2433a/
"""

import time
import os


class Solution1:
    """Basic solution with full DP matrix
    """
    def solve(self, capacity, values, weights):
        m = []  # Contains the max value for the `i` items and capacity `w`
        n = len(values)
        for i in range(n + 1):
            m.append([0] * (capacity + 1))
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if weights[i - 1] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max(m[i - 1][j], m[i - 1][j - weights[i - 1]] + values[i-1])
        return m[n][capacity]


class Solution2:
    """Solution with current row and previous row only
    """
    def solve(self, capacity, values, weights):
        m = []  # Contains the max value for the `i` items and capacity `w`
        n = len(values)
        for i in range(2):
            m.append([0] * (capacity + 1))
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if weights[i - 1] > j:
                    m[1][j] = m[0][j]
                else:
                    m[1][j] = max(m[0][j], m[0][j - weights[i - 1]] + values[i-1])
            m[0] = m[1].copy()
        return m[1][capacity]


class Solution3:
    def solve(self, capacity, values, weights):
        m = []  # Contains the max value for the `i` items and capacity `w`
        n = len(values)
        v1 = [x for _, x in sorted(zip(weights, values), reverse=True)]
        w1 = sorted(weights, reverse=True)
        max_val = 0
        start_index = 1
        tmp_index = 1
        for i in range(2):
            m.append([0] * (capacity + 1))
        for i in range(1, n + 1):
            if i < n:
                start_index = max(w1[i-1], tmp_index - w1[i])
            else:
                start_index = w1[i-1]
            for j in range(start_index, capacity + 1):
                if w1[i - 1] > j:
                    m[1][j] = m[0][j]
                else:
                    m[1][j] = max(m[0][j], m[0][j - w1[i - 1]] + v1[i-1])
                if m[1][j] > max_val:
                    max_val = m[1][j]
                    tmp_index = j
            # print(m[1])
            m[0] = m[1].copy()
        return m[1][capacity]


def find_solution(expected, **kwargs):
    print('\n----------------------------------------------')
    print("capacity: {} values: {} weights: {}".format(kwargs['capacity'], kwargs['values'], kwargs['weights']))

    t1 = time.time()
    # Change the class name, according to which you wanna test
    answer = Solution3().solve(**kwargs)
    t2 = time.time()

    print("\nAnswer: {} Expected: {}".format(answer, expected), end='\t')
    if answer == expected:
        print("Correct answer", end='\t')
    else:
        print("Wrong answer", end='\t')
    print("Total time: {:04f} ms".format((t2 - t1) * 1000))
    print('----------------------------------------------')


if __name__ == '__main__':
    file_path = '/media/bhaskar/hdd1/projects/competitive-coding/knapsack/9abdb98c025011ea.txt.clean.txt'
    use_file = True
    if use_file:
        if not os.path.isfile(file_path):
            print("File not found, {}".format(file_path))
            exit(0)
        with open(file_path) as f:
            lines = f.read().split('\n')
            n, capacity = list(map(int, lines[0].strip().split(' ')))
            values = list(map(int, lines[1].strip().split(' ')))
            weights = list(map(int, lines[2].strip().split(' ')))
            expected = int(lines[3].strip())
            input_dict = {
                'capacity': capacity,
                'values': values,
                'weights': weights
            }
            find_solution(expected, **input_dict)
    else:
        values = [[10, 2, 1, 3], [10, 2, 1, 3]]
        weights = [[10, 5, 10, 10], [10, 5, 10, 10]]
        capacity = [20, 10]
        expected = [13, 10]
        assert len(values) == len(weights) == len(capacity), "Make sure the number of elements in each list is equal"
        num_of_test_cases = len(capacity)
        for i in range(num_of_test_cases):
            input_dict = {
                'capacity': capacity[i],
                'values': values[i],
                'weights': weights[i]
            }
            find_solution(expected[i], **input_dict)
