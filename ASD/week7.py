##    Muhammad Irfan Abidin
##    L200210021/A
print('--Muhammad Irfan Abidin/L200210021--')

def binSe(arr, target):
    if arr != sorted(arr):
        print('Array belum terurut!')
    else:
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result

## Output
print(binSe([1, 2, 3, 3, 4, 4, 4, 5], 4))   # 4
print(binSe([1, 1, 2, 3, 5, 8], 1))         # 0

def find_peak(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


## Output
print(find_peak([0, 2, 4, 2, 0]))       # 2
print(find_peak([0,5,10,20,10,2,0]))    # 3