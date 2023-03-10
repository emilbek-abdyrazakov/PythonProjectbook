def mergeTwoLists(list1, list2):
    list34 = []
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            list1.pop(list34)
            print(list34)


print(mergeTwoLists([1,2,3], [1,3,4]))