#two boolean inputs
bool1 = True
bool2 = False

#logical AND
result_and = bool1 and bool2
print("Logical AND:", result_and)

#logical OR
result_or = bool1 or bool2
print("Logical OR:", result_or)

#logical NOT
result_not = not bool1
print("Logical NOT:", result_not)

#bitwise operators
num1= 5
num2= 3
print("binary for 5 and 3:",bin(5),bin(3))

#bitwise AND
result_bitwise_and = num1 & num2

print("Bitwise AND:", result_bitwise_and)

#bitwise OR
result_bitwise_or = num1 | num2
print("Bitwise OR:", result_bitwise_or)

#bitwise XOR
result_bitwise_xor = num1 ^ num2
print("Bitwise XOR:", result_bitwise_xor)
#bitwise NOT
result_bitwise_not = ~num1
print("Bitwise NOT:", result_bitwise_not)
#bitwise left shift
result_bitwise_lshift = num1 << 1
print("Bitwise Left Shift:", result_bitwise_lshift)
#bitwise right shift
result_bitwise_rshift = num1 >> 1
print("Bitwise Right Shift:", result_bitwise_rshift)


#Print the results in binary form using bin()
print("Bitwise AND (binary):", bin(result_bitwise_and))
print("Bitwise OR (binary):", bin(result_bitwise_or))
print("Bitwise XOR (binary):", bin(result_bitwise_xor))
print("Bitwise NOT (binary):", bin(result_bitwise_not))
print("Bitwise Left Shift (binary):", bin(result_bitwise_lshift))
print("Bitwise Right Shift (binary):", bin(result_bitwise_rshift))


