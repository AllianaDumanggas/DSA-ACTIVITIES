def DecimalToBInary(num):
    if num >= 1:
           DecimalToBInary(num // 2)
    print (num % 2, end= '')
#decimal number
num =int (input ('Enter a decimal number:'))

DecimalToBInary(num)

'break'
#code
num =int (input ('Enter a number:'))
scientific_format = "{:e}".format(num)
print (scientific_format)

num =int (input ('Enter a number:'))
