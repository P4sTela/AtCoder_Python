a, b = map(str, input().split())
c = int(a + b)

if(c ** 0.5).is_integer():
    print("Yes")
else:
    print("No")
