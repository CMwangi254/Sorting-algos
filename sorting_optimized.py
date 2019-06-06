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
a = Rand(start, end, num)


# OPTIMIZED CODE
def insertion_sort(a):  # define a function for sorting the list
    for i in range(1, len(a)):  # loop through the list starting from the second item
        curNum = a[i]
        for j in range(i - 1, -1, -1):  # looping through the list tarting from the item adjacent to the subject item
            if a[j] > curNum:
                a[j+1] = a[j]
            else:
                a[j+1] = curNum
                break
        return a


start_time = time.time()
print(insertion_sort(a))  # print the list
timetaken = time.time()-start_time
print(timetaken)
