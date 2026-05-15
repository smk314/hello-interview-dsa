# https://leetcode.com/problems/3sum/
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([0, 1, 1])
    []
    >>> three_sum([0, 0, 0])
    [[0, 0, 0]]
    """
    nums.sort()
    results: list[list[int]] = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:  # sum == target
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return results


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2, 7, 11, 15], 9)
    [1, 2]
    >>> two_sum([2, 3, 4], 6)
    [1, 3]
    >>> two_sum([-1, 0], -1)
    [1, 2]
    """
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:  # sum == target
            return [left + 1, right + 1]
    raise Exception("no solution found")


# https://leetcode.com/problems/container-with-most-water/
def max_area(height: list[int]) -> int:
    """
    >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49
    >>> max_area([1, 1])
    1
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            current = height[left]
            while left < right and height[left] <= current:
                left += 1
        else:
            current = height[right]
            while left < right and height[right] <= current:
                right -= 1
    return max_area
