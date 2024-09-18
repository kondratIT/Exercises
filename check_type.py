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

def get_positive_number():
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