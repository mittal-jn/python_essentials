my_list=[30,20,50,60,10]
print("Original List:", my_list)

# Bubble Sort
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print("Sorted List:", my_list)