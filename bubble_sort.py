def bubble_sort(elements):
    size = len(elements)

    for i in range(size):

        for i in range(size - 1):
            if (elements[i] < elements[i + 1]):
                elements[i], elements[i+1] = elements[i+1], elements[i]




elements = [5, 9,11,57,324,664, 4, 1, 6, 99, 65, 89]

bubble_sort(elements)

print(elements)


