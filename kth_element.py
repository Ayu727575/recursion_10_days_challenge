def kth(arr1, m, arr2, n, k):
	
	if (k > (m + n) or k < 1):
		return -1
	
	if (m > n):
		return kth(arr2, n, arr1, m, k)
	
	if (m == 0):
		return arr2[k - 1]

	if (k == 1):
		return min(arr1[0], arr2[0])
	
	i = min(m, k // 2)
	j = min(n, k // 2)
	
	if (arr1[i - 1] > arr2[j - 1]):
		return kth(arr1, m, arr2[j:], n - j, k - j)
	else:
		return kth(arr1[i:], m - i, arr2, n, k - i)


def findKthElement(arr1, arr2, k):  
	return kth(arr1, len(arr1), arr2, len(arr2), k)