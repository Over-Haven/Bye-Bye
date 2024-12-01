valid = False

while not valid:
    try :
        n = int(input("Enter a number: "))
        while 0%2 == 0 :
         print("Bye")
         valid = True
    except ValueError:
        print("Invalid")