#input 5 numbers from the user and store them in a list
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3= int(input("Enter the third number: "))
num4= int(input("Enter the fourth number: "))
num5= int(input("Enter the fifth number: "))
my_list=[num1,num2,num3,num4,num5]
print(my_list)

print("Sorted List : ", sorted(my_list))

my_list.sort()
print("Sorted list using sort :", my_list)

#append
new_list= my_list.append(10)
#updated list
print("Updated List:", my_list)

#remove from the list
my_list.remove(my_list[3])
print("List after removing an element:", my_list)

#reverse
my_list.reverse()
print("Reversed List:", my_list)

