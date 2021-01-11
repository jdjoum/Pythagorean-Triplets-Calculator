def find_Pythagorean(upperLimit):
    rows, cols = (upperLimit, 3)
    array = [[0 for i in range(cols)] for j in range(rows)] 
    count = 0
    c = 0
    m = 2
    while(c < upperLimit):
        for n in range(1,m+1):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            if(c > upperLimit):
                break
            if(a == 0 or b == 0 or c == 0):
                break
            array[count][0] = a
            array[count][1] = b
            array[count][2] = c
            count += 1
            print("\nPythagorean Triplets ", count, ": ",a ,b , c)
        m += 1
    print("\nAll the Pythagorean Triplets under the upper limit of: ", upperLimit)
    finalRows, finalCols = (count, 3)
    finalArray = [[0 for i in range(finalCols)] for j in range(finalRows)] 
    for i in range(0, count):
        for j in range(0, 3):
            finalArray[i][j] = array[i][j]
        i += 1
    print("\nFinal Pythagorean Triplets Array: ")    
    print("\n",finalArray)
    return finalArray
        
print("Welcome to the Pythagorean Triplets Calculator!")
limit = int(input("Enter the upper limit for the: "))
find_Pythagorean(limit)