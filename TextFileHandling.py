f_name = 'index'
def create():
    addMore = 'y'
    global f_name
    f_name = input("\t   Enter the name of file to create : ")
    f = open(f_name + ".txt" , 'w')
    print("\t        The file",f_name,"has been created")
    f.close()
def append():
    f=open(f_name + ".txt" , 'a')
    num ='#'
    while not num.isnumeric():
        num=input("\t Enter the number of records to add : ")
        if not num.isnumeric():
            print("\t\t   Enter a valid input")
    num=int(num)
    for i in range(num):
        code = input("\t       Enter the item code  : ")
        name = input("\t       Enter the item name  : ")
        cost = input("\t       Enter the item price : ")
        print("-"*65)
        f.write(code.ljust(15)+name.ljust(15)+cost+"\n")
    print("\t\t    Record successfully added")
    f.close()
def read():
    f=open(f_name + ".txt")
    print("*"*65)
    for i in f:
        print('\t     ',i,end='')
    print("*"*65)
    f.close()

#MAIN PROGRAM

def MAIN():
    choice='0'
    print("|----------------------EXPERIMENT NO.03-------------------------|")
    print("|                     TEXT FILE HANDLING                        |")
    while(choice!='4'):
        print("-"*65)
        print("\t\t 1: Create a file")
        print("\t\t 2: Add data")
        print("\t\t 3: Display the contents")
        print("\t\t 4: EXIT")
        choice=input("\t\t  Enter your choice : ")
        if choice == '1':
            create()
        elif choice == '2':
            append()
        elif choice == '3':
            read()
        elif choice not in ['1','2','3','4']:
            print("\t    Wrong input; input numbers from 1 to 4")
MAIN()
