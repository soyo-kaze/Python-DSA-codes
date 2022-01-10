import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            total += disk_usage(os.path.join(path, i))
    print('{0:<7}'.format(total), os.path.join(path))
    return total


# path = input("enter the path: ")

# disk_usage(path)

count = 0


def binSearch(arr, low, high, target):
    global count
    count += 1
    # print(count)
    mid = (low+high)//2
    while low <= high:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binSearch(arr, low, mid-1, target)
        elif arr[mid] < target:
            return binSearch(arr, mid+1, high, target)
    return -1


a = [3, 3]
print(binSearch(a, 0, len(a)-1, 3))
