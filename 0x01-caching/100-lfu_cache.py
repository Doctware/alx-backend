#!/usr/bin/env python3
""" LFU Cache module implementing LFU with LRU as tiebreaker """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements
    an LFU caching system with LRU tiebreaker.
    """

    def __init__(self):
        """ Initialize the cache with usage tracking structures. """
        super().__init__()
        self.usage_frequency = {}  # Tracks frequency of each key
        self.usage_tracker = []    # Tracks order for LRU among LFU items

    def put(self, key, item):
        """ Assign item to self.cache_data for the given key.

        If either key or item is None, do nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, remove
        the least frequently used item from the cache, with an LRU
        tiebreaker for items with the same frequency.
        """
        if key is None or item is None:
            return

        # If the key already exists, update its value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            # Move key to end of usage tracker to reflect recent use
            self.usage_tracker.remove(key)
            self.usage_tracker.append(key)
        else:
            # Add new key and initialize its frequency
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the keys with the lowest frequency
                min_frequency = min(self.usage_frequency.values())
                min_freq_keys = [
                    k for k in self.usage_tracker
                    if self.usage_frequency[k] == min_frequency
                ]
                # Use LRU order by removing the first in min_freq_keys
                lfu_key = min_freq_keys[0]
                self.usage_tracker.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Insert the new item
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_tracker.append(key)

    def get(self, key):
        """ Retrieve value associated with key in self.cache_data.

        If key is None or not in cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment frequency and update usage order for retrieved key
        self.usage_frequency[key] += 1
        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)

        return self.cache_data[key]
