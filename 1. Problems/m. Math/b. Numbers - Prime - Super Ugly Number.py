# LC 313. Super Ugly Number

'''
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        return self.optimized(n, primes)

    def naiveTLE(self, n: int, primes: List[int]) -> int:
        count = 1
        heap = [1]
        hset = set([1])

        while count <= n:
            num = heapq.heappop(heap)

            for p in primes:
                if not num * p in hset:
                    heapq.heappush(heap, num * p)
                    hset.add(num * p)

            count += 1

        return num

    def optimized(self, n: int, primes: List[int]) -> int:
        arr = [1]

        heap_arr = [(p, idx, 0) for idx, p in enumerate(primes)]
        heapq.heapify(heap_arr)

        while len(arr) < n:

            p_num, p_idx, arr_idx = heapq.heappop(heap_arr)

            if p_num > arr[-1]:
                arr.append(p_num)

            heapq.heappush(heap_arr, (primes[p_idx] * arr[arr_idx + 1], p_idx, arr_idx + 1))

        return arr[-1]
