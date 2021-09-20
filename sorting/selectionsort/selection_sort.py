def selection_sort(elements):
    for i in range(len(elements)-1):
        min = elements[i]
        for j in range(i+1, len(elements)):
            if min > elements[j]:
                elements[i], elements[j] = elements[j], elements[i]


elements = ['Raj', 'Suraj', 'Karan', 'Jade']

selection_sort(elements)

print(elements)
