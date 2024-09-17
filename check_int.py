def get_int():
    incorrect=True
    while incorrect:
        try:
            number = int(input())
            incorrect =False
        except ValueError:
            print("Please Enter the number")
    return number