"""
    https://www.interviewbit.com/problems/n3-repeat-number/

    You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
    If so, return the integer. If not, return -1.

    If there are multiple solutions, return any one.

    Example:

    Input: [1 2 3 1 1]
    Output: 1 
    1 occurs 3 times which is more than 5/3 times.

"""

import sys


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        possible_candidate_1 = possible_candidate_2 = sys.maxsize
        candidate_1_freq = candidate_2_freq = 0

        for item in A:
            if item == possible_candidate_1:
                candidate_1_freq += 1
            elif item == possible_candidate_2:
                candidate_2_freq += 1
            elif candidate_1_freq == 0:
                possible_candidate_1 = item
                candidate_1_freq = 1
            elif candidate_2_freq == 0:
                possible_candidate_2 = item
                candidate_2_freq = 1
            else:
                candidate_1_freq -= 1
                candidate_2_freq -= 1

        candidate_1_freq = candidate_2_freq = 0
        for item in A:
            if item == possible_candidate_1:
                candidate_1_freq += 1
            elif item == possible_candidate_2:
                candidate_2_freq += 1

        if candidate_1_freq > len(A) / 3:
            return possible_candidate_1

        if candidate_2_freq > len(A) / 3:
            return possible_candidate_2

        return -1
