import random
import time
 
def merge_sort(arr):
	if len(arr) <= 1:
    	return arr
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	merged = []
	i = j = 0
	while i < len(left) and j < len(right):
    	if left[i] < right[j]:
        	merged.append(left[i])
        	i += 1
    	else:
        	merged.append(right[j])
        	j += 1
	while i < len(left):
    	merged.append(left[i])
        i += 1
	while j < len(right):
    	merged.append(right[j])
    	j += 1
	return merged
 
def test_sorting():
	random_nums = [random.randint(1, 1000000) for _ in range(1000000)]
	start_time = time.time()
	merge_sort(random_nums)
	end_time = time.time()
	random_time = end_time - start_time
 
	sorted_nums = list(range(1, 1000001))
	start_time = time.time()
	merge_sort(sorted_nums)
	end_time = time.time()
	sorted_time = end_time - start_time
 
	reversed_nums = list(range(1000000, 0, -1))
	start_time = time.time()
	merge_sort(reversed_nums)
	end_time = time.time()
	reversed_time = end_time - start_time
 
	print("Time taken to sort random nums is:", random_time, "seconds")
	print("Time taken to sort sorted nums is:", sorted_time, "seconds")
	print("Time taken to sort reversed nums is:", reversed_time, "seconds")
 
test_sorting()
