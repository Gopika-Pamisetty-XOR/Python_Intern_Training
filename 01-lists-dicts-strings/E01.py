#PROBLEM STATEMENT: Given the list numbers, write a function list_stats(nums) that returns a dictionary with the keys max, min, total, average, descending (a new list sorted from largest to smallest) and every_second (elements at index 0, 2, 4, ...). Then print the results exactly as shown. Do not change the original list.


def list_stats(nums):
    stats = {
        "max": max(nums),
        "min": min(nums),
        "total": sum(nums),
        "average": sum(nums)/len(nums),
        "descending": sorted(nums, reverse = True),
        "every_second": nums[::2]

    }
    print(stats)

    print(f"max: {stats['max']}")
    print(f"min: {stats['min']}")
    print(f"total: {stats['total']}")
    print(f"avaerage: {stats['average']:.2f}")
    print(f"descending: {stats['descending']}")
    print(f"every second: {stats['every_second']}")

 

numbers = [14, 3, 9, 27, 8, 21, 5, 18]   

result = list_stats(numbers)
# print(result)