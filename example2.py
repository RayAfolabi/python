#word problem; Take two input from a user, one will be an integer and the other a float, then multiple the result to get an output 
int_text=input('input an interger number:')
int_num=int(int_text)
float_text=input('input a float number:')
float_num=float(flaot_text)
result=int_num*float_num
print('print result:', result)

#A better way of writing the code
int_num=int(input('enter an interger number:' ))
float_num=float(input('enter a float number:'))
result=int_num*float_num
print('your result is:', result)
