#1.Find all the pairs whose sum is k

def pairs_in_array(list1,list2,length_ofone,length_ofsecond,k):
   for i in range(0,length_ofone):
       for j in range(0,length_ofsecond):
           if list1[i]+list2[j]==k:
               print(list1[i],list2[j])
                
                
list1 = list(map(int, input('Enter elements in array 1  : ').split()))
list2 = list(map(int, input('Enter elements in array 2  : ').split()))
k = int(input('Enter sum to be compared : '))
length_ofone = len(list1)
length_ofsecond = len(list2)
pairs_in_array(list1,list2,length_ofone,length_ofsecond,k)

#2.Find mean and median of elements in a list

list_of_numbers_for_mean = [6, 9, 2002, 2004, 1999]
n = len(list_of_numbers_for_mean)
  
get_sum = sum(list_of_numbers_for_mean)
mean = get_sum / n
  
print("Mean: " + str(mean))

list_median = [6, 9, 1999, 2002, 2004]
n = len(list_median)
list_median.sort()
  
if n % 2 == 0:
    median1 = list_median[n//2]
    median2 = list_median[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = list_median[n//2]
print("Median is: " + str(median))

#3.Write a Python program to remove an item from a tuple.

n = ( "n", "i", "s", "h", "i", "t", "a", ".g", "x")
n = n[:2] + n[2:]
listx = list(n) 
listx.remove("x") 
n = tuple(listx)

print(n)

#4.Write a Python program to reverse a tuple.

def Reverse(tuples):
    n = tuples[::-1]
    return n
tuples = ("n", "i", "s", "h", "i", "t", "a", ".g")
print(Reverse(tuples))

#5.Write a Python program to find maximum and the minimum value in a set.
def MAX(sets):
    return (max(sets))
sets = set({8, 9, 24, 25, 69, 3, 10, 65, 55})
print(MAX(sets))

def MIN(sets):
    return (min(sets))
sets = set({8, 9, 24, 25, 69, 3, 10, 65, 55})
print(MIN(sets))

#6.Write a Python Program to print multiplication and sum of all the elements in a set.

list_n = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list_n.append(numbers)
print("Sum of elements in given list is :", sum(list_n))

def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
n = [6, 9, 10, 12]
print("Multiplication of elements in given list is: ", multiplyList(n))

#7.Kth largest number in a list
