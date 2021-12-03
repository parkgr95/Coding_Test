s = input()
ans = int(s[0])
for c in s[1:]:
    if ans <= 1 or c in '01':
        ans += int(c)
    else:
        ans *= int(c)
print(ans)