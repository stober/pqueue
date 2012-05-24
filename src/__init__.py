#! /usr/bin/env python
"""
Author: Jeremy M. Stober
Program: __INIT__.PY
Date: Thursday, May 24 2012
Description: Simple priority queue.
"""

import heapq as hq
import itertools

class pqueue:
    """
    A priority queue with fast member checking and variable tie
    breaking (LIFO or FIFO). Updated using the recipe from the heapq
    documentation.
    """

    def __init__(self, policy = "LIFO"):
        if policy == 'LIFO':
            self.step = -1
        else: # policy == 'FIFO'
            self.step = 1

        self.counter = itertools.count() # step only allowed in 2.7
        self.heap = []
        self.entries = {}
        self.removed_key = '<REMOVED>'

    def push(self, pri, key):
        if key in self.entries:
            self.remove(key)
        cnt = next(self.counter) * self.step
        entry = [pri, cnt, key]
        self.entries[key] = entry
        hq.heappush(self.heap, entry)

    def __contains__(self, key):
        return self.entries.has_key(key)

    def __len__(self):
        return len(self.entries)

    def clean(self):
        """
        Remove all heap entries marked for removal.
        """
        self.heap = [entry for entry in self.heap if entry[-1] != self.removed_key]

    def remove(self, key):
        entry = self.entries.pop(key)
        entry[-1] = self.removed_key

    def pop(self):
        pri, cnt, key = hq.heappop(self.heap)

        while key == self.removed_key:
            pri, cnt, key = hq.heappop(self.heap)

        del self.entries[key]
        return key



