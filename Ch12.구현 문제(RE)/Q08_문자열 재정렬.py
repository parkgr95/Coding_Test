# K1KA5CB7
# AJKDLSI412K4JSJ9D
s = input()
ans_c = ""
ans_n = 0
for c in s:
    if c.isalpha():
        ans_c += c
    else:
        ans_n += int(c)
print("".join(sorted(ans_c)) + str(ans_n))