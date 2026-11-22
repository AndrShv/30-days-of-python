import asyncio



def find_sum(target_sum: int, arr) -> dict[int, int]:
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum > target_sum:
            left += 1
        elif sum < target_sum:
            right -= 1
    return {
        left: arr[left],
        right: arr[right]
    }

async def main():
    array = [2, 5, 6, 9, 13, 19, 24, 29, 32, 34, 37, 41]
    target_sum = 3


