values =[10,5,6,0,9,8,2]

for value in values:
    try:
        print(10/ value)
    except ZeroDivisionError as Error: #behandlet nur zero error
        print(str(Error)) #Print the error message