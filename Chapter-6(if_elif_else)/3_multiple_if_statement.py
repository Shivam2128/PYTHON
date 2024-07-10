a = int(input('enter your age :'))


# if statement  no. 1
if(a%2 == 0):
    print('a is even')

# if statement no. 2
if(a>=18):
    print("you are above the age consent")
    print('good for you')

elif(a<0):
    print('you are giving invalid age')


# elif(a==0):
#     print('you are giving 0 it is not valid')
     
else:
    print('you are below the age of consent')
    print('not aligible')


print('end program')