# Design a data structure that can, efficiently with respect to time used. Store and
# check if the total of any three successibely added elememnts is equal to a given
# total. For example, movingTotal()creates an empty container with no existing
# totals.append([1,2,3,4]) appends elements[1,2,3,4], which means that there are two
# exisiting totals (1+2+3 = 6 and 2+3+4 = 9). append ([5]) appends element 5 and creates
# additional total from [3,4,5]. There would not be  three totals (1+2+3 =6 , 2+3+4 = 9,
# and 3+4+5 = 12). At this point contains (6) contains(9) and contains(12) show retrun True,
# while contains (7) should return False
# fullNumber = []
#
#
# def append(numbers):
#     fullNumber.extend(numbers)
#
#
# def contains(total):
#     checker = []
#     for i in range(0, len(fullNumber)):
#         if i + 3 <= len(fullNumber):
#             checker.append(sum(fullNumber[i:i + 3]))
#     return total in checker
#
#
# append([1, 2, 3, 4])
# print(contains(6))
# print(contains(9))
# print(contains(12))
# print(contains(7))
#
# append([5])
# print(contains(6))
# print(contains(9))
# print(contains(12))
# print(contains(7))

from collections import deque


class MovingTotal:
    def __init__(self):
        self.deque = deque()
        self.total = 0
        self.totals_set = set()

    def append(self, arr):
        for num in arr:
            self.total += num
            self.deque.append(num)
            if len(self.deque) == 3:
                self.totals_set.add(self.total)
                removed = self.deque.popleft()
                self.total -= removed

    def contains(self, total):
        return total in self.totals_set


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))