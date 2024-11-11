# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:17:07 2024

@author: priya
"""

class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        kMax = 1000
        primes = self._sieveEratosthenes(kMax)

        prevNum = 0
        for num in nums:
            # Make nums[i] the smallest as possible and still > nums[i - 1].
            i = bisect.bisect_left(primes, num - prevNum)
            if i > 0:
                num -= primes[i - 1]
            if num <= prevNum:
                return False
            prevNum = num

        return True

    def _sieveEratosthenes(self, n):
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return [i for i in range(n) if isPrime[i]]
