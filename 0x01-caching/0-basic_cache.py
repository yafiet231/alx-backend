#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching
    and is a caching system:
    """
    def put(self, key, item):
        """adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
