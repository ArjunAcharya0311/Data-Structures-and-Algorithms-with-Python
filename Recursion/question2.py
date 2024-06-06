'''Recursive function to compute factorial of an integer'''

def factorial(x):
    if x == 0:
        return 1
    
    f = x * factorial(x - 1)

    return f

def main():
    x = input("Enter number for factorial\n")

    f = factorial(int(x))

    print(f)

if __name__=='__main__':
    main()