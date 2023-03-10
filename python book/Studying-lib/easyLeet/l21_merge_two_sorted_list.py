def mergeTwoLists(list1, list2):
    # list = 0
    # for i in range(len(list1)):
    #     for x in range(len(list2)):
    #         if list1[i] < list2[x]:
    #             list.append([i])
    # return list
    list3 = []
    i = 0
    while i < 3:
        if list1[i] <= list2[i]:
            list3.append(list1[i])
            list1.pop(list1[i])

            print(list1)
        else:
            list3.append(list2[i])
            i += 1
    return list3


print(mergeTwoLists([1,2,4], [1,3,4]))
# print(mergeTwoLists([], []))
# print(mergeTwoLists([], [0]))

# Output: [1,1,2,3,4,4]