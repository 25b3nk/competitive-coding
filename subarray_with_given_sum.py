"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1#

SOLVED!!!
"""

import time
import numpy as np


class Solution1:
    """First experiment
    """
    def solve(self, arr, n, s): 
        truth_table = []
        for i in range(len(arr) + 1):
            truth_table.append([False] * (s + 1))
            truth_table[i][0] = True

        print(np.array(truth_table))
        print(list(range(s + 1)))
        for i in range(1, len(arr) + 1):
            print(arr[i - 1], truth_table[i])
            for j in range(1, s+1):
                # if truth_table[i][j] is False and j >= arr[i - 1]:
                #     if truth_table[i - 1][j - arr[i - 1]] is True:
                #         truth_table[i][j] = True
                if j >= arr[i - 1]:
                    if truth_table[i  - 1][j - arr[i - 1]] is True:
                        truth_table[i][j] = True
                else:
                    truth_table[i][j] = False
            print(arr[i - 1], truth_table[i])
            print()
            if truth_table[i][s] is True:
                print("Index: {}".format(i - 1))
                break
            if i < len(arr):
                truth_table[i + 1] = truth_table[i].copy()
        end_index = i - 1
        final_sum = 0
        while final_sum < s:
            final_sum += arr[i - 1]
            i -= 1
        print(np.array(truth_table))
        if final_sum == s:
            return [i+1, end_index+1]
        else:
            return [-1, -1]


class Solution2:
    """Dynamic programming approach (Overkill!)
    """
    def solve(self, arr, n, s): 
        #Your code here
        truth_table = []
        for i in range(2):
            truth_table.append([False] * (s + 1))
        for i in range(2):
            truth_table[i][0] = True

        for i in range(1, len(arr) + 1):
            # print("\n" + str(arr[i - 1]), end=', ')
            truth_table[1] = [False] * (s + 1)
            truth_table[1][0] = True
            for j in range(1, s+1):
                if j < arr[i - 1]:
                    truth_table[1][j] = False
                else:
                    if truth_table[0][j - arr[i - 1]] == True:
                        # print(j, end=' ')
                        truth_table[1][j] = True
            # print(arr[i - 1], truth_table[1])
            if truth_table[1][s] == True:
                print("Index: {}".format(i - 1))
                break
            if i < len(arr):
                truth_table[0] = truth_table[1].copy()
        end_index = i - 1
        final_sum = 0
        while final_sum < s and i >= 1:
            final_sum += arr[i - 1]
            i -= 1
        if final_sum == s:
            return [i+1, end_index+1]
        else:
            return [-1, -1]


class Solution3:
    """Sliding window approach (Correct solution, after reading the hint)
    """
    def solve(self, arr, n, s): 
        #Your code here
        start_index = 1
        end_index = 1
        final_sum = 0
        for i in range(n + 1):
            while final_sum > s:
                final_sum -= arr[start_index - 1]
                start_index += 1
            if final_sum == s:
                break
            elif final_sum < s:
                if i < n:
                    final_sum += arr[i]
                    end_index = i + 1
                continue
        if final_sum == s:
            return [start_index, end_index]
        else:
            return [-1]


def find_solution(expected, **kwargs):
    print('\n----------------------------------------------')
    print("values: {} given sum: {}".format(kwargs['arr'], kwargs['s']))

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
    values = [[1,2,3,7,5], [1,2,3,4,5,6,7,8,9,10],
              [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134 ],
             ]
    given_sums = [12, 15, 468]
    expected = [[2, 4], [1, 5], [38, 42]]
    # values = [
    #     [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134 ]
    # ]
    # given_sums = [468]
    # expected = [[38, 42]]
    # assert len(values) == len(given_sums) == len(expected), "Make sure the number of elements in each list is equal"
    num_of_test_cases = 3  # len(values)
    for i in range(num_of_test_cases):
        input_dict = {
            'arr': values[i],
            'n': len(values[i]),
            's': given_sums[i]
        }
        find_solution(expected[i], **input_dict)
