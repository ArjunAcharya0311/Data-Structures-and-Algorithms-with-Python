'''recursive function that swaps every two elements of the original string'''

def swap(s):
    if s == "":
        return ""
    elif len(s) == 1:
        return s

    result = s[1] + s[0] + swap(s[2:])

    return result

def main():
    test_cases = {
        "arjun" : "raujn",
        "jnaskjbs" : "njsajksb",
        "wehibrer" : "ewihrbre"
    }

    for k, v in test_cases.items():
        assert swap(k) == v

if __name__=='__main__':
    main()