#word problem; Take two input from a user, one will be an integer and the other a float, then multiple the result to get an output 
int_text=input('input an interger number:')
int_num=int(int_text)
float_text=input('input a float number:')
float_num=float(float_text)
result=int_num*float_num
print('print result:', result)

#A better way of writing the code
int_num=int(input('enter an interger number:' ))
float_num=float(input('enter a float number:'))
result=int_num*float_num
print('your result is:', result)

# using the built in power function you can pass two values
base_num=int(input('enter base number:'))
power_num=int(input('enter power number:'))
result=pow(base_num, power_num)
print('your result is:',)

#to select a random number from(0,10), use an inbuilt function called random 
random_num=random.randint(0,10)
print(random_num)

# to get a floor division of a number use double divide sign
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
result=num1//num2 #you can use math.floor(num1/num2)
print('your result is:', result)

#use the math function 
import math
result=math.floor(3.4)
print(result)

#to swipe variable use the Temp
a=5
b=7
print('a,b',a,b)
temp=a
a=b
b=temp
print('a,b'a,b)

#Write a code to determine the largest number 

num1= int(input('enter the first number:'))
num2=int(input ('enter the second number:'))
if num2>=num1
  print('num2 is greater than num1')
else:
  print('num1 is greater')
  
#Alternatively import the max function 
num1= int(input('first number:'))
num2= int(input('second number:') )
largest=max(num1,num2)
print('the largest number is:', largest)

#find the max of 3 numbers

num1= int(input('enter the first number:'))
num2=int(input ('enter the second number:'))
num3=int(input('enter the third number:'))
if (num2>=num1) and (num2>=num3):
  print('num2 is the largest')
elif (num3>=num1) and (num3>=num2):
  print ('num3 is the largest')
else:
  print('num1 is the largest')
#alternatively the max function can be used

#find the average of numbers a user entered 

len = int(input("How many numbers do you want to enter? "))
 
nums = []
 
for i in range(0, len):
   element = int(input("Enter element: "))
   nums.append(element)
 
total = sum(nums)
avg = total/len
print("Average of elements you entered",round(avg,2))




  



