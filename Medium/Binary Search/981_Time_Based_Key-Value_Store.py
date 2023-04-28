"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""

class TimeMap(object):

    def __init__(self):
        self.store = {} # create a hashmap where the key value is going to be a string and the value of the hashmap will be a list of lists key : list of [value, timestamp]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = [] # if the key is not already in the store then set it to an empty list
        self.store[key].append([value, timestamp]) # add the value and timestamp factors to the key
        

    def get(self, key, timestamp):
        res = "" # if the key doesn't exist in the store then return an empty string
        values = self.store.get(key, []) # if the function gets something it will return the list, if it doesn't then it will default to returning an empty list

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # if the middle value timestamp is less than or equal to the actual timestamp
                res = values[m][0] # this value[m] is the closest we have seen so far
                l = m + 1 # search to the right portion to see if we get any closer to the result
            else: # if it is greater than the timestamp then that is not allowed
                r = m - 1 # search to the left portion
            
        return res
