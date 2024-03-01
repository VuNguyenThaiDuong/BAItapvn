def mergesort(sequence):
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2    

    left_sequence = mergesort(sequence[:mid])
    right_sequence = mergesort(sequence[mid:])

    return merge(left_sequence, right_sequence)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result
fi = open( "SL10.txt" , 'r')
test  = fi.readline().split(",")
test = list(map(float,test))
print(mergesort(test))

                                          
                                           
                                  

