'''
3. Given a list of interval:[start, end].
Find the length of the maximal set of mutually disjoint intervals

Constraints:
    1<=N<=1e5
    1<=A[i][0]<=A[i][2]1e9

Example:
input: [[1,2],[2,10],[4,6]]
output:2

Explanation:
Select [1,2] and [4,6].
selecting [2,10 will block [1,2] and [4,6]]
'''
class Solution:
    def solve(self,A):
        A.sort(key=lambda x:x[1])
        print(A)
        prev_s, prev_e = A[0]
        count = 1
        for s,e in A:
            if s <= prev_e:
                pass
            else:
                prev_s, prev_e = s, e
                count += 1
        return count
A=[[2,4],[4,10],[1,2],[4,6],[10,15]]
sobj = Solution()
print(sobj.solve(A))
