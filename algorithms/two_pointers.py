import asyncio


async def find_sum(target_sum: int, arr: list[int]) -> dict[int, int]:
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return {
                left: arr[left],
                right: arr[right]
            }
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1

    return {}


async def main():
    array = [2, 5, 6, 9, 13, 19, 24, 29, 32, 34, 37, 41]
    required_sum = 60
    result_sum = await find_sum(required_sum, array)
    print(result_sum)


asyncio.run(main())
