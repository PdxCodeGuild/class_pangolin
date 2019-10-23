#Let's write a simple REPL (read evaluate print loop) calculator that can handle: 
# addition, subtraction, multiplication, and division.
#Ask the user for an operator and each operand.
#Don't forget that input returns a string, which you can convert to a float using float(user_input) 
#where user_input is the string you got from input.
input_operator = input("What is the operation you'd like to perform?")
input_operand1 = int(input("What is the first number?"))
inputer_operand2 = int(input("What is the second number?"))

if input_operator == "+":
    print(input_operand1 + inputer_operand2)
elif input_operator == "-":
    print(input_operand1 - inputer_operand2)
elif input_operator == "*":
    print(input_operand1 * inputer_operand2)
elif input_operator == "/":
    print(input_operand1 / inputer_operand2)