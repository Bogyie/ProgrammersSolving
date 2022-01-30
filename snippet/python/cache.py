from typing import Callable, Iterable, Optional
from bisect import bisect_left, bisect_right
from time import time


class SortedCollection(object):
    def __init__(self, iterable:Iterable=tuple(), key:Optional[Callable]=None):
        self._given_key = key
        key = (lambda x: x) if key is None else key
        decorated = sorted((key(item), item) for item in iterable)
        self._keys = [k for k, item in decorated]
        self._items = [item for k, item in decorated]
        self._key = key

    def _getkey(self) -> Callable:
        return self._key

    def _setkey(self, key:Optional[Callable]) -> None:
        if key is not self._key:
            self.__init__(self._items, key=key)

    def _delkey(self):
        self._setkey(None)

    key = property(_getkey, _setkey, _delkey, 'key function')

    def clear(self):
        self.__init__([], self._key)

    def copy(self):
        return self.__class__(self, self._key)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, i):
        return self._items[i]

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __repr__(self):
        return '%s(%r, key=%s)' % (
            self.__class__.__name__,
            self._items,
            getattr(self._given_key, '__name__', repr(self._given_key))
        )

    def __reduce__(self):
        return self.__class__, (self._items, self._given_key)

    def __contains__(self, item):
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self._items[i:j]

    def index(self, item):
        'Find the position of an item.  Raise ValueError if not found.'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self._items[i:j].index(item) + i

    def count(self, item):
        'Return number of occurrences of item'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self._items[i:j].count(item)

    def appeend(self, item):
        k = self._key(item)
        if self._keys[-1] > k:
            raise ValueError
        self._keys.append(k)
        self._items.append(item)
        
    def pop(self, index:int=None):
        if index is None:
            self._keys.pop()
            return self._items.pop()
        else:
            self._keys.pop(index)
            return self._items.pop(index)
    
    def insert(self, item):
        'Insert a new item.  If equal keys are found, add to the left'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def insert_right(self, item):
        'Insert a new item.  If equal keys are found, add to the right'
        k = self._key(item)
        i = bisect_right(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def remove(self, item):
        'Remove first occurence of item.  Raise ValueError if not found'
        i = self.index(item)
        del self._keys[i]
        del self._items[i]

    def find(self, k):
        'Return first item with a key == k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i != len(self) and self._keys[i] == k:
            return self._items[i]
        raise ValueError('No item found with key equal to: %r' % (k,))

    def find_le(self, k):
        'Return last item with a key <= k.  Raise ValueError if not found.'
        i = bisect_right(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key at or below: %r' % (k,))

    def find_lt(self, k):
        'Return last item with a key < k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key below: %r' % (k,))

    def find_ge(self, k):
        'Return first item with a key >= equal to k.  Raise ValueError if not found'
        i = bisect_left(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key at or above: %r' % (k,))

    def find_gt(self, k):
        'Return first item with a key > k.  Raise ValueError if not found'
        i = bisect_right(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key above: %r' % (k,))


def param_hash(*args, **kwargs):
    return hash(str(args) + str(kwargs))


def cache(func:Callable):
    data = dict()
    def wrapper(*args, **kwargs):
        key = param_hash(*args, **kwargs)
        if key not in data:
            data[key] = func(*args, **kwargs)
        return data[key] 
    return wrapper


def lru_cache(func:Callable, max_size:int=128):
    data = dict()
    page = SortedCollection([], lambda x: x[0])
    def wrapper(*args, **kwargs):
        key = param_hash(*args, **kwargs)
        if key not in data:
            data[key] = func(*args, **kwargs)
            page.append((time(), key))
            if len(page) > max_size:
                data.pop(page.pop(0)[1])  
        return data[key] 
    return wrapper


def lifo_cache(func:Callable, max_size:int=128):
    """
    python >= 3.7, dict LIFO
    """
    data = dict()
    count = 0
    def wrapper(*args, **kwargs):
        key = param_hash(*args, **kwargs)
        if key not in data:
            data[key] = func(*args, **kwargs)
            if count > max_size:
                data.popitem()
            else:
                nonlocal count
                count += 1    
        return data[key] 
    return wrapper


def lfu_cache(func:Callable, max_size:int=128):
    """
    python >= 3.7
    """
    data = dict()
    count = 0
    use_count = dict()
    def wrapper(*args, **kwargs):
        key = param_hash(*args, **kwargs)
        if key not in data:
            data[key] = func(*args, **kwargs)
            use_count[key] += 1
            if count > max_size:
                data.popite
            else:
                nonlocal count
                count += 1    
        use_count[key] = 1
        return data[key] 
    return wrapper


if __name__ == "__main__":
    @cache
    def test_func(n:int):
        a = 0
        for _ in range(n ** 3):
            a += 1
        return a
        
    print(test_func(500))
    print(test_func(500))
