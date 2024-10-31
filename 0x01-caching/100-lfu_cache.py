#!/usr/bin/env python3
""" this module implement cache replacement sysytem for LFU """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ the class MRU cache thats inherit from Base caching """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_frequency = {}
        self.usage_tracker = []

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is None then do nothing

        if lenght of cache data is > than BaseCahing.MAX_ITEMS
        remove the leat frquently item i.e perform LFU algorithim
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_tracker.remove(key)
        else:
            self.usage_frequency[key] = 1

        self.cache_data[key] = item
        self.usage_tracker.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # find the minimum frequency among current items
            min_frequency = min(self.usage_frequency.values())

            min_freq_keys = [
                    k
                    for k in self.usage_tracker
                    if self.usage_frequency[k] == min_frequency
            ]

            lfu_key = min_freq_keys[0]
            self.usage_tracker.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.usage_frequency[lfu_key]
            print("DISCARD: {}".format(lfu_key))

    def get(self, key):
        """
        returns the value in cache_data linked to key
        if key is None or not in cache_data return noen
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)

        return self.cache_data[key]
