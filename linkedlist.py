from classnode import*
def MainMenu():
    print("1.Create a List")
    print("2.Add at Beginning")
    print("3.Add After")
    print("4.Delete")
    print("5.Display")
    print("6.Count")
    print("7.Reverse")
    print("8.Search")
    print("9.Exit")
    Choices()
Link = LinkedList()
def Choices():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amt = int(input("How many nodes you want: "))
        for i in range(amt):
            value = int(input("Enter the Element: "))
            Link.appendelement(value)
    elif choice == 2:
        add = int(input("Enter the Element: "))
        Link.AddAtbeginning(add)
        print('List is: ', end='')
        Link.display()
    elif choice == 3:
        add = int(input("Enter the Element: "))
        pos = int(input("Enter the position after which this element is inserted: "))
        Link.AddAfter(add,pos)
        print('List is: ', end='')
        Link.display()
    elif choice == 4:
        delete= int(input("Enter the element for deletion: "))
        Link.delete(delete)
    elif choice == 5:
        print('List is: ', end='')
        Link.display()
    elif choice == 6:
        print ("Number of Elements are: " ,Link.count())
    elif choice == 7:
        Link.reverse()
        print('List is: ', end='')
        Link.display()
    elif choice == 8:
        find = int(input("Enter the Element to be searched: "))
        SEARCH = Link.search(find)
        if SEARCH == -1:
            print(str(find) + ' was not found.')
        else:
            print(str(find) + ' is at index ' + str(SEARCH) + '.')
    elif choice == 9:
        quit()
    elif choice == "":
        print("Invalid Input")
    else:
        print("Invalid Input")
    print (" ")
    print(" ")
    MainMenu()
MainMenu()



