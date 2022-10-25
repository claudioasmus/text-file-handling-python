def create():
    qList=[]
    global f_name
    f_name=input("      Enter the name of file to create : ")
    f=open(f_name+".txt",'w')
    print("\tGood to go, file created, Now....")
    n=int(input("\tEnter the no. of quotes to add : "))
    for i in range(n):
        quote=input('      '+str(i+1)+".   Enter the quote : ")
        qList=qList+['\n'+quote]
    f.writelines(qList)
    print("\t      The quotes have been added")
    print("*"*65)
    f.close()

def read():
    f_name=input("\tEnter the name of file to read : ")
    print("\tProcessing...")
    print("-"*65,end='')
    f=open(f_name+".txt", 'r')
    x=f.read()
    vowl=0
    num=0
    upper=0
    specialChar=0
    for i in x:
        if i.lower() in 'aeiou':
            vowl+=1
        if i.isnumeric():
            num+=1
        if i.isupper():
            upper+=1
        if not i.isalnum():
            specialChar+=1
    f.close()
    print(x)
    print("*"*65)
    print("*\t     No. of vowels present     :",str(vowl).ljust(22),"*")
    print("*\t     No. of digits present     :",str(num).ljust(22),"*")
    print("*\t     No. of uppercase letters  :",str(upper).ljust(22),"*")
    print("*\t     No. of special characters :",str(specialChar).ljust(22),"*")
    print("*"*65)
choice=0
print("|----------------------EXPERIMENT NO.04-------------------------|")
print("|                     TEXT FILE HANDLING                        |")
print("-"*65)
while (choice!='3'):
    print("      1. Create a file and enter quotes")
    print("      2. Read a file and get details")
    print("      3.             EXIT")
    choice=input("\tEnter your choice(1/2/3) : ")
    print("*"*65)
    if choice=='1':
        create()
    elif choice=='2':
        read()
    elif choice!='1'and choice!='2'and choice!='3':
        print("\tWrong input enter again")
        choice=int(input("\tEnter your choice(1/2/3) : "))
else :
    print("\t\t-->Exiting loop")
