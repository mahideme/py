users={'Nathan':2313,'Geez':'pass231','Abebe':'092313133','Miki':"pl3s34D0n'tH4ckM3"} # stored username and password in dictionar format.
a=1  # to display welcoming message or to limit trying.
for i in range(5): # for incorrect username and password it give a chance to try up to 5 times.
    uname=input("Username -> ")  
    passwd=input("Password -> ")
    if uname in users:  # True -- if the input username belongs in the stored dictionary.
        if type(passwd)!=type(users[uname]): # by defult any input is string. option for other data type. 
            try: # to handle the specific error-- string password!
                passwd=int(passwd) # changes the input password data type to integer. 
                if passwd in users.values(): # check if the converted password is same with the username password in the dictionary.
                    a=-1 
                    break # to stop and leave the loop.
                else: # incorrect password.
                    print("Incorrect Login1!")  #1st error.
                    a=1
            except: # handls input datatype error.
                print("Incorrect Login!2")  #2nd error.  
                a=1
        elif passwd in users.values(): # for defoult input datatype and correct password.
            a=-1
            break
        else: #2 for defoult input datatype and incorrect password. 
            print("Incorrect Login!3") ## 3rd error
            a=1
    else:  #3 the input username didn't belong to the stored dictionary.
        print("Incorrect Login!4")  ## 4th error
        a=1
if a>0: # banned to login after 5 times trial.
    print("Sorry you are limited!")
else:  # successeful logined and acceptance acknowledgment
    print("Welcome to GTST Company!")

     



        