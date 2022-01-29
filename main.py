# import re

# phoneNumRegex = re.compile('((sam)(eer|ir|er))*')

# mo = phoneNumRegex.search("s2s")

# print(mo.group(2)) if mo else print(mo)


# def lineFun(x):
#     return 1.2*x + 2
#
#
# def MAE(arr):
#     errSum = 0
#     for i in arr:
#         errSum += (lineFun(i[0])-i[1])**2
#     return errSum/(2*len(arr))
#
#
# arr = [[2, -2], [5, 6], [-4, -4], [-7, 1], [8, 14]]
# print(MAE(arr))

arr = [1,-3,-1,4,-1,-2,3,1,-3]

def maxSum(arr):
    max = -float('inf')
    for i in range(len(arr)):
        n = 0
        for j in range(i,len(arr)):
            sumArr =  sum(arr[n:j+1])
            if max < sumArr:
                max = sumArr
            n+=1
    return max

print(maxSum(arr))