#!/usr/bin/env python3
""" Basic Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize the class by calling the parent constructor."""
        super().__init__()
        self.lru_order = []  # List to maintain the order of usage

    def put(self, key, item):
        """Add an item to the cache using LRU algorithm."""
        if key is None or item is None:
            return

        # If the key already exists, update the item and refresh its position
        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item and update the LRU order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """Return the value linked to key in cache_data."""
        if key is None or key not in self.cache_data:
            return None

        # Refresh the key's position in the LRU order
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data.get(key)
