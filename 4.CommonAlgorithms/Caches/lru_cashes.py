from collections.abc import Callable
from functools import lru_cache


class LRUCache:
    def __init__(self, func: Callable, max_size: int = 1024):
        self._cache = dict()
        self._func = func
        self._max_size = max_size

    def __call__(self, *args):
        if args in self._cache:
            cached_result = self._cache.pop(args)
            self._cache[args] = cached_result
            print('result from cache')
            return cached_result

        result = self._func(*args)

        if len(self._cache) > self._max_size:
            # delete first elem
            del self._cache[next(iter(self._cache))]

        print('result is not from cache')
        self._cache[args] = result


@lru_cache()
def default_lru_cache(n):
    return n * n


def test_func(n):
    return n * n


def main_my_lru():
    my_lru_cache = LRUCache(func=test_func)
    my_lru_cache(3)
    my_lru_cache(3)
    my_lru_cache(5)
    my_lru_cache(7)
    print(my_lru_cache(3))
    print(my_lru_cache._cache)


def main_builtin_lru():
    default_lru_cache(5)
    default_lru_cache(5)
    default_lru_cache(5)
    default_lru_cache(5)
    default_lru_cache(4)
    default_lru_cache(2)
    hits = default_lru_cache.cache_info()
    print(hits)


if __name__ == '__main__':
    main_my_lru()
