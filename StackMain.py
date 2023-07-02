from Stack import*
print("**********************************************************")
print("******   My Stack Menu                              ******")
print("******   1.Push                                     ******")
print("******   2.Pop                                      ******")
print("******   3. Display Stack contents                  ******")
print("******   4.Exit                                     ******")
print("**********************************************************")

stack = Stack()
def choice():
    Choice = int(input("Enter your choice: "))
    if Choice ==1:
        item= int(input("Enter the number to be pushed into the stack:: "))
        stack.push(item)
        choice()
    elif Choice == 2:
        print("")
        stack.pop()
        choice()
    elif Choice == 3:
        stack.DisplayStack()
        choice()
    elif Choice== 4:
        quit()
    else:
        print ("Invalid Input")
        choice()

choice()

