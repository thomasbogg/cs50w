def announce(f):
    def wrapper():
        print('About to run the function...')
        f()
        print('Done with the function.')
    return wrapper

@announce # decorator call
def hello():
    print('Hello, world!')

hello()

'''A good use of a decorator is to make sure that a user is logged in
before running some command'''
