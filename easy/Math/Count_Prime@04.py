__author__ = "chirag"

"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        primes=[True for i in range(n+1)]
        p =2

        while p*p<=n:
            if primes[p]  :
                for i in range(p*p,n+1,p):
                    # print(",i",i)
                    primes[i]=False

            p+=1
        count=0
        # print(primes)
        for _bool in range(2,n):
            if  primes[_bool]:
                count+=1
        return count
