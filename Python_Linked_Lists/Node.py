class Node:
    """let's create the function that constructs a node object"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """"This is how me create a linked list.
    We pass it a value and then create a Node with that value.
    Then we have our head and tail nodes reference out new node"""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    """In append method, we take in the value, create a new node
    check if the linked list is empty and set head and tail equal to the new node
    if the linked list is NOT empty we set the tail nodes reference equal to the new node
    and then set the tail node equal to the new node because it is now not the end of the list"""

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """Now lets create a method to print our linked list
    Creates a temp node and assignees it to the head node
    we create 'result' to hold out values as to ne returned
    While the temp node is not None we will add the value to result and cast that value as a string element"""

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    """Now lets add an element at the beginning of a linked list"""

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    """This will insert a value at a provided index"""

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.length == 0:
                self.tail = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    """This is traverse the whole list one node at a time"""

    def traverse (self):
        curent = self.head
        while curent is not None:
            print(curent.value, end = ' ')
            curent = curent.next
        print()

    """This will search for a target value in the linked list"""

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    """This will get the value of a node at a given index"""

    def get(self, index):
        current = self.head
        if index > self.length - 1 or index < 0:
            return "Index out of bounds"
        else:
            for _ in range(index):
                current = current.next
            return current.value

    """This will update the value of a node at a given index"""

    def set(self, index, value):
        current = self.head
        if index > self.length - 1 or index < 0:
            return "Index out of bounds"
        else:
            for _ in range(index):
                current = current.next
            current.value = value
            return True

    """This will pop and return the first value in the list"""

    def pop_first(self):
        if self.length == 0:
            return None

        poped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poped_node.next = None
        self.length -= 1
        return poped_node.value

    def pop(self):
        if self.length == 0:
            return None

        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value

        else:
            popped_node = self.tail
            temp = self.head

            while temp.next is not self.tail:
                temp = temp.next

            self.tail = temp
            self.tail.next = None
            self.length -= 1
            return popped_node.value

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None

        elif index == 0:
            return self.pop_first()

        elif index == self.length - 1:
            return self.pop()

        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next

            popped_node = prev.next
            prev.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value








test = LinkedList(1)
test.append(2)
test.append(3)
test.prepend(5)
test.insert(4, 10)
test.traverse()
print(str(test))
print(test.get(-9))
print(test.pop_first())
print(str(test))


