import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

maxNum=0
answer=""

while len(a)>0:
    if (a[0]>maxNum and a[0]<a[-1]) or (a[0]>maxNum and a[-1]<maxNum):
        answer=answer+"L"
        maxNum=a[0]
        a.pop(0)
    elif (a[-1]>maxNum and a[0]>a[-1]) or (a[-1]>maxNum and a[0]<maxNum):
        answer=answer+"R"
        maxNum=a[-1]
        a.pop()
    else:
        break

print(len(answer))
print(answer)