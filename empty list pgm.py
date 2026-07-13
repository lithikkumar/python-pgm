list1=[]
list2=[]
result=[]

n=int(input("Enter the number of elements:"))

print("Enter element for list1:")
for i in range(n):
    num=int(input("Enter element:"))
    list1.append(num)
    
print("Enter element for list2:")
for i in range(n):
    num=int(input("Enter element:"))
    list2.append(num)
    
for i in range(n):
    result.append(list1[i]+list2[i])
    print("\nList1:",list1)
    print("\nList2:",list2)
    print("Result(Addition):",result)
    
    
