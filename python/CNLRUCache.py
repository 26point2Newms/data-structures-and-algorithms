'''
Created on July 15, 2020

@author: charles newman
https://github.com/26point2Newms
'''

from collections import OrderedDict

class LRUCache(object):
    '''
    Implementation of a Least Recently Used Cache (LRU Cache) which discards
    the least recently used items first.
    '''

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        '''
        Returns the value associated with the key if found (cache hit) and 
        moves the key to the end to show it was recently used.
        Returns -1 if the key is not found (cache miss).
        '''
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        '''
        Adds/updates the value and moves the key to the end to show it was
        recently used. 
        Checks the length of the ordered dictionary against the capacity
        specified in the 'constructor'. 
        Remove the first key (the least recently used) if capacity is exceeded.
        '''
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
