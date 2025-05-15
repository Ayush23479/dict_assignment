
#  *************** Project 2 *****************

n = int(input("Enter a number : "))
my_list = [ele+1 for ele in range(n)]

print(my_list)
sList = my_list[0:5]
print(sList)
print(sList[::-1])