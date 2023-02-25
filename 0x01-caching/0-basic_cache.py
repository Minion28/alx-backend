#!/usr/bin/env python3
"""
BasicCache that inherits from BasicCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a caching system.
    """
    def put(self, key, item):
        """
        do nothing if item is none.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        return none if key does not exist.
        """
        return self.cache_data.get(key, None)
