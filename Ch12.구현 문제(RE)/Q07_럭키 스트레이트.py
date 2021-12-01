s = str(input())
print("LUCKY" if not sum(map(int, s[:len(s)//2])) - sum(map(int, s[len(s)//2:])) else "READY")