"""_summary_

https://www.interviewbit.com/problems/noble-integer/

Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.



Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is found else return -1.

"""



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)

        if A and A[0] == 0:
            return 1

        for index, value in enumerate(A):
            if index == 0 or A[index - 1] == A[index]:
                continue
            if value == index:
                return 1

        return -1
