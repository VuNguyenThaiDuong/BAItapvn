def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
       
        return quicksort(less)+equal+quicksort(greater)  
    else:  
        return array
fi = open( "SL1.txt" , 'r')
fo = open( "my.txt"  , 'w')
test  = fi.readline().split(",")
test = list(map(float,test))
print(quicksort(test))

