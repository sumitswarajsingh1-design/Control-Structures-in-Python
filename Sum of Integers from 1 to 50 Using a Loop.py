
start=int(input("Enter the first number : "))
end=int(input("Enter the ending number : "))
 
sum=0
for x in range(start,end+1):
    sum+=x
print(f"the sum of {start} to {end} is {sum}")


