# class MovingTotal:
#
#     def append(self, numbers):
#         """
#         :param numbers: (list) The list of numbers.
#         """
#         pass
#
#     def contains(self, total):
#         for i in range(slef.numbers)
#         """
#         :param total: (int) The total to check for.
#         :returns: (bool) If MovingTotal contains the total.
#         """
#         return None
#
#
# if __name__ == "__main__":
#     movingtotal = MovingTotal()
#
#     movingtotal.append([1, 2, 3, 4])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))
#
#     movingtotal.append([5])
#     print(movingtotal.contains(6))
#     print(movingtotal.contains(9))
#     print(movingtotal.contains(12))
#     print(movingtotal.contains(7))
#
# import json
# def sort_by_price_ascending(json_string):
#     data = json.loads(json_string)
#     sorted_data = sorted(data, key=lambda x: (x["price"], x["name"]))
#     return json.dumps(sorted_data)
#
#
# print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
#
# Given an integer array nums, return the third distinct maximum number in this array. If the
# third maximum does not exist, return the maximum number.

def thirdMax(nums):
    import sys

    if (len(nums) < 3):
        return max(nums)
    arr_size = len(nums)

    # Initialize first, second
    # and third Largest element
    first = nums[0]
    second = -sys.maxsize
    third = -sys.maxsize

    # Traverse array elements
    # to find the third Largest
    for i in range(1, arr_size):

        # If current element is
        # greater than first,
        # then update first,
        # second and third
        if (nums[i] > first):

            third = second
            second = first
            first = nums[i]


        # If arr[i] is in between
        # first and second
        elif (nums[i] > second):

            third = second
            second = nums[i]

        # If arr[i] is in between
        # second and third
        elif (nums[i] > third):
            third = nums[i]

    return third


print(thirdMax([3, 2, 1, 5]))
print(thirdMax([2, 2, 3, 1]))
