def bubble_sort(elements):
    length = len(elements)
    for i in range(length):
        swapped = False
        for j in range(length-1-i):
            if elements[j] > elements[j+1]:
                swapped = True
                elements[j], elements[j+1] = elements[j+1], elements[j]

        if not swapped:
            break
    print(elements)


elements = [80, 40, 50, 60, 30]
bubble_sort(elements)
