#!/usr/bin/env python3
""" this module implement cache replacement plicies algorithim
    Using LRU """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ the LRU cache class thats inherit from Base caching """

    def __init__(self):
        """ inisialized
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is None then do nothing

        if lenght of cache data is > than BaseCahing.MAX_ITEMS
        remove the least resently used item i.e perform LRU
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.useage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_usage = self.usage_order.pop(0)
            del self.cache_data[least_usage]
            print("DISCARD: {}".format(least_usage))

    def get(self, key):
        """
        Return thr value on self.cached_data linked to key
        if key is none then do nothing
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
