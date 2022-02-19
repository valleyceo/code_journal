# Circular Queue

# Time complexity: O(1) for dequeue, O(1) for enqueue (amortized time complexity)
class Queue:

    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:

        self._entries = [0] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x: int) -> None:

        if self._num_queue_elements == len(self._entries):  # Needs to resize.
            # Makes the queue elements appear consecutively.
            self._entries = (self._entries[self._head:] +
                             self._entries[:self._head])
            # Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [0] * (len(self._entries) * Queue.SCALE_FACTOR -
                                    len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self) -> int:

        self._num_queue_elements -= 1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:

        return self._num_queue_elements
