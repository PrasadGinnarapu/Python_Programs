'''
1. Given N bulbs, either on (1) or off(0).
Turning on ith bulb causes all remaining bulbs on the right to flip.
Find the min number of sweitches to turn all the bulbs on.

Constraints:
    1<=N<=1e5
    A[i]={0,1}'''
def bulbs(A):
    ''' Time complexity  is O(N)'''
	cost=0
	for b in A:
		if cost%2 ==0:
                    b=b
		else:
                    b=not b
		if b%2==1:
                    continue
		else:
                    cost+=1
	return cost
A=[1,0,1,0,1,1,0]
cost = bulbs(A)
print(cost)
