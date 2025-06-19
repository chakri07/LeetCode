"""

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.

https://leetcode.com/problems/my-calendar-i
"""

class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Manual binary search to find insertion point
        lo, hi = 0, len(self.bookings)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.bookings[mid][0] < start:
                lo = mid + 1
            else:
                hi = mid

        # Check with previous event
        if lo > 0 and self.bookings[lo - 1][1] > start:
            return False

        # Check with next event
        if lo < len(self.bookings) and self.bookings[lo][0] < end:
            return False

        # No conflict — insert at position lo
        self.bookings.insert(lo, (start, end))
        return True
