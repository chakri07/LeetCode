from collections import defaultdict
class TimeMap:

    def __init__(self):
        # (time stamp , value)
        self.data_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # All the timestamps timestamp of set are strictly increasing.
        if key not in self.data_map:
            return ''
        
        time_list = self.data_map[key]

        if timestamp < time_list[0][0]:
            return ''

        left = 0 
        right = len(time_list) - 1

        ret_idx = -1 

        while left <= right:
            mid = (left + right)//2

            if time_list[mid][0] <= timestamp:
                left = mid + 1 
                ret_val = mid
            else:
                right = mid - 1

        return time_list[ret_val][1]

