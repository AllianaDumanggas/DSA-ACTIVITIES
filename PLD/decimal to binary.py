print("Hello, Welcome to Scientific Converter")
print("SCIENTIFIC CONVERTER")
answer = input("Do you want to start?: yes or no?: ")
answer = answer.lower()

while (answer == 'yes'):
    num = int(input('Please enter a positive number:'))
    if num > 0:
        scientific_format = "{:e}".format(num)
        print(scientific_format)
    elif num < 0:
        print ('Please enter a positive number only')

    answer = input("Do you want to try once more?: yes/no: ")
    if (answer == 'no'):
        break

if (answer == 'no'):
    print("Thank you for using this converter, Have a nice day!")
else:
    print("You have written a wrong input")







