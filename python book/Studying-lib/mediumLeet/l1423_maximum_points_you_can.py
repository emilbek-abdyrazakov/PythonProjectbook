# There are several cards arranged in a row, and each card has an associated number of
# points. The points are given in the integer array cardPoints. In one step, you can
# take one card from the beginning or from the end of the row. You have to take exactly
# k cards. Your score is the sum of the points of the cards you have taken.Given the
# integer array cardPoints and the integer k, return the maximum score you can obtain.
def maxScore(cardPoints, k):
    ind1 = []
    ind2 = []
    res = 0
    for i in range(0,k):
        ind1.append(i)
    for y in range(-1,-k-1,-1):
        ind2.append(y)
    # ind2.reverse()
    ind1.reverse()
    ind = ind1 + ind2
    counter = 0
    big = []
    for x in range(len(ind)):
        if counter >= k:
            big.append(res)
            res -= cardPoints[ind[x-k]]
        res += cardPoints[ind[x]]
        counter += 1
        if x == len(ind)-1:
            big.append(res)
    return max(big)


print(maxScore([1, 2, 3, 4, 5, 6, 1], 3))

        # print(cardPoints[ind[x:x+k]])

        # if sum(cardPoints[ind[i:i+k]]) >= res:
        #     res = sum(cardPoints[ind[i:i+k]])
    # return res
    #     if cardPoints[ind[i:k]] >= res:
    #         res = cardPoints[ind[i:k]]
    # return res




    # s = cardPoints[:k]
    # a = cardPoints[-k:]
    # s.reverse()
    # a.reverse()
    # j = s + a
    # res = 0
    # v = k -1
    # for i in range(len(j)-v):
    #     res1 = sum(j[i:i+k])
    #     if res1 >= res:
    #         res = res1
    # return res

