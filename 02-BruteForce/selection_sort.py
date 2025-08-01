def selection_sort(xs):
    n = len(xs)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if xs[j] < xs[min_index]:
                min_index = j
        xs[i], xs[min_index] = xs[min_index], xs[i]

xs=[3,2,1,5,4]


print(selection_sort(xs))

