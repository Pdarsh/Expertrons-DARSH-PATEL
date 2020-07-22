n=int(input())
li = []
marks = []
for i in range(n):
    n=input()
    m=float(input())
    li.append(n)
    marks.append(m)

d = dict(zip(li,marks))
m = list(set(marks))
m.sort()
s = m[1]

d = dict(sorted(d.items()))

for x,y in d.items():
    if (y == s):
        print(x)
