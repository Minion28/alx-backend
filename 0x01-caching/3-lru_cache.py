#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    inherit from BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """
        handle the elements
        """

        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """
        delete elements
        """

        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """
        add elements
        """

        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def put(self, key, item):
        """
        Assign to the dictionary
        Do nothing if item is none
        """

        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """
        Return value linked
        """

        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
