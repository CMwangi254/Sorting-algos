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


def insertion_sort(a):  # define a function for sorting the list
    for i in range(1, len(a)):  # loop through the list starting from the second item
        for j in range(i-1, -1, -1):  # looping through the list tarting from the item adjacent to the subject item
            if a[j] > a[j+1]:  # if number in subject is greater than the number on the right
                a[j], a[j+1] = a[j+1], a[j]  # swap them
            else:
                break  # break the loop
    return a  # return the newly sorted list


start_time = time.time()
print(insertion_sort(a))  # print the list
timetaken = time.time()-start_time
print(timetaken)


def insertion_sort(a):  # define a function for sorting the list
    for i in range(1, len(a)):  # loop through the list starting from the second item
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j], a[j + 1] = a[j + 1], a[j]  # swap them
            j -= 1
        else:
            break
    return a


start_time = time.time()
print(insertion_sort(a))  # print the list
timetaken = time.time()-start_time
print(timetaken)


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
