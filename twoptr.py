# https://leetcode.com/problems/container-with-most-water/
def max_area(height: list[int]) -> int:
    """
    >>> max_area([1,8,6,2,5,4,8,3,7])
    49
    >>> max_area([1,1])
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
