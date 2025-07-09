def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = dict()
    for i,num in enumerate(numbers):
        group.setdefault(num,[]).append(i)

        return group
    

nums = [3,5,5,6,7,8,7,9,4,2]
result = group_indices(nums)
print(result)
