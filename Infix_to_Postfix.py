print("**************** Infix to Postfix *****************")

def MainMenu():
    Result = []
    operand = []
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    Expression= (input("Enter the infix Expression:: ").upper())
    for ch in Expression:
        if(ch=='('):
            operand.append(ch)
        elif(ch== ')'):
            while(operand [-1]!='('):
                element= operand.pop()
                Result.append(element)
            operand.pop()
        elif (ch== '^' or ch =='*' or ch == '/' or ch =='+' or ch == '-'):
            if(len(operand)>0):
                while(priority[operand[-1]]>= priority[ch]):
                    element=operand.pop()
                    Result.append(element)
                    if(len(operand)==0):
                        break
            operand.append(ch)
        else:
            Result.append(ch)
    while(len(operand)!=0):
        element= operand.pop()
        Result.append(element)
    print("")
    print ("Infix Expression is=",Expression)
    print("Postfix expression is=", end='')
    for element in Result:
        print(element, end= '')
    TryAgain()
def TryAgain():
    print ("")
    print("")
    choice= input("Do you want to convert more?: YES or NO: ")
    if choice== "YES":
        MainMenu()
    elif choice == "NO":
        print("Thank you")
        quit()
    else:
        print("Wrong Input")
        TryAgain()
MainMenu()

