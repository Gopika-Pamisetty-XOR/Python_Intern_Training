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
    return 0

numbers = [14, 3, 9, 27, 8, 21, 5, 18]
RESULT = list_stats(numbers)
# print(result)
