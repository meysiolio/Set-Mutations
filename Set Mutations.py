A_length = int(input())
A = set(map(int,input().split()))

otherSetsNum = int(input())

for i in range(otherSetsNum):
    line1 = input()
    command = line1.split()[0]
    setLenght = int(line1.split()[1])
    newSet = set(map(int,input().split()))
    if command == "intersection_update":
        A.intersection_update(newSet)
    if command == "update":
        A.update(newSet)
    if command == "symmetric_difference_update":
        A.symmetric_difference_update(newSet)
    if command == "difference_update":
        A.difference_update(newSet)
        
print(sum(A))