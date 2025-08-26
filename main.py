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

'''
Find longest consecutive
example: [6, 2, 4, 0, 1, 3]
result: 5
explanation: [0,1,2,3,4]
'''

def longestConsecutive(arr):
    arr_set = set(arr)
    longest_streak  = 0
    for item in arr:
        if item - 1 not in arr_set:
            current_num = item
            current_streak = 1
            while current_num + 1 in arr_set:
                current_num += 1
                current_streak += 1
        longest_streak = max(current_streak, longest_streak)
    return longest_streak


testcases = [[6,2,4,0,1,3], [9, 19, 100, 21, 20]]
print("Longest Consecutive: ", [longestConsecutive(i) for i in testcases])

'''
Write a function to find the second largest number in a list.
'''
def second_largest_num_using_sort(num):
    num.sort()
    return num[-2]

def second_largest_num_organic_way(num):
        if len(num) < 2:
            return None
        first, second = float('-inf')
        for n in num:
            if n > first:
                second = first
                first = n
            elif first > n > second:
                second = n
        return second if second != float('-inf') else None

testcases = [[1, 2, 1, 5, 2, 8], [10, 11, 8, 5]]
print("Second Largest: ", [second_largest_num_using_sort(x) for x in testcases])

'''
Write a program to check if two strings are anagrams.
'''
def checkifanagram(string1, string2):
    return sorted(string1) == sorted(string2)

def checkIfAnagramWithOutBuiltIn(string1, string2):
    if len(string1) != len(string2):
        return False
    freq = {}
    for char in string1:
        freq[char] = freq.get(char, 0) + 1

    for char in string2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
    return True

print("Is anagram:", checkifanagram('silent', 'listen'))
print("Is anagram:", checkifanagram('silent', 'listet'))
print("Is anagram:", checkIfAnagramWithOutBuiltIn('silent', 'listen'))
print("Is anagram:", checkIfAnagramWithOutBuiltIn('silent', 'liste'))