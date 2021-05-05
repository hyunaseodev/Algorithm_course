import sys
sys.stdin=open("input.txt", "r")
N, M=map(int, input().split())
a=list(map(int, input().split()))
a.sort(reverse=True)
cnt=0

def boat(a):
    sum=a[0]
    for i in range(len(a)):
        if len(a)>1 and sum+a[-i-1]<= M:
            sum=sum+a[-i-1]
        else:
            return(a[1:len(a)-i])

while len(a)>0:
    a=boat(a)
    cnt+=1
print(cnt)