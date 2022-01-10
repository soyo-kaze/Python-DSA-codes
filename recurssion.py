

def Factorial(n):
    if n == 0:
        return 1  # base case for the factorial
    else:
        return n*Factorial(n-1)  # the recussive case for the factorial


# print(Factorial(5))


def draw_line(tick_length, tick_label=""):
    line = '-'*tick_length
    if tick_label:
        line += ' '+tick_label
    print(line)


def draw_interval(major_length):
    if major_length > 0:
        draw_interval(major_length-1)
        draw_line(major_length)
        draw_interval(major_length-1)


def draw_ruler(inches_num, major_length):
    draw_line(major_length, "0")
    for j in range(1, 1+inches_num):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))


# draw_ruler(3, 5)


def bin_search(arr, low, high, target):
    if low > high:
        return [-1, False]
    mid = (high+low)//2
    if arr[mid] == target:
        return [mid, True]
    elif arr[mid] < target:
        return bin_search(arr, mid+1, high, target)
    else:
        return bin_search(arr, low, mid-1, target)


a = list(x for x in range(20))
# print(a)

print(bin_search(a, 0, len(a)-1, 10))

print(bin_search(a, 0, len(a)-1, 13))
