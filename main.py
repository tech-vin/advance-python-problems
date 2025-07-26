'''
deep copy vs shallow copy
'''
import copy

original = [[1, 2], [5, 6]]
s_copy = copy.copy(original)
s_copy[0].append(3)
s_copy[1].append(7)

print("original: ", original)
print("shallow copy: ", s_copy)

original = [[1, 2], [5, 6]]

d_copy = copy.deepcopy(original)
d_copy[0].append(3)
d_copy[1].append(7)

print("original: ", original)
print("deep copt: ", d_copy)



'''
Genarators
'''
def return_sequence(n):
    for i in range(1, n+1):
        yield i

seq = return_sequence(5)
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

'''
threading
'''

import threading, time

def worker(name, delay):
    for i in range(3):
        print(f"[{name}] is working... ({i}) ")
        time.sleep(delay)
    print(f'[{name}] done.')

t1 = threading.Thread(target=worker, args=['T1', 1])
t2 = threading.Thread(target=worker, args=["T2", 2])

t1.start()
t2.start()

t1.join()
t2.join()


print("all theads executed!")

'''
Merge Sort
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


testcases = [[5, 2, 1, 2, 7, 18, 21, 8], [8, 7, 5, 9, 11, 5]]
print("Merge Sort: ",[merge_sort(i) for i in testcases])


'''
Quick Sort
'''
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    mid = [i for i in arr if i == pivot]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]

    return quickSort(left) + mid + quickSort(right)

testcases = [[5, 2, 1, 2, 7, 18, 21, 8], [8, 7, 5, 9, 11, 5]]
print("Quick Sort: ", [quickSort(i) for i in testcases])