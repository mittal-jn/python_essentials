# Sum of even numbers
total = 0                      # running total starts at 0

for i in range(1, 51):
    if i % 2 == 0:
        total += i             # add each even number to the total

print("The sum of even numbers from 1 to 50 is:", total)

#While loop to sum even numbers from 1 to 50
total = 0
i= 1
while i <= 50:
    if i % 2 == 0:
        total += i
    i += 1  
print("The sum of even numbers from 1 to 50 is(while loop):", total)