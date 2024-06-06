# Accumulator mmethod - imperative programming
def revList(lst):
    accumulator= []
    
    for x in lst:
        print(accumulator)
        accumulator = [x] + accumulator
    
    return accumulator

def recRevList(lst):
    ''' Recursion of a list
    '''
    # base condition
    if lst == []:
        return []
    
    restrev = recRevList(lst[1:])
    first = lst[0:1]

    result = restrev + first

    return result

def recRevString(s):
    ''' Recursion of a string
    '''
    # base condition
    if s == "":
        return ""
    
    restrev = recRevList(s[1:])
    first = s[0:1]

    result = restrev + first

    return result

def recRevList2(lst):
    def revListHelper(index):
        if index == -1:
            return []
        
        restrev = revListHelper(index-1)
        first = [lst[index]]

        result = first + restrev

        return result
    return revListHelper(len(lst) - 1)

def reverseSequence(seq):
    seq_type = type(seq)
    empty_seq = seq_type()

    if seq == empty_seq:
        return empty_seq
    
    restrev = reverseSequence(seq[1:])
    first = seq[0:1]
    result = restrev + first

    return result

def main():
    print(revList([1,2,3,4]))

if __name__ == "__main__":
    main()