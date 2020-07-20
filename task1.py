# write a code to return the pair of elements which result the desired sum
# input> [2,4,6,3,1],6
# output> (2,4) returns 6

def findPairs(data, sum):
    pairs = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == sum:
                pairs.append(tuple([data[i],data[j]]))
    return pairs

print(findPairs([3,4,2,5],7))
