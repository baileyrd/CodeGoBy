import sys
from itertools import imap # not needed in Python 3, use map instead
data = imap(int, sys.stdin.read().split())
scan = data.next # or data.__next__ if you happen to use Python 3

def cache(wrapped):
    memo = {}
    def inner(arg):
        if arg in memo:
            return memo[arg]
        ret = wrapped(arg)
        memo[arg] = ret
        return ret
    return inner