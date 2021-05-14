import sys
sys.stdin=open("input.txt", "r")
num, n = input().split()
n=int(n)
a=[0]*(len(num)-n)

for i in range(len(a)):
    maxVal=0
    maxIndex=0
    for j in range(len(num)-len(a)+i+1):
        if int(num[j]) > maxVal:
            maxVal=int(num[j])
            maxIndex=j
    num=num[maxIndex+1:]
    a[i]=maxVal

for k in a:
    print(k, end='')