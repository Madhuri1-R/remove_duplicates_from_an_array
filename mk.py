def remove_duplicates(arr):
    if len(arr) == 0:
       return[]
    unique = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i+1]:
           unique.append(arr[i])
    return unique
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter element value:"))
    arr.append(num)
result = remove_duplicates(arr)  
print("After removing duplicates:",result)


 