"""
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

https://leetcode.com/problems/exclusive-time-of-functions/description
"""

from collections import defaultdict
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time_map = [0] * n
        # run_map = defaultdict(list)
        stack = []

        # transform input into needed way
        for i in range(len(logs)):
            log = logs[i]
            splitted = log.split(':')
            splitted[2] = int(splitted[2])
            logs[i] = splitted


        for process, action, curr_time in logs:
            if action == "start":
                if stack:
                    # if the action is start we push new task on the stack 
                    # and update the running time of the previous task
                    # and also update the pause time
                    prev_pro, prev_run_time, prev_start_time = stack[-1]
                    prev_run_time += curr_time - prev_start_time
                    stack[-1] = [prev_pro, prev_run_time, curr_time]
                
                # append the new process to stack
                stack.append([process,0,curr_time])
            else:
                # if actions is end then pop the previous task
                # caluclate the run time and update the arr
            
                prev_pro, prev_run_time, prev_start_time = stack.pop()
                prev_pro = int(prev_pro)
                time_map[prev_pro] += prev_run_time
                time_map[prev_pro] += curr_time - prev_start_time + 1
                if stack:
                    # update the start time of the earlier task
                    # as it will start to execute.
                    stack[-1][2] = curr_time + 1

        return time_map


