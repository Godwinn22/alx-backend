#!/usr/bin/env python3
""" Basic Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """This is a class LIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assign the item value to the key in cache_data dictionary."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.keys.remove(key)
                else:
                    print("DISCARD: {}".format(self.keys[-1]))
                    del self.cache_data[self.keys[-1]]
                    self.keys.pop(-1)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Returns the value linked to key in cache_data dictionary."""
        return self.cache_data.get(key, None)
