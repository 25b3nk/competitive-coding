"""
https://binarysearch.com/room/Weekly-Contest-54-lcf4Qws6iH?questionsetIndex=2
"""
import numpy as np


class Solution:
    def solve(self, n, requests):
        m = []
        for i in range(2):
            m.append([0] * n)
        final_sum = 0
        is_blocked = False
        print(np.array(m))
        for val in requests:
            print("\n----------------------------------------")
            print(val)
            if (val[2] == 1):
                if m[not val[0]][val[1]] == 1:
                    is_blocked = True
                if val[1] > 0:
                    if (m[not val[0]][val[1] - 1] == 1):
                        is_blocked = True
                if val[1] < n - 1:
                    if (m[not val[0]][val[1] + 1] == 1):
                        is_blocked = True
            else:
                if m[val[0]][val[1]] == 1:
                    is_blocked = False
            m[val[0]][val[1]] = val[2]
            print(np.array(m))
            if (m[0][0] == 1 and m[1][0] == 1) \
                or (m[0][n-1] == 1 and m[1][n-1] == 1):    
                continue
            if not is_blocked:
                final_sum += 1
            print("Blocked?: {} Sum: {}".format(is_blocked, final_sum))
        return final_sum


if __name__ == '__main__':
    n = 6
    requests = [[1,1,1],[0,0,1],[0,1,1],[0,1,0]]
    sol = Solution().solve(n, requests)
    print(sol)
