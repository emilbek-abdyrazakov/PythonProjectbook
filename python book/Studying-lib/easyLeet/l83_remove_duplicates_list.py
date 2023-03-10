def deleteDuplicates(head):
    for i in range(len(head) - 2):
        if head[i] == head[i + 1]:
            del head[i]
    return head


print(deleteDuplicates([1, 1, 2]))
print(deleteDuplicates([1, 1, 2, 3, 3]))
