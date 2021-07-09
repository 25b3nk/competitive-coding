from time import time


class Solution:
    values = {
        0: 0,
        1: 1,
        2: 1
    }

    def fibo(self, n):
        """Compute nth fibonacci number and return within O(logn) time

        Args:
            n (int)

        Returns:
            int: nth Fibonacci number
        """
        if n in [0, 1, 2]:
            return self.values[n]
        m = 3
        k = 2
        f = self.values
        while True:
            # print("m: {}".format(m))
            # print("m: {}\tk: {}".format(m, k))
            # print("(m - k + 1): {}\t(m - k): {}".format(m - k + 1, m - k))
            if m not in self.values:
                if (m - k + 1) not in self.values:
                    self.fibo(m - k + 1)
                if (m - k) not in self.values:
                    self.fibo(m - k)
                if k not in self.values:
                    self.fibo(k)
                if (k - 1) not in self.values:
                    self.fibo(k - 1)
                f[m] = f[k]*f[m-k+1] + f[k-1]*f[m-k]
            if m == n:
                break
            if (m - 1) not in self.values:
                f[m - 1] = self.fibo(m - 1)
            k = m
            if 2*m - 1 > n:
                m = n
            else:
                m = 2*m - 1
        return f[n]

    def fibo2(self, n):
        """Compute nth fibonacci number and return within O(n) time

        Args:
            n (int)

        Returns:
            int: nth Fibonacci number
        """
        if n in [0, 1, 2]:
            return self.values[n]
        m = 3
        f = self.values
        while True:
            f[m] = f[m - 1] + f[m - 2]
            if m >= n:
                break
            m += 1
        return f[n]


if __name__ == "__main__":
    while True:
        n = int(input("Enter n: "))
        t1 = time()
        print("\n\tFibo(n): {}".format(Solution().fibo(n)))
        t2 = time()
        print("\tTotal time for O(logn): {} seconds".format(t2- t1))

        t1 = time()
        print("\n\tFibo(n): {}".format(Solution().fibo2(n)))
        t2 = time()
        print("\tTotal time O(n): {} seconds\n".format(t2- t1))
