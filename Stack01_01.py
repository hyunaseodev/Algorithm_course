import sys
sys.stdin=open("input.txt", "r")
num, m = map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:#stack이 비워져있으면 false, 그렇지 않으면 true
        stack.pop()
        m-=1
    stack.append(x)
if m!= 0:
    stack=stack[:-m]
res=''.join(map(str, stack)) #string을 join함
print(res) 
