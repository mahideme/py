# a= int(input("enter the first number \n"))
# b= int(input("enter the second number\n"))
# print(a+b)
# c= input("enter your name \n>")
# d= input("enter your age \n>")
# print("hello",c, "you are", d, "years old!" )
# print(type(c))
# f = ["apple", "mango", "banana", "orange"]
# print(f[0])
# e= '''hello 
# this is mahlet
# and i'm study python now   
# and i hope i will be smart'''
# print(e)
# g= "hello world"
# print(g[5])
        
        #list
# 
# 

          # dictionary. 
# h= {1: "doing",2:"hard", "mahlet": "demeke"}
# print(h["mahlet"], h[1], h[2])

         # if , elif, else, nested if
# num=int(input("enter any number\n"))
# if num>0:
#     print("the number is positive")
#     if num>9 and num<=99: print("the number is two digit")
#     elif num>99:print("the number is more than two digit")
#     else:print("the number is one digit")
#     if True:print("the number is",num, "!!")
# elif num==0: 
#     print("the number",num, "is zero") 
#     if True:print(num, "is nothing??")   
#     if 1:print("i don't know!") 
# else: print("the number", num, "is negative") 
     #***************************************
# user=input("enter your username please\n ->") 
# pw=int(input("enter the password\n ->"))
# if user=="mahlet":
#     if pw==123:
#        print("Welcom!", user)
#     else:
#         print("wrong password")
# else:
#     print("access deined")

# grade=int(input("enter out of 100\n"))
# if grade>80: print("A")
# elif grade>=60: print("B")
# elif grade>=50: print("C")
# elif grade>=45: print("D")
# else: print("failed")

# distance=int(input("enter the distance\n"))
# time=int(input("enter the time\n"))
# speed=distance/time
# print("the speed is", speed,"km/hr")
# if speed>=40: print("you are fast, cool down")
# elif speed>=20 and speed<40: print("you are on good speed")
# elif speed>0: print("you are so slow")
# else: print("you are stopped!")
                        #loop
          ######for loop   
# for z in 1,2,3,4,5: print(z)
'''n = [1,2,3,4,5]
   for z in n: print(z)'''
# the above 2 are the same shit they print the number 1 to 5

# for hi in "hello world": print(hi) #it also print each words in a line

# print(list(range(110)))
# print(len(range(10)))
'''a=[1,3,3,2,5,3,2,3,3,2,2] 
print(len(a))'''
# length and list 


# for i in range(10): print("hello world")
'''range=[1,2,3,4,5,6,7,8,9,10]
for i in range: print("hello world")'''
#the above two codes are the same they print the string(hello world) 10 times

# for i in range(10):
#     if i%2==0: print(i,"-the number is even")
#     else: print(i,"-the number is odd")
'''a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    b=i%2
    if b==0: print("the number ",i," is even")
    else: print("the number ",i," is odd")'''
# the above two codes assign the number if it is even or odd

# print(10*"hello world  ")  # loo[ with print. the output is single lined.
# below down there is other way of writting for the above two but i don't know how????????
#[print(i, "- the number is even") if i % 2 == 0 else print(i, "- the number is odd") for i in range(10)]
# may be it because python is most likely oop rather than procedural programming 
# [print("Hello, world!") for _ in range(10)]


'''a= ['mahi', 'babi','sari', 'tring', 'deme']
b= input("enter the name\n->")
for i in a:
    if i==b: 
        print(b, " is family member")
        break
else: print(b," is not family member")'''

'''user={"abe":85,"debe":94}
inpt=input("enter the student name")
for stud in user: 
    if stud==inpt:
        print(stud,"your average is ", user[stud])
        break
else: print("there is no name found with", inpt)'''
# the above two are for loop with else and break

         ########## while loop
'''a=1
while a<=10:
    print(a, "Hello World!")
    a+=1'''
# print(10*"hello world  ")  # loo[ with print. the output is single lined.
# listing from 1 to 10 and hello world 10 times. we can do them separatlly.

'''while True:
    print("infinite loop")'''
# infinity loop 
### can be stoped by ctrl+c in the consul part!

'''user= int(input("enter the number"))
a=1
sum=0
while a<=user:
    sum=sum+a
    a+=1
print("the sum is", sum)'''
# a program which add number up to the input

'''a=1
while a<=3000:
    print(a)
    if a==2012: break
    a+=1'''
# a program that list number until 3000 and when it is 2012 it will stop by using break.


                      #Exceptions
'''try: 
    user= int(input("enter a pin\n -")) 
    print("you have enterd!\nyour entry is", user ) 
except:
    print("please enter only numbers!")'''
#### try and execpt

"""l= [4,"a", 6, 0, 9]
for i in l:
    try:
        print("entry= ",i)
        r=1/int(i)
        print("the resprocal of ", i , "is ", r,"\n")
    except ZeroDivisionError:
        print("any number cannot be divided by 0\n")   
    except ValueError:   
        print("divide only number")
        print("next try\n")
print("successfully finished")"""
### specific Exceptions like ZeroDivisionError, ValueError, TypeError, RuntimeError



