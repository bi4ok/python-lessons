import sys

s = {}
k = int(sys.stdin.readline().strip())

for l in range(101):
    s[str(l)] = 0
for i in range(int(k)):
    s1 = sys.stdin.readline().strip().split(' ')
    try:
        num = int(s1[0])
    except ValueError:
        continue
    for j in range(1, num + 1):
        if j > len(s1):
            break
        try:
            s[str(s1[j])] += 1
        except ValueError:
            pass

s1 = ''
for k in s:
    if s[k] > 0:
        s1 += (str(k) + ' ') * s[k]

sys.stdout.write(s1)