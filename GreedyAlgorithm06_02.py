import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

b=[]
for i in range(n):
    b.append([i+1, a[i]])
b.sort(reverse=True)

answer=[]
for i in range(n):
    if i==0 or b[i][1]==0:
        answer.insert(0,b[i][0])
    else:
        cnt=0
        for j in range(i):
            if answer[j]>b[i][0]:
                cnt+=1
            if cnt==b[i][1]:
                answer.insert(j+1,b[i][0])
                break

for i in answer:
    print(i, end=" ")

