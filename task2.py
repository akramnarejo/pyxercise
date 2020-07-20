# write a code to return the pair of elements which result the maximum product
# input> [4,5,3,-4,-6]
# output> (-4,-6)

def maxProduct(data):
    maxval = float('-inf')
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if maxval < data[i]*data[j]:
                maxval = data[i]*data[j]
                a,b = (data[i],data[j])
    return tuple([a,b])
    
print(maxProduct([-3000,5,-2,8,-40,-1000]))

