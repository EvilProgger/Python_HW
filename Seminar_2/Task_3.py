n = int(input("Введите число: "))

def get_filling(n):
    return [round((1 + 1 / x)**x) for x in range (1, n + 1)]

nums = get_filling(n)
print(nums)
print(round(sum(nums), 5))