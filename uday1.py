def OR(data, sz):
	mOR = 0
	for i in range(sz):
		mOR |= data[i]
	return mOR
def minSubset(data, sz, maxOR):
	count=[[1e9 for _ in range(maxOR+1)]for _ in range(sz+1)]
	count[0][0] = 0
	for i in range(sz) :
		for j in range(maxOR) :
			count[i + 1][j] = min(count[i + 1][j], count[i][j])
			if (count[i][j] != 1e9) :
				count[i + 1][j | data[i]] = min(
					count[i + 1][j | data[i]], count[i][j] + 1)
	return count[sz][maxOR]
# ----------Driver code--------
if __name__ == '__main__':
	data = [1,4,24,2]
	sz = len(data)
	maxOR = OR(data, sz)
	print(minSubset(data, sz, maxOR))



##def check(mid, array, n, K):
##	count = 0
##	sum = 0
##	for i in range(n):
##		if (array[i] > mid):
##			return False
##		sum += array[i]
##		if (sum > mid):
##			count += 1
##			sum = array[i]
##	count += 1
##	if (count <= K):
##		return True
##	return False
##def solve(array, n, K):
##	start = max(array)
##	end = 0
##	for i in range(n):
##		end += array[i]
##	answer = 0
##	while (start <= end):
##		mid = (start + end) // 2
##		if (check(mid, array, n, K)):
##			answer = mid
##			end = mid - 1
##		else:
##			start = mid + 1
##	return answer
### -----------Driver Code-------
##if __name__ == '__main__':
##	array = [5,6,6,8]
##	n = len(array)
##	K = 4
##	print(solve(array, n, K))
