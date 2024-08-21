#!/usr/bin/env python3
""" Basic Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This is a class FIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """This will initialize the parent class attribute"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign the item value to the key in cache_data dictionary."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Returns the value linked to key in cache_data dictionary."""
        return self.cache_data.get(key, None)
