a = [3, 2, 7, 5, 6]  # create a list


def insertion_sort(a):  # define a function for sorting the list
    for i in range(1, len(a)):  # loop through the number of items in the list
        for j in range(i-1, -1, -1):  # looping through the index value of the items in the list starting from the end
            if a[j] > a[j+1]:  # if number in subject is greater than the number on the left
                a[j], a[j+1] = a[j+1], a[j]  # swap them
            else:
                break  # break the loop
    return a  # return the newly sorted list


print(insertion_sort(a))  # print the list
