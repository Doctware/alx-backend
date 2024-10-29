#!/usr/bin/env python3
""" this module implement cache replacemet policies algorithim
    for FIFO i.e Queue """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ This inherit from Base caching to implement fifo caching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is None then do nothing

        if lenght of cache data is > than BaseCahing.MAX_ITEMS
        remove the oldest item i.e perform FIFO
        """
        if key is None and item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_item = self.order.pop(0)
            del self.cache_data[oldest_item]
            print("DISCARD: {}".format(oldest_item))

    def get(self, key):
        """
        Return thr value on self.cached_data linked to key
        if key is none then do nothing
        """
        return self.cache_data.get(key)
