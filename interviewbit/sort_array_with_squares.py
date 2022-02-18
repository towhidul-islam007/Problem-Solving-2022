"""_summary_
    https://www.interviewbit.com/problems/sort-array-with-squares/

    Problem Description

    Given a sorted array A containing N integers both positive and negative.

    You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

    Try to this in O(N) time.


    Problem Constraints
    1 <= N <= 10^5.

    -10^3 <= A[i] <= 10^3
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        has_square = [0] * 1000001
        for item in A:
            has_square[item * item] += 1

        squares = []
        for index, item in enumerate(has_square):
            if item > 0:
                squares.extend([index] * item)

        return squares
