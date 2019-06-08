import time
import random
# a = [3, 2, 7, 5, 6]  # create a list


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


num = 1000
start = 20
end = 1500
A = Rand(start, end, num)


def insertion_sort3(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                break
        A[k+1] = curNum
    return A


start_time = time.time()
print(insertion_sort3(A))  # print the list
timetaken = time.time()-start_time
print(timetaken)