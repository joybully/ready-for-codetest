import sys

N = int(sys.stdin.readline().rstrip())
part = list(map(int, (sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
requestPart = list(map(int, (sys.stdin.readline().rstrip().split())))

def binarySearch(start, end, target):
    while(start<=end):
        mid = (start+end)//2
        if part[mid] == target:
            return mid
        elif part[mid]<target:
            start = mid+1
        elif part[mid]>target:
            end = mid-1
    return None

part = sorted(part)
requestPart = sorted(requestPart)

for i in requestPart:
    if binarySearch(0, N-1, i)!=None:
        print("yes ", end = "")
    else:
        print("no ", end = "")

print(" ")