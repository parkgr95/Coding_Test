data = input()
result = []
count = 0

for x in data:
  if ord(x) >= 65 and ord(x) <= 90: # if x.isalpha():1
    result.append(x)
  else:
    count += int(x)

result.sort()

if count != 0:
  result.append(str(count))

print(''.join(result))