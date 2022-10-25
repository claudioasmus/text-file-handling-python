def count():
    cnt=0
    f=open("quotes.txt","r")
    x=f.read()
    list=x.split()
    word=input("\tEnter the word : ")
    for i in list:
        if i.lower()==word.lower():
            cnt+=1
    print('\t Word\'',word,'\'is present',cnt,'times')
    f.close()
    print("*"*65)

def vowline():
    f=open('quotes.txt','r')
    x=f.readlines()
    print('\tLines starting with vowels: ')
    line=1
    for i in x:
        if i[0].lower() in 'aeiou':
            line+=1
            print('\tLine no.',line,':',i)
    f.close()
    print("*"*65)

def vowel():
    f=open('quotes.txt','r')
    x=f.read()
    list=x.split()
    print("\tWords starting with vowels :")
    for i in list:
        if i[0].lower() in 'aeiou':
            print('\t\t     ',i)
    f.close()
    print("*"*65)

choice=0
print("|----------------------EXPERIMENT NO. 5-------------------------|")
print("|                     TEXT FILE READING                         |")
print("-"*65,'\n \t\tCONTENT OF FILE :')
f=open('quotes.txt','r')
x=f.read()
print(x)
f.close()
print("-"*65)
while (choice!='4'):
    print("      1. Search and Count a word")
    print("      2. Show lines beginning with vowel")
    print("      3. Show words beginning with vowel")
    print("      4.             EXIT")
    choice=input("\tEnter your choice(1/2/3/4) : ")
    print("*"*65)
    if choice=='1':
        count()
    elif choice=='2':
        vowline()
    elif choice=='3':
        vowel()
    elif choice!='1'and choice!='2'and choice!='3'and choice!='4':
        print("\tWrong input enter again")
        choice=int(input("\tEnter your choice(1/2/3/4) : "))
else :
    print("\t\t-->Exiting loop")
    
