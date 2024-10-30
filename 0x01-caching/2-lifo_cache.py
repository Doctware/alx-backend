#!/usr/bin/env python3
""" this module implement cache replacemet policies algorithim
    for LIFO i.e Stack """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ This inherit from Base caching to implement LIFO caching
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
        remove the latest item i.e perform LIFO
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest_item = self.order.pop(3)
            del self.cache_data[newest_item]
            print("DISCARD: {}".format(newest_item))

    def get(self, key):
        """
        Return thr value on self.cached_data linked to key
        if key is none then do nothing
        """
        return self.cache_data.get(key)
