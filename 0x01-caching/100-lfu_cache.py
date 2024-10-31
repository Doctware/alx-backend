#!/usr/bin/env python3
"""This module implements a cache replacement system using LFU."""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching and implements
    an LFU caching system.
    """

    def __init__(self):
        """Initialize the cache with usage tracking structures."""
        super().__init__()
        self.usage_frequency = {}  # Tracks frequency of each key
        self.usage_tracker = []    # Tracks order for LRU among LFU items

    def put(self, key, item):
        """Assign item to self.cache_data for the given key.
        
        If either key or item is None, do nothing.
        If the number of items exceeds BaseCaching.MAX_ITEMS, remove
        the least frequently used item from the cache.
        """
        if key is None or item is None:
            return

        # Update frequency and usage order if key exists
        if key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_tracker.remove(key)
        else:
            # Add new key with initial frequency
            self.usage_frequency[key] = 1

        # Store item and update tracker
        self.cache_data[key] = item
        self.usage_tracker.append(key)

        # Enforce cache limit by removing least frequently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the minimum frequency
            min_frequency = min(self.usage_frequency.values())

            # Find all keys with this minimum frequency
            min_freq_keys = [
                k for k in self.usage_tracker
                if self.usage_frequency[k] == min_frequency
            ]

            # Remove the first (least recently used) among minimum frequency keys
            lfu_key = min_freq_keys[0]
            self.usage_tracker.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.usage_frequency[lfu_key]
            print("DISCARD:", lfu_key)

    def get(self, key):
        """Retrieve value associated with key in self.cache_data.
        
        If key is None or not in cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment frequency and update usage order for retrieved key
        self.usage_frequency[key] += 1
        self.usage_tracker.remove(key)
        self.usage_tracker.append(key)

        return self.cache_data[key]
