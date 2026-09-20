def insertion_sort(lst):
    for i in range(1,len(lst)):
        key = lst[i]

        # Move elements of lst[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i-1

        while j >= 0 and key < lst[j]:
            lst[j+1]=lst[j]
            j-=1

        # Insert key in its correct position
        lst [j+1]=key
    return lst

lst = [12,11,13,5,6]

sorted = insertion_sort(lst)
print("Sorted Elements : ",sorted)