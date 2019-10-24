#Allow the user to keep performing operations until they say 'done'. 
#Use while True and break. Below is some sample input/output.

while True:
    input_operator = input("What is the operation you'd like to perform? Type 'done' to close.\n")
    if input_operator == "done":
        break
    input_operand1 = float(input("What is the first number?\n"))
    inputer_operand2 = float(input("What is the second number?\n"))
    if input_operator == "+":
        print(input_operand1 + inputer_operand2)
            
    elif input_operator == "-":
        print(input_operand1 - inputer_operand2)
            

    elif input_operator == "*":
        print(input_operand1 * inputer_operand2)
            

    elif input_operator == "/":
        print(input_operand1 / inputer_operand2)
    
    elif input_operator == "%":
        print(input_operand1 % inputer_operand2)

    elif input_operator == "**":
        print(input_operand1 ** inputer_operand2)