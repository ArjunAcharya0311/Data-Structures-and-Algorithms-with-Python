'''
Recursive function called intpow that given a number, x, and an integer, n, computes x^n.
'''

def intpow(x, n):
    if n == 0:
        return 1
    
    result = x * intpow(x, n-1)

    return result

def main():
    mult = intpow(3,9)
    print(mult)

    test_cases()

def unittest(x, n):
    mult = intpow(x, n)
    assert mult == x**n

def test_cases():
    x_list = [2, 3, 0.5, 1/4]
    n_list = [10, 9, 8, 7]

    for i in range(len(x_list)):
        unittest(x_list[i], n_list[i])

if __name__=='__main__':
    main()