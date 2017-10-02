

#count the number of even numbers in the array 
def countEvens(A):
    count = 0

    for i in range(len(A)):
        if(A[i] % 2 == 0):
            count = count +1
    return count



#Return true if an array contains the number 2 twice in a row:
def twoTwos(A):
    for i in range(len(A)-1):
        if(A[i] == 2 and A[i+1]==2):
                return True 
    return False



#Main

print('Count the number of even numbers in the array: A = [1,2,3,4,5,6,7]')
print(countEvens([1,2,3,4,5,6,7]))

print('Return true if an array contains the number 2 twice in a row: A = [1,1,2,1,1,2,1,2,1,2,2]')
print(twoTwos([1,1,2,1,1,2,1,2,1,2,2]))
print('[1,1,1,1,2,1,2,1,2,1,2,1,2]')
print(twoTwos([1,1,1,1,2,1,2,1,2,1,2,1,2]))


