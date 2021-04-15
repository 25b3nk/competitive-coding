import time
from collections import defaultdict

# class Solution:
#     def solve(self, walks, target):
#         out_dict = {}
#         start_ind = 0
#         final_sum = 0
#         for val in walks:
#             end_ind = start_ind + val
#             if end_ind < start_ind:
#                 r = range(end_ind, start_ind)
#             else:
#                 r = range(start_ind, end_ind)
#             start_ind = end_ind
#             for i in r:
#                 if i not in out_dict:
#                     out_dict[i] = 0
#                 out_dict[i] += 1
#         for i in out_dict:
#             if out_dict[i] >= target:
#                 final_sum += 1
#         return final_sum


class Solution:
    def solve(self, nums, target):
        pos = 0
        jumps = defaultdict(int)
        print(jumps)
        for dist in nums:
            jumps[pos] += 1 if dist > 0 else -1
            jumps[pos + dist] -= 1 if dist > 0 else -1
            pos += dist
        print(jumps)
        lastpos = level = total = 0
        for pos, val in sorted(jumps.items()):
            if level >= target:
                total += pos - lastpos
            print("pos: {} val: {} level: {} total: {}".format(pos, val, level, total))
            level += val
            lastpos = pos
            print("level: {} lastpos: {}".format(level, lastpos))
        return total


if __name__ == '__main__':
    # walks = [2, -4, 1]
    # target = 2
    # output = 3
    walks = [[2, -4, 1], [-2, -2], [-2, 1], [100, -100], [1073741824, -1073741824]]
    target = [2, 1, 1, 2, 2]
    expected = [3, 4, 2, 100, 1073741824]
    assert len(walks) == len(target) == len(expected), "Make sure the number of elements in each list is equal"
    num_of_test_cases = len(walks)
    for i in range(num_of_test_cases):
        print('\n\n\n----------------------------------------------')
        print("Walks: {} target: {}".format(walks[i], target[i]))
        t1 = time.time()
        sol = Solution()
        answer = sol.solve(walks[i], target[i])
        t2 = time.time()
        print("\nAnswer: {} Expected: {}".format(answer, expected[i]), end='\t')
        if answer == expected[i]:
            print("Correct answer", end='\t')
        else:
            print("Wrong answer", end='\t')
        print("Total time: {:04f} ms".format((t2 - t1) * 1000))
