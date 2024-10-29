#!/usr/bin/env python3
""" this module implement basic cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ The class Basic cach that inherit from Base Cahing
    """

    def __init__(self):
        """ Inialiazing
        """
        super().__init__()

    def put(self, key, item):
        """
        The put methos:

        assign to dictionary self.cached_data the item value
        for the key

        if key or item is noe the do nothing
        """
        self.cached_data[key] = item

    def get(self, key):
        """
        Return thr value on self.cached_data linked to key
        if key is none then do nothing
        """
        if key not in self.cached_data.keys():
            return None
        return self.cached_data[key]
