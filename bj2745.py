num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()
ans = 0
for i, num in enumerate(n[::-1]):
    ans += int(b) ** i * num_list.index(num)
print(ans)

# n, b = input().split()
# print(int(n, int(b))) 
#이것도 가능함