#DATA STRUCTURES

#Number : INT etc
print(int(-1/2)) 

#Boolean : not, ^ [(a and not b) or (not a and b)], and , or
if True or False and False : 
   print("And has preceedence")

#String : Immutable
string = "This is a String"
print(string)

#List : Mutable
list = [1,"Thats a list", 2]
print(list)
list.append(4)
print(list[1])
print(list[0:1]) 
print(len(list)) 

#Tuple : Immutable
tuple = (1,"Thats a list", 2)
print(tuple)

#Set : Ordered Unique ELements
list = [1,2,4,3,2,3]
print(set(list))

#LOOPS
#while loop
i = 1
while i < 10 :
   print(i)
   i += 1

#for loop
for i in range(0, 10) :
   print(i)

for i in range(0, 10, 2):
   print(i)
   
for i in range(0, 10, -2):
   print(i)

#advanced for loop
s = "Hello"
for i in s:
   print(i)

l = [(1,2),(3,4)]
for i,j in l:
   print(i,j)

#FUNCTIONS
def factorial(k):
  if (k > 0):
    if (k == 1): 
         return 1
    result = k * factorial(k-1)
  else :
    result = 0
  return result
  
print(factorial(1))
