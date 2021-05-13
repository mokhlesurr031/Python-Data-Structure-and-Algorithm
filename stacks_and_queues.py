# FIFO approach (queue)
# LIFO approach (stack)

from collections import deque


# Create a linked_list

linked_list = deque()

print(linked_list)


# Append values

linked_list.append(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list)

# Append value at the beginning of the list

linked_list.appendleft(11)

print(linked_list)


# Remove last element

linked_list.pop()

print(linked_list)

linked_list.popleft()

print(linked_list)
