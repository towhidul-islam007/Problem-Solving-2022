""""
https://www.interviewbit.com/problems/hotel-bookings-possible/

Problem Description

A hotel manager has to process N advance bookings of rooms for the next season. 
His hotel has C rooms. Bookings contain an arrival date and a departure date. 

He wants to find out whether there are enough rooms in the hotel to satisfy the demand. 

Write a program that solves this problem in time O(N log N) .



Input Format
First argument is an integer array A containing arrival time of booking.

Second argument is an integer array B containing departure time of booking.

Third argument is an integer C denoting the count of rooms.

"""


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean

    def hotel(self, arrive, depart, K):
        booking_data = []
        for x, y in zip(arrive, depart):
            booking_data.append((x, 0))
            booking_data.append((y, 1))

        booking_data.sort(key=lambda x: (x[0], -x[1]))
        current_visitor = 0

        for item in booking_data:
            if item[1] == 0:
                current_visitor += 1
            else:
                current_visitor -= 1

            if current_visitor > K:
                return 0

        return 1
