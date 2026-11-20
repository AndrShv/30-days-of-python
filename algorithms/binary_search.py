import  asyncio

async def binary_search(target: int, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1


async def main():
    target_num = 37
    example_arr = [2, 5, 6, 9, 13, 19, 24, 29, 34, 37, 41]
    found_index = await binary_search(target_num, example_arr)
    if found_index != -1:
      print(f"Индекс числа: {found_index}")
    else:
      print("Число не найдено")

asyncio.run(main())