from functools import wraps


# cache decorlator
def cache(func):
    data = dict()
    
    def param_hash(*args, **kwargs):
        return hash(str(args) + str(kwargs))
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = param_hash(*args, **kwargs)
        if key not in data:
            data[key] = func(*args, **kwargs)
        return data[key] 
    
    return wrapper


# timer
from datetime import datetime

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Success. {end-start} taken for {func.__name__}')
        return result
    return wrapper


# sorted list
from bisect import bisect_left, bisect_right
from collections.abc import Container

class SortedList(Container):
	def __init__(self, data=None):
		self.data = sorted(data) if data else []

	def __setitem__(self, key, value):
		raise NotImplementedError

	def __contains__(self, value):
		return bisect_right(self.data, value) > 0

	def add(self, value):
		"""Add an item to this list."""
		index = bisect_right(self.data, value)
		self.data.insert(index, value)

	def pop(self, index=None):
		"""Remove and return item at index (default last).
		Raise IndexError if this list is empty."""
		if index is None:
			index = len(self.data) - 1
		return self.data.pop(index)

	def remove(self, value):
		"""Remove first occurrence of value.
		Raise ValueError if not found."""
		index = self.index(value)
		del self[index]

	def clear(self):
		"""Remove all items from this list."""
		self.data = []

	def copy(self):
		"""Return a shallow copy of this list."""
		return self.__class__(self.data[:])

	def count(self, value):
		"""Return number of occurrences of value."""
		i = bisect_left(self.data, value)
		j = bisect_right(self.data, value)
		return j - i

	def index(self, value, start=0, stop=None):
		"""Return first index of value.
		Raise ValueError if not found."""
		if stop is None:
			stop = len(self.data)
		index = bisect_left(self.data, value, start, stop)
		if index != len(self.data) and self.data[index] == value:
			return index
		raise ValueError


