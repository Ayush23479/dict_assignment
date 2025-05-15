#  *************** Project 1 *****************

# without conditional statements

# my_dict ={"Ram": 50,
#           "Shyam": 40,
#           "Hari": 76,
#           "Surya": 34,
#           "Krish": 87}

# std = input("Enter the name of the student : ") 

# # print("The marks of the student",std," is ",my_dict.get(std,'student not found'))
# output= my_dict.get(std,"Student not found")
# print(std,"marks : ",output)


# With conditional statements

my_dict ={"Ram": 50,
          "Shyam": 40,
          "Hari": 76,
          "Surya": 34,
          "Krish": 87}

std = input("Enter the name of the student : ") 

if std in my_dict:
    print("The marks of the student",std,"is",my_dict[std])

else:
    print("Student not found.")
