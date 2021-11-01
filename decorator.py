def dec(func):
    print("Hello somebody !")
    func()
    print("See you..")

@dec
def inner():
    print('You are welcome !')

inner