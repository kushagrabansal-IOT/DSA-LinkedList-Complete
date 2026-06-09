# DSA-LinkedList-Complete — Solutions
# Author: Kushagra Bansal — Project Lab India

class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val; self.next = nxt

def arr(head):
    r=[]; c=head
    while c: r.append(c.val); c=c.next
    return r

def build(lst):
    if not lst: return None
    h=Node(lst[0]); c=h
    for v in lst[1:]: c.next=Node(v); c=c.next
    return h

def reverse(head):
    """3-pointer reversal | O(n) T, O(1) S"""
    prev=None; cur=head
    while cur:
        nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
    return prev

def has_cycle(head):
    """Floyd detection | O(n) T, O(1) S"""
    s=f=head
    while f and f.next:
        s=s.next; f=f.next.next
        if s is f: return True
    return False

def cycle_start(head):
    """Floyd phase 2 — find cycle entry | O(n) T, O(1) S"""
    s=f=head
    while f and f.next:
        s=s.next; f=f.next.next
        if s is f:
            s=head
            while s is not f: s=s.next; f=f.next
            return s
    return None

def merge_sorted(l1, l2):
    """Dummy node merge | O(n+m) T, O(1) S"""
    d=Node(); c=d
    while l1 and l2:
        if l1.val<=l2.val: c.next=l1; l1=l1.next
        else:              c.next=l2; l2=l2.next
        c=c.next
    c.next=l1 or l2
    return d.next

def find_middle(head):
    """Slow-fast pointer | O(n) T, O(1) S"""
    s=f=head
    while f and f.next: s=s.next; f=f.next.next
    return s

def remove_nth_end(head, n):
    """Two-pointer one-pass | O(n) T, O(1) S"""
    d=Node(); d.next=head; fast=slow=d
    for _ in range(n+1): fast=fast.next
    while fast: slow=slow.next; fast=fast.next
    slow.next=slow.next.next
    return d.next

def is_palindrome(head):
    """Reverse half | O(n) T, O(1) S"""
    mid=find_middle(head); second=reverse(mid)
    p1=head; p2=second
    while p2:
        if p1.val!=p2.val: return False
        p1=p1.next; p2=p2.next
    reverse(second)
    return True

def reverse_k_group(head, k):
    """Count k, reverse segment | O(n) T, O(1) S"""
    d=Node(); d.next=head; prev=d
    while True:
        c=0; node=prev.next
        while node and c<k: node=node.next; c+=1
        if c<k: break
        cur=prev.next; p=None
        for _ in range(k):
            nxt=cur.next; cur.next=p; p=cur; cur=nxt
        tail=prev.next; prev.next=p; tail.next=cur; prev=tail
    return d.next

from collections import OrderedDict
class LRUCache:
    """DLL + HashMap | O(1) get/put"""
    def __init__(self, cap): self.cap=cap; self.c=OrderedDict()
    def get(self, k):
        if k not in self.c: return -1
        self.c.move_to_end(k); return self.c[k]
    def put(self, k, v):
        if k in self.c: self.c.move_to_end(k)
        self.c[k]=v
        if len(self.c)>self.cap: self.c.popitem(last=False)

if __name__ == "__main__":
    print("="*55)
    print("  DSA LinkedList Complete — Project Lab India")
    print("="*55)
    print(f"  Reverse [1..5]:        {arr(reverse(build([1,2,3,4,5])))}")
    print(f"  Middle of [1..5]:      {find_middle(build([1,2,3,4,5])).val}")
    l1=build([1,3,5]); l2=build([2,4,6])
    print(f"  Merge sorted:          {arr(merge_sorted(l1,l2))}")
    print(f"  isPalindrome [1,2,1]:  {is_palindrome(build([1,2,1]))}")
    print(f"  KGroupReverse k=2:     {arr(reverse_k_group(build([1,2,3,4,5]),2))}")
    lru=LRUCache(2)
    lru.put(1,10); lru.put(2,20)
    print(f"  LRU get(1):            {lru.get(1)}")
    lru.put(3,30)
    print(f"  LRU get(2) evicted:    {lru.get(2)}")
    print("="*55)
