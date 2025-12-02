
def tuple_basics():
    my_tuple = ("string", 1, 2)
    print(my_tuple)    

def my_func(*args):
    print(args.__class__)

if __name__ == "__main__":
    tuple_basics()
    my_func()