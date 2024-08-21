#!/usr/bin/env python3
""" Basic Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a class BasicCache that inherits from
    BaseCaching and is a caching system
    """
    def put(self, key, item):
        """Assign the item value to the key in cache_data dictionary."""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in cache_data dictionary."""
        # if key is None or key not in self.cache_data:
        #     return None
        return self.cache_data.get(key, None)
