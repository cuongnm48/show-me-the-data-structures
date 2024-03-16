class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    set_1 = set()
    current = llist_1.head
    while current:
        set_1.add(current.value)
        current = current.next
    
    set_2 = set()
    current = llist_2.head
    while current:
        set_2.add(current.value)
        current = current.next
    
    union_set = set_1.union(set_2)
    
    result = LinkedList()
    for value in union_set:
        result.append(value)
    
    return result

def intersection(llist_1, llist_2):
    set_1 = set()
    current = llist_1.head
    while current:
        set_1.add(current.value)
        current = current.next
    
    set_2 = set()
    current = llist_2.head
    while current and current is not None:
        set_2.add(current.value)
        current = current.next
    
    intersection_set = set_1.intersection(set_2)
    
    result = LinkedList()
    for value in intersection_set:
        result.append(value)
    
    return result


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

## Test Case 3: Edge case with one empty list
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3, 5, 7, 9]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Union (one empty list):", union(linked_list_7, linked_list_8))  # Output should be: 9 -> 3 -> 5 -> 7 -> 
print("Intersection (one empty list):", intersection(linked_list_7, linked_list_8))  # Output should be empty

## Test Case 4: Edge case with very large values
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = list(range(1, 1001, 2))  # Odd numbers from 1 to 1000
element_2 = list(range(2, 1001, 2))  # Even numbers from 2 to 1000

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print("Union (very large values):", union(linked_list_9, linked_list_10))  # Output should be: 1 -> 2 -> 3 -> ... -> 999 -> 1000 ->
print("Intersection (very large values):", intersection(linked_list_9, linked_list_10))  # Output should be empty

## Test Case 5: General case with overlapping values
linked_list_11 = LinkedList()
linked_list_12 = LinkedList()

element_1 = [1, 2, 3, 4, 5]
element_2 = [4, 5, 6, 7, 8]

for i in element_1:
    linked_list_11.append(i)

for i in element_2:
    linked_list_12.append(i)

print("Union (overlapping values):", union(linked_list_11, linked_list_12))  # Output should be: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 ->
print("Intersection (overlapping values):", intersection(linked_list_11, linked_list_12))  # Output should be: 4 -> 5 ->