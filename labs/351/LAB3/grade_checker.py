grade=int(input("Enter your numeric grade:"))
lettergrade = ""

if(grade >= 90 and grade <= 100):
    print("Your grade is : A")
    lettergrade = "A"
elif(grade>=80 and grade <= 89):
    print("Your grade is : B")
    lettergrade = "B"
elif(grade>=70 and grade <= 79):    
    print("Your grade is : C")
    lettergrade = "C"
elif(grade>=60 and grade <= 69):
    print("Your grade is : D")
    lettergrade = "D"   
elif(grade>=0 and grade <= 59):
    print("Your grade is : F")
    lettergrade = "F"
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")

if(lettergrade == "A" or lettergrade == "B" or lettergrade == "C"):
    print("Conratulations! You have done a great job!")

elif(lettergrade== "D" or lettergrade == "F"):
    print("You can do better. Work harder and try again!")