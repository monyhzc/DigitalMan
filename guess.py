import random
n = random.randint(0,100)
x = int(input())
cnt = 1
while (x!=n):
    if(x>n): print("Too Big")
    if(x<n): print("Too Small")
    cnt = cnt + 1
    x = int(input())
print("Times:",cnt)