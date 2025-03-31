"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

https://leetcode.com/problems/time-based-key-value-store/description/
"""

from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.key_map = {}
        

    #lets do two solutions
    # assume time stamps are not in order and assume binary insert while inserting 

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # key with time stamp with map 
        if not key in self.key_map:
            self.key_map[key] = []
        
        self.key_map[key].append((timestamp,value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self.key_map:
            return ""

        tuples = self.key_map[key]
        left = 0
        right = len(tuples)-1
        result = ""

        # assuming sorted
        while left <= right:
            mid = (left + right) // 2
            if tuples[mid][0] <= timestamp:
                result = tuples[mid][1]
                left = mid + 1 
            else:
                right = mid - 1

        return result



# --------------------------------------------------
# ASssume time stamps are not sorted so we sort while inserting 

