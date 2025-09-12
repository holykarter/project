# Singly Linked List in Python — from scratch, with a short demo
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Iterator, Optional

@dataclass
class _Node:
    value: Any
    next: Optional["_Node"] = None

class SinglyLinkedList:
    """
    Minimal, well-behaved singly linked list.
    O(1): prepend, append (amortized constant with tail pointer), pop_left
    O(n): get, set, insert (by index), remove (by value), pop (from end), find, reverse (but in-place & O(1) extra space)
    """
    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[_Node] = None
        self.tail: Optional[_Node] = None
        self._len = 0
        if iterable:
            for x in iterable:
                self.append(x)

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    # ---- Core helpers ----
    def _node_at(self, index: int) -> _Node:
        """Return node at index (0-based). Raise IndexError if out of range."""
        if index < 0 or index >= self._len:
            raise IndexError("index out of range")
        cur = self.head
        for _ in range(index):
            assert cur is not None
            cur = cur.next
        assert cur is not None
        return cur

    # ---- Fast O(1) operations ----
    def prepend(self, value: Any) -> None:
        """Insert at head in O(1)."""
        node = _Node(value, self.head)
        self.head = node
        if self.tail is None:  # first element
            self.tail = node
        self._len += 1

    def append(self, value: Any) -> None:
        """Insert at tail in O(1) with tail pointer."""
        node = _Node(value, None)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._len += 1

    def pop_left(self) -> Any:
        """Remove from head in O(1)."""
        if self.head is None:
            raise IndexError("pop_left from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:  # list became empty
            self.tail = None
        self._len -= 1
        return node.value

    # ---- O(n) operations (require traversal) ----
    def get(self, index: int) -> Any:
        return self._node_at(index).value

    def set(self, index: int, value: Any) -> None:
        self._node_at(index).value = value

    def insert(self, index: int, value: Any) -> None:
        """Insert before position index. index==len is append."""
        if index < 0 or index > self._len:
            raise IndexError("index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == self._len:
            self.append(value)
            return
        prev = self._node_at(index - 1)
        node = _Node(value, prev.next)
        prev.next = node
        self._len += 1

    def pop(self) -> Any:
        """Remove last item. O(n) because singly list must find prev of tail."""
        if self.head is None:
            raise IndexError("pop from empty list")
        if self.head is self.tail:
            val = self.head.value
            self.head = self.tail = None
            self._len -= 1
            return val
        # find node before tail
        prev = self.head
        while prev.next is not self.tail:
            prev = prev.next
            assert prev is not None
        assert self.tail is not None
        val = self.tail.value
        prev.next = None
        self.tail = prev
        self._len -= 1
        return val

    def remove(self, value: Any) -> bool:
        """Remove first occurrence of value; return True if found."""
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._len -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def find(self, predicate: Callable[[Any], bool]) -> Optional[int]:
        """Return index of first value matching predicate; else None."""
        idx = 0
        cur = self.head
        while cur:
            if predicate(cur.value):
                return idx
            idx += 1
            cur = cur.next
        return None

    def reverse(self) -> None:
        """In-place O(n), O(1) extra space."""
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


# ---- Demo: show when each method is useful ----
def demo():
    print("Create with iterable & append (queue-like build):")
    ll = SinglyLinkedList([1, 2, 3])
    print(" start:", ll)
    ll.append(4)     # O(1)
    ll.append(5)
    print(" after appends:", ll)

    print("\nPrepend (stack-at-head or building reversed):")
    ll2 = SinglyLinkedList()
    for x in [3, 2, 1]:
        ll2.prepend(x)  # O(1)
    print(" built via prepend:", ll2)

    print("\nQueue operations (FIFO): append -> pop_left")
    q = SinglyLinkedList()
    for job in ["A", "B", "C"]:
        q.append(job)           # enqueue
    print(" queue:", q)
    print(" dequeue:", q.pop_left())  # O(1)
    print(" queue now:", q)

    print("\nStack using head (LIFO): prepend -> pop_left")
    st = SinglyLinkedList()
    for x in [10, 20, 30]:
        st.prepend(x)  # push
    print(" stack:", st)
    print(" pop:", st.pop_left())  # pop
    print(" stack now:", st)

    print("\nInsert in middle (needs traversal):")
    print(" before:", ll)
    ll.insert(2, 99)  # O(n)
    print(" after insert at index 2:", ll)

    print("\nRemove a value (first occurrence):")
    print(" before:", ll)
    ll.remove(3)  # O(n)
    print(" after remove 3:", ll)

    print("\nPop last (singly list must traverse):")
    print(" before:", ll)
    print(" popped:", ll.pop())  # O(n)
    print(" after:", ll)

    print("\nReverse in-place:")
    print(" before:", ll)
    ll.reverse()  # O(n)
    print(" after:", ll)

    print("\nFind by predicate (first even):")
    idx = ll.find(lambda v: v % 2 == 0)
    print(" first even index:", idx, "value:", ll.get(idx) if idx is not None else None)

demo()
