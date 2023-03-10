# solution [1,2,2,3,5,6]
def merge(nums1, m, nums2, n):
    if len(nums1) == 0:
        nums1 = nums2
    count = 0
    for i in range(m, m + n):
        nums1[i] = nums2[count]
        count += 1
    nums1.sort()
    print(nums1)

    # for i in range(m+n):
    #     sec = 0
    #     if nums1[i] > nums2[sec]:
    #         temp = nums1[i]
    #         nums1[i] = nums2[sec]
    #         counter = 1
    #         while i + counter < m+n:
    #             temp2 = nums1[i + counter]
    #             nums1[i + counter] = temp
    #             temp = temp2
    #             counter += 1
    #         sec += 1
    #     if nums1[i] == 0:
    #         nums1[i] = nums2[sec]
    #         sec += 1
    # print(nums1)


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
