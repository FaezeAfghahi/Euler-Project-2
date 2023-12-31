
"""
Created on Sun Dec 31 12:23:39 2023
 EULER PROJECT 2
 Even Fibonacci Numbers
 
@author: FAEZE AFGHAHI
"""

def isEVEN(n):
    if n % 2 == 0:
        return True
    else:
        return False

first = 1
second = 2
sum = 0
while (first < 4000000) :
    print(first)
    new = first + second
    if isEVEN(first)== True:
        sum = sum + first
    else:
        sum = sum
    first = second
    second = new
    
print('sum is :', sum)