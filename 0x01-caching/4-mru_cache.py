#!/usr/bin/env python3
""" this module implement cache replacement sysytem for MRU """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ the class MRU cache thats inherit from Base caching """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_tracker = []

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is None then do nothing

        if lenght of cache data is > than BaseCahing.MAX_ITEMS
        remove the Mostused item i.e perform MRU algoritihm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_tracker.remove(key)

        self.cache_data[key] = item
        self.usage_tracker.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_item = self.usage_tracker.pop(-2)
            del self.cache_data[mru_item]
            print("DISCARD: {}".format(mru_item))

    def get(self, key):
        """
        returns the value in cache_data linked to key
        if key is None or not in cache_data return noen
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)
        return self.cache_data[key]
