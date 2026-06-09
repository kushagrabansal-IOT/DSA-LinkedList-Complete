# Linked List — Learning Notes
# By Kushagra Bansal | Project Lab India

## Dummy Node Pattern
Always use: dummy=Node(); dummy.next=head
Avoids edge case handling when head changes.

## Floyd Cycle Detection
Phase 1: slow=1step, fast=2steps → they meet inside cycle
Phase 2: reset slow to head, both 1step → meet at cycle start
Proof: distance from head to cycle start = distance from meet point to start

## Two Pointer Patterns
| Problem | Pointers | How |
|---------|---------|-----|
| Find middle | slow+fast | fast=2x speed |
| Remove nth end | two with gap n+1 | advance fast n+1, then both |
| Cycle detection | slow+fast | fast=2x speed |
| Intersection | two heads | switch when null |

## Common Templates
Reverse: prev=None, cur=head; while cur: nxt=cur.next; cur.next=prev; prev=cur; cur=nxt
Merge: dummy=Node; while l1 and l2: pick smaller; attach remaining
