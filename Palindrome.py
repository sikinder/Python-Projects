input_str = (input("Enter string to check: "))
print(type(input_str))
input_str_lower = input_str.lower()
print("Given string input converted to lowercase is : ", input_str_lower)
reversed_inp_str = input_str_lower[::-1]
print("Reversed string of the input string is :", reversed_inp_str)

if input_str_lower == reversed_inp_str:
    print("The Given string is Palindrome")
else:
    print("The Given string is not a Palindrome")
