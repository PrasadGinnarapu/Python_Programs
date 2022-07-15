'''
2. Given an array of N integers.
Find the highest product by multiplying 3 elements.

Constraints:
##3<=N<=5e5 (i.e. 5**5)
##
##Example:
##     Input: [1,2,3,4]
##     Output: 2 * 3 * 4 = 24
##
##    Input: [1,5,-20,-10,4,3,9,10,8]
##    Output: -10 * -20 * 10 = 2000
'''

def maxof3elements(l):
    st = sorted(l)
    hi3 = st[-1]*st[-2]*st[-3]
    lo2hi = st[0]*st[1]*st[-1]
    return max(hi3,lo2hi)

l = [1,5,-20,-10,4,3,9,10,8]
res = maxof3elements(l)
print(res)
