#Name: Lilliana Parra
#Github username: ParraL1
#Date: 01/19/2022
#Description: Asks for a number of integers, then takes the max and min of those integers

N=int(input("How many integers would you like to enter?\n"))
print("Please enter "+str(N)+" integers.")
firstVal=0
#first value from user and assign
minVal=int(input())
maxVal=0
#Loop inputs
for i in range(0,N-1):
    x=int(input())
    if x< minVal :
        minVal= x
    if x> maxVal :
         maxVal=x

#Print results of loop
print("min:",minVal)
print("max:",maxVal)