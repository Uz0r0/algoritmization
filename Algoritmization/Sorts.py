list = [1, 34, 454 ,234, 23, 234 , 11, 65, 232 ,8768, 0]

#Bubble-Sort
def bubbleSort(list):
    length = len(list)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            b = j + 1
            if list[j] > list[b]:
                list[j], list[b] = list[b], list[j]
                swapped = True
        if not swapped:
            break        
    return list

#Insertion-Sort
def insertionSort(list):
    length = len(list)
    for i in range(1, length):
        key = list[i] 
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key 
    return list        

print(f'InsertonSort: {insertionSort(list)}')


#Selection-Sort

#Randix-Sort

#Idk-Sort

#Quick-Sort
def quickSort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[len(list) // 2]

    left = [x for x in list if pivot > x]
    mid = [x for x in list if pivot == x]
    right = [x for x in list if pivot < x]

    return quickSort(left) + mid + quickSort(right)
