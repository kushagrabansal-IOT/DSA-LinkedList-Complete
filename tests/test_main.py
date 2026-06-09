import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_reverse():
    assert arr(reverse(build([1,2,3,4,5]))) == [5,4,3,2,1]
    assert arr(reverse(build([1]))) == [1]
    assert reverse(None) is None

def test_merge_sorted():
    l1=build([1,3,5]); l2=build([2,4,6])
    assert arr(merge_sorted(l1,l2)) == [1,2,3,4,5,6]

def test_find_middle():
    assert find_middle(build([1,2,3,4,5])).val == 3
    assert find_middle(build([1,2,3,4])).val == 3

def test_palindrome():
    assert is_palindrome(build([1,2,3,2,1])) == True
    assert is_palindrome(build([1,2,3])) == False

def test_lru():
    lru=LRUCache(2)
    lru.put(1,10); lru.put(2,20)
    assert lru.get(1) == 10
    lru.put(3,30)
    assert lru.get(2) == -1
    assert lru.get(3) == 30
