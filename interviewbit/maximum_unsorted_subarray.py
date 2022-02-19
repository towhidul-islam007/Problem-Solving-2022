"""
    https://www.interviewbit.com/problems/maximum-unsorted-subarray/

    You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.

    Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.

    If A is already sorted, output -1.

    Example :

    Input 1:

    A = [1, 3, 2, 4, 5]

    Return: [1, 2]

    Input 2:

    A = [1, 2, 3, 4, 5]

    Return: [-1]

"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        a_sorted = sorted(A)

        sz = len(A)

        if sz <= 1:
            return [-1]

        l, r = 0, len(A) - 1
        while l + 1 < sz and A[l] == a_sorted[l]:
            l += 1

        while r - 1 >= 0 and A[r] == a_sorted[r]:
            r -= 1

        if l >= r:
            return [-1]

        return [l, r]
