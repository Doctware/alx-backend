#!/usr/bin/env python3
""" this module implement basic cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ The class Basic cach that inherit from Base Cahing
    """

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is noe the do nothing
        """
        if key is not None and item is not None:
            self.cached_data[key] = item

    def get(self, key):
        """
        Return thr value on self.cached_data linked to key
        if key is none then do nothing
        """
        return self.cached_data.get(key)
