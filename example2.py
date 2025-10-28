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