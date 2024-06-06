'''Recursive function that computes the length of a string'''

def length(s):
    if s == "":
        return 0
    
    l = 1 + length(s[1:])

    return l

def main():
    s = input("Enter your string \n")

    l = length(s)

    print(l)

if __name__=='__main__':
    main()