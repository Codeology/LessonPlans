class DictionaryStack:
    def __init__(self):
        self.data = {}
        self.index = -1

    def push(self, value):
        self.index += 1
        self.data[self.index] = value
        return value

    def pop(self):
        if self.index > -1:
            value = self.data[self.index]
            del self.data[self.index]
            self.index -= 1
            return value

    def peek(self):
        if self.index > -1:
            return self.data[self.index]

    def isEmpty(self):
        return self.index == -1

class LinkedListStack:
    def __init__(self):
        self.tail = None

    def push(self, value):
        if not self.tail:
            self.tail = Node(value)
        else:
            self.tail.append(value)
            self.tail = self.tail.next
        return value

    def pop(self):
        if self.tail:
            value = self.tail.value
            self.tail = self.tail.prev
            self.next = None
            return value

    def peek(self):
        if self.tail:
            return self.tail.value

    def isEmpty(self):
        return self.tail == None


class ArrayStack:
    def __init__(self):
        self.index = -1
        self.MAXSIZE = 2
        self.data = [None for i in xrange(self.MAXSIZE)]

    def push(self, value):
        self.index += 1

        # we've hit the max, resize the array!!
        if self.index == self.MAXSIZE:
            self.MAXSIZE *= 2
            newArray = [None for i in xrange(self.MAXSIZE)]
            newArray[:self.MAXSIZE/2] = self.data
            self.data = newArray
        self.data[self.index] = value
        return value

    def pop(self):
        if self.index > -1:
            value = self.data[self.index]
            self.index -= 1
            return value

    def peek(self):
        if self.index > -1:
            return self.data[self.index]

    def isEmpty(self):
        return self.index == -1

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        if not self.tail:
            self.tail = self.head = Node(value)
        else:
            self.tail.append(value)
            self.tail = self.tail.next
        return value

    def remove(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return value

    def peek(self):
        if self.head:
            return self.head.value

    def isEmpty(self):
        return self.head == None

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def append(self, value):
        newNode = Node(value)
        self.next = newNode
        newNode.prev = self

def tests():
    # Stack tests
    for s in [DictionaryStack(), LinkedListStack(), ArrayStack()]:
        s.push(1)
        s.push(2)
        s.push(3)

        assert(s.isEmpty() == False)
        assert(s.pop() == 3)
        assert(s.peek() == 2)
        assert(s.pop() == 2)
        assert(s.peek() == 1)
        assert(s.pop() == 1)
        assert(s.isEmpty() == True)

    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    assert(q.isEmpty() == False)
    assert(q.remove() == 1)
    assert(q.peek() == 2)
    assert(q.remove() == 2)
    assert(q.peek() == 3)
    assert(q.remove() == 3)
    assert(q.isEmpty() == True)


if __name__ == "__main__":
    tests()
