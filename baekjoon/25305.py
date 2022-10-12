n, k = input().split()
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)
print(arr[int(k)-1])