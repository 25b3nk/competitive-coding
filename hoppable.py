"""
https://binarysearch.com/problems/Hoppable
"""

import time
import os


class Solution1:
    def solve(self, nums):
        tt = []
        n = len(nums)
        if (n == 1):
            return True
        for i in range(2):
            tt.append([False] * (n + 1))
            tt[i][0] = True

        for i in range(n):
            for j in range(1, n + 1):
                if j <= nums[i]:
                    tt[1][j] = True
                else:
                    if tt[0][j - nums[i]] == True:
                        tt[1][j] = True
            if tt[1][n] == True:
                return True
            tt[0] = tt[1].copy()
        return False


class Solution2:
    def solve(self, nums):
        tt = []
        n = len(nums)
        if (n == 1):
            return True
        for i in range(2):
            tt.append([False] * (n))
            tt[i][0] = True

        for i in range(n):
            print(nums[i], tt[1])
            for j in range(i, n):
                if not tt[0][i] == True:
                    return False
                if j <= i + nums[i]:
                    tt[1][j] = True
                else:
                    break
            print(nums[i], tt[1])
            if tt[1][n - 1] == True:
                return True
            tt[0] = tt[1].copy()
        return False


def find_solution(expected, **kwargs):
    print('\n----------------------------------------------')
    print("values: {}".format(kwargs['nums']))

    t1 = time.time()
    # Change the class name, according to which you wanna test
    answer = Solution2().solve(**kwargs)
    t2 = time.time()

    print("\nAnswer: {} Expected: {}".format(answer, expected), end='\t')
    if answer == expected:
        print("Correct answer", end='\t')
    else:
        print("Wrong answer", end='\t')
    print("Total time: {:04f} ms".format((t2 - t1) * 1000))
    print('----------------------------------------------')


if __name__ == '__main__':
    file_path = ''
    use_file = False
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
        values = [[2,4,0,1,0], [0], [1, 0], [0, 1], [1, 1, 0], [4, 0, 5, 0, 1, 0, 0, 10, 0, 0, 1]]
        expected = [True, True, True, False, True, True]
        # assert len(values) == len(expected), "Make sure the number of elements in each list is equal"
        num_of_test_cases = len(values)
        for i in range(num_of_test_cases):
            input_dict = {
                'nums': values[i]
            }
            find_solution(expected[i], **input_dict)

