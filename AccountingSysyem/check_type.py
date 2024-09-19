def get_int():
    incorrect=True
    while incorrect:
        try:
            number = int(input())
            incorrect =False
        except ValueError:
            print("Please Enter the number")
    return number

def get_float():
    incorrect=True
    while incorrect:
        try:
            number = float(input())
            incorrect =False
        except ValueError:
            print("Please Enter the float value")
    return number

def get_positive_int():
    incorrect=True
    while incorrect:
        try:
            number = int(input())
            if number>0:
                incorrect =False
            else:
                print("Please Enter the positive number")
        except ValueError:
            print("Please Enter the positive number")
    return number

def get_positive_float():
    incorrect=True
    while incorrect:
        try:
            number = float(input())
            if number>0:
                incorrect =False
            else:
                print("Please Enter the positive float number")
        except ValueError:
            print("Please Enter the positive float number")
    return number

def get_range():
    incorrect=True
    while incorrect:
        try:
            number = str(input())
            if number =="":
                incorrect =False
            else:
                number=int(number)
                if number>0:
                    incorrect =False
                else:
                    print("Please enter the positive number or Enter")
        except ValueError:
            print("Please enter the positive number or Enter")
    return number