data = input()
half = int(len(data) / 2)

count = 0
for i in range(half):
  count += int(data[i])
  count -= int(data[i + half])

if count == 0:
  print('LUCKY')
else:
  print('READY')
