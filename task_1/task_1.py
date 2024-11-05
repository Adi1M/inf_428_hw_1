# This is the solution of the 1 task where I should find the longest continuous increasing subsequence
#All the links for tasks you can find in README
#Task 1:

index = 1
max_index = []

#This is the array from first example

nums = [1,3,5,4,7]

for i in range(0, len(nums) - 1):
    if nums[i] < nums[i + 1]:
        index += 1
    else:
        max_index.append(index)
        index = 1

max_index.append(index)
print(max(max_index))


#Task 2:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

if n == 0:
    print(nums1)

index = 0

for i in range(m, m + n):
    nums1.remove(0)
    nums1.insert(i, nums2[index])
    index += 1

print(nums1.sort())


# Task 3:
intersection = set()

for i in nums1:
    if i in nums2:
        intersection.add(i)

print(list(intersection))